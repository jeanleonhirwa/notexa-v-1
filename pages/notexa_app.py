import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-pro:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()
        return res.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ Gemini API error: {e}"

# --- Streamlit UI for Notexa ---
st.title("Notexa - AI Summary and Quiz Generator")
st.write("Enter a topic or question below. Notexa will generate a concise summary and a short quiz for you using Gemini AI.")

# Text input for topic
topic = st.text_input("Topic or Question:")

# Button to ask Gemini and display response
if st.button("Generate"):
    if topic:
        with st.spinner("Generating summary and quiz..."):
            prompt = (
                f"Give a short and clear summary about this topic: {topic}. "
                "Then generate 3 quiz questions with answers based on that topic."
            )
            response = ask_gemini(prompt)
            if response.startswith("❌"):
                st.error(response)
            else:
                # Debug: Show raw response (optional, comment out in production)
                # st.code(response)

                summary = ""
                quiz = []
                answers = []
                lines = response.splitlines()
                section = None

                for line in lines:
                    l = line.strip()
                    # Section detection
                    if l.startswith("### Summary"):
                        section = "summary"
                        continue
                    elif l.startswith("---") or l.startswith("***"):
                        section = None
                        continue
                    elif l.startswith("### Quiz Questions"):
                        section = "quiz"
                        continue

                    # Collect summary
                    if section == "summary" and l:
                        summary += l + " "
                    # Collect quiz questions (bold lines)
                    elif section == "quiz" and l.startswith("**") and l.endswith("**"):
                        quiz.append(l.strip("*").strip())
                    # Collect answers (handles both "**Answer:" and "> **Answer:")
                    elif section == "quiz" and (
                        l.lower().startswith("**answer:") or l.lower().startswith("> **answer:")
                    ):
                        # Remove leading '>' and asterisks, then strip
                        answer_text = l.lstrip("> ").strip("*").replace("Answer:", "").replace("answer:", "").strip()
                        answers.append(answer_text)

                st.subheader("Summary:")
                st.write(summary.strip() if summary else "No summary found.")
                st.subheader("Quiz:")
                if quiz:
                    for q in quiz:
                        st.write(f"- {q}")
                else:
                    st.write("No quiz found.")
                if answers:
                    st.subheader("Answers:")
                    for a in answers:
                        st.write(f"- {a}")
    else:
        st.warning("Please enter a topic or question.")