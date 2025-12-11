import streamlit as st
import analytics

analytics.load_analytics()
st.set_page_config(
    page_title="Notexa -Learning Made Simple.",
    page_icon="assets/logo.png"
)
import requests
import os
from dotenv import load_dotenv
from fpdf import FPDF
import io

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"
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

                # --- PDF Generation ---
                pdf = FPDF()
                pdf.set_left_margin(15)
                pdf.set_right_margin(15)
                pdf.add_page()
                pdf.set_font("Arial", size=14)
                pdf.cell(0, 10, "Summary", ln=True, align="L")
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(180, 10, summary.strip() if summary else "No summary found.")
                pdf.ln(5)
                pdf.set_font("Arial", size=14)
                pdf.cell(0, 10, "Quiz Questions", ln=True, align="L")
                pdf.set_font("Arial", size=12)
                if quiz:
                    for idx, q in enumerate(quiz, 1):
                        safe_q = q.replace("\n", " ")
                        pdf.multi_cell(180, 10, f"{idx}. {safe_q}")
                else:
                    pdf.multi_cell(180, 10, "No quiz found.")
                pdf.ln(5)
                pdf.set_font("Arial", size=14)
                pdf.cell(0, 10, "Answers", ln=True, align="L")
                pdf.set_font("Arial", size=12)
                if answers:
                    for idx, a in enumerate(answers, 1):
                        safe_a = a.replace("\n", " ")
                        pdf.multi_cell(180, 10, f"{idx}. {safe_a}")
                else:
                    pdf.multi_cell(180, 10, "No answers found.")
                # Output PDF to memory (fixed for fpdf)
                pdf_bytes = pdf.output(dest='S')
                pdf_buffer = io.BytesIO(pdf_bytes)
                st.download_button(
                    label="Download Summary & Quiz as PDF",
                    data=pdf_buffer,
                    file_name="summary_quiz.pdf",
                    mime="application/pdf"
                )
    else:
        st.warning("Please enter a topic or question.")

# --- Go Premium Button in Sidebar ---
st.sidebar.markdown('''<hr style="margin-top:2em;margin-bottom:0.5em;">''', unsafe_allow_html=True)
st.sidebar.markdown('''
    <a href="/premium" target="_self" style="
        display: block;
        background: linear-gradient(90deg, #FFD700 0%, #FFB300 100%);
        color: #222;
        padding: 0.5em 1.2em;
        border-radius: 2em;
        font-weight: bold;
        font-size: 1.1em;
        text-align: center;
        text-decoration: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 2px solid #fff2b2;
        margin-top: 0.5em;
        margin-bottom: 1em;
        transition: background 0.2s;
    " onmouseover="this.style.background='#FFB300'" onmouseout="this.style.background='linear-gradient(90deg, #FFD700 0%, #FFB300 100%)'">
        🙏 Donate
    </a>
''', unsafe_allow_html=True)
st.sidebar.markdown(
    '<div style="margin-top:3em; margin-bottom:1em; font-size:1.05em;">'
    '📢 <b>Turn students and teachers into customers.</b> '
    '<a href="https://your-ad-link.com" target="_blank" style="color:#00b894; font-weight:bold; text-decoration:underline;">Advertise on Notexa</a>.'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('''
    <style>
    .notexa-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100vw;
        background: rgba(255,255,255,0.0);
        color: #888;
        text-align: center;
        font-size: 1em;
        padding: 0.7em 0 0.5em 0;
        z-index: 9999;
    }
    </style>
    <div class="notexa-footer">© 2025. Made with ❤️ by the Hirwa Leon</div>
    ''', unsafe_allow_html=True)
