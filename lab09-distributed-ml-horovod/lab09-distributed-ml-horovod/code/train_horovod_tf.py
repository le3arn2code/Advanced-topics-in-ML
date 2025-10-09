# nano code/train_horovod_tf.py
import tensorflow as tf
import horovod.tensorflow as hvd

hvd.init()
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
tf.config.threading.set_intra_op_parallelism_threads(2)
tf.config.threading.set_inter_op_parallelism_threads(2)

(mnist_images, mnist_labels), _ = tf.keras.datasets.mnist.load_data()
dataset = tf.data.Dataset.from_tensor_slices((
    tf.cast(mnist_images[..., tf.newaxis] / 255.0, tf.float32),
    tf.cast(mnist_labels, tf.int64)
))
dataset = dataset.repeat().shuffle(10000).batch(128)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, [3, 3], activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

optimizer = tf.keras.optimizers.Adam(0.001 * hvd.size())

@tf.function
def training_step(images, labels, first_batch):
    with tf.GradientTape() as tape:
        logits = model(images, training=True)
        loss = tf.reduce_mean(tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True))
    tape = hvd.DistributedGradientTape(tape)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    if first_batch:
        hvd.broadcast_variables(model.variables, root_rank=0)
        hvd.broadcast_variables(optimizer.variables(), root_rank=0)
    return loss

for batch, (images, labels) in enumerate(dataset.take(50)):
    loss = training_step(images, labels, batch == 0)
    if batch % 10 == 0 and hvd.rank() == 0:
        print(f"Step {batch}, Loss: {loss.numpy():.4f}")
