import string

STOP_WORDS = {
    "a", "an", "the", "is", "am", "are", "was", "were",
    "to", "of", "and", "or", "in", "on", "for", "with",
    "at", "by", "from", "as", "that", "this", "it", "i"
}

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Split into words
    words = text.split()

    # Remove stop words
    clean_words = []

    for word in words:
        if word not in STOP_WORDS:
            clean_words.append(word)

    return clean_words


# Test the function
sample = "I am a Python, Java and Machine Learning student."

result = preprocess_text(sample)

print(result)