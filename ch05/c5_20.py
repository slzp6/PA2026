"""c5_20.py"""

SENTENCE = "A journey of a thousand miles begins with a single step."

words = SENTENCE.lower().replace('.', '').replace(',', '').split()
unique_words = {word for word in words if len(word) <= 5}

print(words)
print(unique_words)
