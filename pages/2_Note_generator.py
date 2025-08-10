import streamlit as st
import requests
import os
from dotenv import load_dotenv
from fpdf import FPDF

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
st.title("Notexa - AI Note Generator")
st.write("Enter a topic or question below. Notexa will generate easy detailed notes for you using Gemini AI.")

# Text input for topic
topic = st.text_input("Topic or Question:")

# Use session state to store notes
if 'notes' not in st.session_state:
    st.session_state['notes'] = ''

# Only show Generate button initially
if not st.session_state['notes']:
    if st.button("Generate"):
        if topic:
            with st.spinner("Generating notes..."):
                prompt = (
                    f"Generate academic detailed notes that are not too long and easy to understand about this topic: {topic}. Keep it simple."
                )
                response = ask_gemini(prompt)
                if response:
                    st.session_state['notes'] = response
                else:
                    st.error("Failed to generate notes. Please try again.")

if st.session_state['notes']:
    st.markdown("### 📑 Generated Notes:")
    st.write(st.session_state['notes'])
    # Prepare PDF with Unicode font (requires fpdf2 and DejaVuSans.ttf in project directory)
    import io
    pdf = FPDF()
    pdf.add_page()
    # Add Unicode font (DejaVuSans.ttf must be in the same directory or provide full path)
    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
    if not os.path.exists(font_path):
        # Download the font automatically if not present
        import urllib.request
        font_url = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf"
        try:
            with st.spinner("Downloading font for PDF export..."):
                urllib.request.urlretrieve(font_url, font_path)
        except Exception as e:
            st.error(f"Failed to download DejaVuSans.ttf: {e}")
            font_path = None
    if font_path and os.path.exists(font_path):
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_left_margin(15)
        pdf.set_right_margin(15)
        pdf.set_font("DejaVu", size=14)
        pdf.cell(0, 10, "Generated Notes", ln=True, align="L")
        pdf.set_font("DejaVu", size=12)
        for line in st.session_state['notes'].splitlines():
            safe_line = line.replace("\n", " ")
            pdf.multi_cell(180, 10, safe_line)
        pdf_bytes = pdf.output(dest='S')
        pdf_buffer = io.BytesIO(pdf_bytes)
        # Regenerate and Download buttons in a row
        col1, col2 = st.columns([1, 1])
        regenerate_clicked = col1.button("Regenerate")
        col2.download_button(
            label="Download Notes as PDF",
            data=pdf_buffer,
            file_name="notes.pdf",
            mime="application/pdf"
        )
        if regenerate_clicked:
            if topic:
                with st.spinner("Regenerating notes..."):
                    prompt = (
                        f"Generate academic detailed notes that are not too long and easy to understand about this topic: {topic}. Keep it simple."
                    )
                    response = ask_gemini(prompt)
                    if response:
                        st.session_state['notes'] = response
                    else:
                        st.error("Failed to generate notes. Please try again.")

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
