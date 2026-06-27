import math

# --------------------------------
# Term Frequency (TF)
# --------------------------------
def calculate_tf(words):
    tf = {}

    total_words = len(words)

    for word in words:
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1

    for word in tf:
        tf[word] = tf[word] / total_words

    return tf


# --------------------------------
# Inverse Document Frequency (IDF)
# --------------------------------
def calculate_idf(documents):
    idf = {}

    total_documents = len(documents)

    unique_words = set()

    for document in documents:
        unique_words.update(document)

    for word in unique_words:
        document_count = 0

        for document in documents:
            if word in document:
                document_count += 1

        idf[word] = math.log(total_documents / document_count)

    return idf


# --------------------------------
# TF-IDF
# --------------------------------
def calculate_tfidf(tf, idf):
    tfidf = {}

    for word in tf:
        if word in idf:
            tfidf[word] = tf[word] * idf[word]

    return tfidf


# --------------------------------
# Test Data
# --------------------------------
document1 = [
    "python",
    "java",
    "machine",
    "learning"
]

document2 = [
    "python",
    "html",
    "css"
]

documents = [document1, document2]

tf = calculate_tf(document1)

idf = calculate_idf(documents)

tfidf = calculate_tfidf(tf, idf)

print("TF:")
print(tf)

print()

print("IDF:")
print(idf)

print()

print("TF-IDF:")
print(tfidf)