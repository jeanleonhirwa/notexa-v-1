import streamlit as st
import analytics

analytics.load_analytics()
st.set_page_config(
    page_title="Notexa -Learning Made Simple.",
    page_icon="assets/logo.png"
)
from fpdf import FPDF
import os
import sys

# Add parent directory to path to import gemini_api
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gemini_api import generate_detailed_notes

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
                response = generate_detailed_notes(topic)
                if response:
                    st.session_state['notes'] = response
                else:
                    st.error("Failed to generate notes. Please try again.")

if st.session_state['notes']:
    st.markdown("### 📑 Generated Notes:")
    st.write(st.session_state['notes'])
    
    # Prepare PDF with built-in fonts
    import io
    pdf = FPDF()
    pdf.add_page()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    
    # Use built-in Arial font (no external files needed)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 15, "Generated Notes", ln=True, align="C")
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 12)
    
    # Process the notes text and handle special characters
    notes_text = st.session_state['notes']
    # Remove or replace problematic characters
    notes_text = notes_text.encode('latin1', errors='ignore').decode('latin1')
    
    for line in notes_text.splitlines():
        if line.strip():  # Skip empty lines
            # Split long lines to fit page width
            words = line.split()
            current_line = ""
            for word in words:
                test_line = current_line + " " + word if current_line else word
                # Approximate character limit per line (adjust based on font size)
                if len(test_line) > 80:
                    if current_line:
                        pdf.multi_cell(0, 8, current_line.strip())
                    current_line = word
                else:
                    current_line = test_line
            if current_line:
                pdf.multi_cell(0, 8, current_line.strip())
        else:
            pdf.ln(4)  # Add space for empty lines
    
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_buffer = io.BytesIO(pdf_bytes)
    
    # Regenerate and Download buttons in a row
    col1, col2 = st.columns([1, 1])
    regenerate_clicked = col1.button("Regenerate")
    col2.download_button(
        label="Download Notes as PDF",
        data=pdf_buffer.getvalue(),
        file_name="notes.pdf",
        mime="application/pdf"
    )
    
    if regenerate_clicked:
        if topic:
            with st.spinner("Regenerating notes..."):
                response = generate_detailed_notes(topic)
                if response:
                    st.session_state['notes'] = response
                else:
                    st.error("Failed to generate notes. Please try again.")

# --- Go Premium Button in Sidebar ---
st.sidebar.markdown('''<hr style="margin-top:2em;margin-bottom:0.5em;">''', unsafe_allow_html=True)
st.sidebar.markdown('''
    <a href="/donate" target="_self" style="
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
