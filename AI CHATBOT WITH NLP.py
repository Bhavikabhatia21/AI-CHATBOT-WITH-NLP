from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

career_data = {
    "Python": {
        "career": "Backend Developer / Data Scientist",
        "roadmap": [
            "Learn Advanced Python",
            "Learn Django or Flask",
            "Build Projects",
            "Apply for internships"
        ],
        "salary": "4-10 LPA (India)"
    },
    "Java": {
        "career": "Java Developer / Android Developer",
        "roadmap": [
            "Learn Core Java",
            "Learn Spring Boot",
            "Build REST APIs",
            "Apply for internships"
        ],
        "salary": "4-9 LPA (India)"
    },
    "Machine Learning": {
        "career": "ML Engineer / AI Engineer",
        "roadmap": [
            "Learn Python",
            "Learn Numpy & Pandas",
            "Learn Machine Learning",
            "Build ML Projects"
        ],
        "salary": "6-15 LPA (India)"
    },
    "Data": {
        "career": "Data Analyst",
        "roadmap": [
            "Learn Excel",
            "Learn SQL",
            "Learn Power BI",
            "Build Dashboard Projects"
        ],
        "salary": "4-8 LPA (India)"
    }
}

# Preprocess text
def preprocess(text):
    tokens = text.lower().split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Detect skills
def detect_skills(user_input):
    text = user_input.lower()
    skills = []

    if "python" in text:
        skills.append("Python")
    if "java" in text:
        skills.append("Java")
    if "machine learning" in text or "ml" in text:
        skills.append("Machine Learning")
    if "data" in text:
        skills.append("Data")

    return skills

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    data = request.get_json()
    msg = data["msg"]

    # Greeting
    if any(word in msg.lower() for word in ["hi", "hello", "hey"]):
        return jsonify({"response": "Hello 👋 I am your AI Career Mentor. Tell me your skills!"})

    # Detect skills
    skills = detect_skills(msg)

    if skills:
        reply = "Based on your skills (" + ", ".join(skills) + "), you can consider:\n\n"

        for skill in skills:
            info = career_data.get(skill)
            if info:
                reply += f"🔹 Career: {info['career']}\n"
                reply += f"💰 Salary: {info['salary']}\n"
                reply += "➤ Roadmap:\n"
                for step in info["roadmap"]:
                    reply += f"   - {step}\n"
                reply += "\n"

        return jsonify({"response": reply})

    if "bye" in msg.lower():
        return jsonify({"response": "Goodbye! Best of luck for your career 🚀"})

    if "thank" in msg.lower():
        return jsonify({"response": "You're welcome 😊"})

    return jsonify({"response": "Please tell me your skills like Python, Java, ML, Data."})

if __name__ == "__main__":
    app.run(debug=True)