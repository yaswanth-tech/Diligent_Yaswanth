import streamlit as st
import os
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Diligent Jarvis", page_icon="🤖")

HF_TOKEN = "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"
PINECONE_TOKEN = "pcsk_6GK8Kj_TZviVeSiurmGi5UsmE2WKvB1EsZ6SFq4oefAJc5gHkWfZ9Y5fV94fucpLnmw87b"

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_resource
def create_client():
    client = InferenceClient(token=HF_TOKEN)
    return client

def get_ai_response(question, company_context):
    client = create_client()
    messages = [
        {
            "role": "system",
            "content": "You are a helpful enterprise assistant. Use the given company data to answer user questions.\n\nCompany Data:\n" + company_context
        },
        {
            "role": "user",
            "content": question
        }
    ]
    try:
        response = client.chat_completion(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=messages,
            max_tokens=500,
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as error:
        return "AI connection error: " + str(error)

st.title("🤖   Ironman Jarvis")

if "knowledge_base" not in st.session_state:
    st.session_state.knowledge_base = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "System ready. Ask your questions."}
    ]

with st.sidebar:
    st.header("Knowledge Base")
    company_data = st.text_area("Paste Company Data Here:", height=150)
    if st.button("Train Jarvis"):
        st.session_state.knowledge_base = company_data
        st.success("Knowledge base updated successfully!")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Ask a question...")

if user_question:
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.write(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            context_data = st.session_state.knowledge_base if st.session_state.knowledge_base else "No company data provided."
            ai_reply = get_ai_response(user_question, context_data)
            st.write(ai_reply)
    
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
