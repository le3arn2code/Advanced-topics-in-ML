# Layman Explanation

Think of DistilBERT as a student who learned from BERT (the teacher).
We train this student to read movie reviews and decide if people liked or hated the movie.

After training, we build a simple web service using Flask.
When you send a review, it replies instantly whether it's positive or negative.
