import streamlit as st

# --- Language Switcher ---
lang = st.selectbox(
    "🌐 Language / Ururimi / Langue",
    ("English", "Kinyarwanda", "French"),
    index=0,
    help="Choose your language"
)

# --- Welcome ---
st.title("👋 Welcome to Notexa!")
st.markdown(
    "#### Your friendly AI-powered study assistant for students of all ages.\n"
    "Pick a tool below to get started:"
)

# --- Tool Cards ---
st.markdown("### 🛠️ Tools")
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/notexa_app.py", label="📝 AI Summary & Quiz", use_container_width=True)
    st.page_link("pages/note_summarizer.py", label="📚 Note Summarizer", use_container_width=True)

with col2:
    st.page_link("pages/quiz_from_notes.py", label="🧪 Quiz Generator from Notes", use_container_width=True)
    st.page_link("pages/revision_helper.py", label="📈 Smart Revision Helper", use_container_width=True)

st.markdown("---")
st.info("Notexa is designed to be simple, safe, and helpful for every student. Enjoy learning! 😊")