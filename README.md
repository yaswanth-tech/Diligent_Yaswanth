Ironman Jarvis

Ironman Jarvis is a professional AI-powered enterprise assistant built using Retrieval-Augmented Generation principles. The application allows users to inject company-specific knowledge dynamically and receive accurate, context-aware responses using a large language model. The system is designed for internal enterprise usage with a clean UI and simple architecture.

Project Description

This project demonstrates how an enterprise assistant can be built using Streamlit and an open-source large language model. The assistant answers questions strictly based on the context provided by the user, avoiding hallucinations. The application uses Mistral-7B-Instruct-v0.2 through Hugging Face and LangChain for orchestration.

Technology Stack

Frontend: Streamlit
Language Model: Mistral-7B-Instruct-v0.2
AI Framework: LangChain
Model Hosting: Hugging Face Hub
Language: Python
Styling: Custom CSS

Project Structure

Diligent_Jarvis
app.py
requirements.txt
style.css
.env
README.md

Environment Requirements

Python version 3.8 or higher
Hugging Face account
Hugging Face API token

Installation and Setup

Step 1: Clone the repository

git clone https://github.com/YourUsername/Diligent_Jarvis.git

cd Diligent_Jarvis

Step 2: Create and activate virtual environment

python -m venv venv

Windows:
.\venv\Scripts\activate

Mac or Linux:
source venv/bin/activate

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Create environment variable file

Create a file named .env in the root directory and add:

HF_TOKEN=your_hugging_face_token_here

Do not upload the .env file to GitHub.

Running the Application

Start the application using:

streamlit run app.py
