from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    job_description = request.form["job"]

    if resume.filename == "":
        return "Please upload a resume."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    resume.save(filepath)

    with open(filepath, "r", encoding="utf-8") as file:
        resume_text = file.read()

    return f"""
    <h2>Resume Uploaded Successfully</h2>

    <h3>Resume Text</h3>

    <pre>{resume_text}</pre>

    <h3>Job Description</h3>

    <pre>{job_description}</pre>
    """


if __name__ == "__main__":
    app.run(debug=True)