import math

def cosine_similarity(vector1, vector2):

    dot_product = 0

    for word in vector1:
        if word in vector2:
            dot_product += vector1[word] * vector2[word]

    magnitude1 = 0

    for value in vector1.values():
        magnitude1 += value * value

    magnitude1 = math.sqrt(magnitude1)

    magnitude2 = 0

    for value in vector2.values():
        magnitude2 += value * value

    magnitude2 = math.sqrt(magnitude2)

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity
resume = {
    "python": 0.4,
    "java": 0.3,
    "machine": 0.2
}

job = {
    "python": 0.5,
    "java": 0.2,
    "html": 0.3
}

score = cosine_similarity(resume, job)

print("Similarity Score:")
print(score)

print()

print("Match Percentage:")
print(round(score * 100, 2), "%")