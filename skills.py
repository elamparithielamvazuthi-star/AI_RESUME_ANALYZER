from preprocess import preprocess_text

SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "sql",
    "mysql",
    "flask",
    "django",
    "react",
    "nodejs",
    "machine",
    "learning",
    "tensorflow",
    "pytorch",
    "ai",
    "cloud",
    "aws",
    "azure",
    "docker",
    "git",
    "github"
}

def extract_skills(text):

    words = preprocess_text(text)

    found_skills = []

    for word in words:
        if word in SKILLS:
            found_skills.append(word)

    return found_skills

def compare_skills(resume_skills, job_skills):

    matched = []

    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing

resume = """
Python Java HTML CSS Machine Learning Git
"""

job = """
Python SQL Flask Machine Learning AWS Git
"""

resume_skills = extract_skills(resume)

job_skills = extract_skills(job)

print("Resume Skills:")
print(resume_skills)

print()

print("Job Skills:")
print(job_skills)
matched, missing = compare_skills(resume_skills, job_skills)

print()

print("Matched Skills:")
print(matched)

print()

print("Missing Skills:")
print(missing)

print()

match_percentage = (len(matched) / len(job_skills)) * 100

print("Skill Match Percentage:")
print(round(match_percentage, 2), "%")