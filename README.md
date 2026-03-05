# AI-CHATBOT-WITH-NLP
Company: CODTECH IT SOLUTION PVT.LTD

Name: BHAVIKA BHATIA

Intern Id: CTIS4942

Domain: Python Programming

Duration: 6 Weeks

Mentor: Neela Santosh


## Project Overview

The AI Career Mentor Chatbot is a simple web-based application that provides career suggestions based on the user's technical skills. The main objective of this project is to demonstrate how Natural Language Processing (NLP) can be used to understand user input and generate meaningful responses related to career guidance.

This chatbot allows users to enter their programming skills such as Python, Java, Machine Learning, or Data, and the system responds with possible career paths, expected salary ranges, and a basic learning roadmap. The chatbot acts as a simple career guidance assistant for students or beginners who want to explore career opportunities in the technology field.

The project is developed using Python with Flask as the backend framework, and it uses NLTK (Natural Language Toolkit) to perform basic natural language processing tasks such as removing stopwords and performing lemmatization.

The frontend interface is created using HTML, CSS, and JavaScript, which provides a clean and interactive chat interface where users can type their queries and receive responses instantly.

The chatbot works by analyzing the user input, detecting relevant technical skills, and then matching them with predefined career data stored in the application. Based on this information, it generates a response containing career options, salary expectations, and a step-by-step roadmap to help the user move forward in that career path.

This project demonstrates the integration of NLP concepts with web development, making it a useful learning experience for students who want to understand how AI-powered chat systems can be developed.

## Features

- The AI Career Mentor chatbot includes several useful features:

- Interactive chat interface for user interaction

- Basic Natural Language Processing using NLTK

- Detection of user skills from natural language input

- Career recommendations based on detected skills

- Display of possible job roles in the IT industry

- Estimated salary ranges for careers in India

- Step-by-step learning roadmap for each career path

- Greeting and exit responses for a conversational experience

- The chatbot can currently recognize skills such as Python, Java, Machine Learning, and Data, and it provides career suggestions accordingly.

## Technologies Used

- This project uses the following technologies and libraries:

## Programming Language

Python

## Backend Framework

Flask

Natural Language Processing Library

NLTK (Natural Language Toolkit)

## Frontend Technologies

HTML

CSS

JavaScript

## NLP Techniques Used

Stopword Removal

Lemmatization

Keyword Detection

## How the Chatbot Works

- The chatbot processes user queries through a simple NLP pipeline.

- First, the user enters their skills or a message in the chat interface. The message is sent to the Flask backend using a POST request.

- The backend then processes the text using basic NLP steps. Stopwords are removed from the input and words are lemmatized using the WordNet Lemmatizer from NLTK.

- Next, the system checks whether the message contains specific keywords related to programming skills such as Python, Java, Machine Learning, or Data. If a skill is detected, the chatbot retrieves the corresponding career information from the predefined dataset stored in the application.

- Finally, the chatbot generates a formatted response containing:

- Career role suggestions

- Estimated salary range

- A simple roadmap to learn the required skills

- This response is then sent back to the frontend and displayed in the chat interface.

## Example Interaction
User Input
Python, Data, ML
Chatbot Response

Career: Backend Developer / Data Scientist
Salary: 4–10 LPA (India)

## Roadmap

- Learn Advanced Python

- Learn Django or Flask

- Build Projects

- Apply for internships

- The chatbot may also suggest other careers such as ML Engineer or Data Analyst depending on the detected skills.

## Project Structure
INTERNSHIP
│
├── AI_CHATBOT_WITH_NLP.py
├── templates
│   └── index.html
├── static
│   ├── css
│   └── js
└── README.md

- AI_CHATBOT_WITH_NLP.py – Contains the Flask backend and chatbot logic
- index.html – Chat interface for user interaction
- static folder – Contains CSS and JavaScript files for UI design

## Conclusion

The AI Career Mentor Chatbot is a beginner-friendly project that demonstrates how Natural Language Processing can be integrated with web applications to build interactive AI systems.

Although the chatbot currently supports a limited number of skills, it can easily be extended by adding more career data and improving the NLP model to support more advanced queries.

This project helped in understanding the basics of Flask web development, NLP preprocessing, and chatbot design. It also provides a strong foundation for building more advanced AI-based career recommendation systems in the future.

## OUTPUT
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/ad57fd4a-6e4e-4cf9-abd0-8abd035294cb" />
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/b712eb59-7dcc-444d-a914-5651efb6193f" />
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/c598c2a0-a3f6-436d-b291-5fa7f11560d7" />
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/4a6af6d7-9cc7-4f20-b7c5-0995418a99a3" />
