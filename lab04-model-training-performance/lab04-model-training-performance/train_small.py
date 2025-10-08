import tensorflow as tf, time
print('Training small model...')
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 784) / 255.0
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
start = time.time()
model.fit(x_train, y_train, epochs=1, batch_size=32, verbose=2)
print(f'Small model trained in', time.time() - start, 'seconds')
