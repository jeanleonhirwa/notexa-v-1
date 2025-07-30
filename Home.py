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
    st.page_link(
        "pages/1_AI_Summary_&_Quiz.py",
        label="📝 AI Summary & Quiz",
        use_container_width=True,
        help="Get a quick summary and quiz for any topic you enter."
    )
    
    st.page_link(
        "pages/2_Note_summarizer.py",
        label="📚 Note Summarizer",
        use_container_width=True,
        help="Summarize your notes into easy-to-read points. (Coming soon)"
    )
    

with col2:
    st.page_link(
        "pages/3_Quiz_from_notes.py",
        label="🧪 Quiz Generator from Notes",
        use_container_width=True,
        help="Turn your notes into practice quizzes. (Coming soon)"
    )
    
    st.page_link(
        "pages/4_Revision_helper.py",
        label="📈 Smart Revision Helper",
        use_container_width=True,
        help="Get smart revision tips and reminders. (Coming soon)"
    )
    

st.markdown("---")
st.info("Notexa is designed to be simple, safe, and helpful for every student. Enjoy learning! 😊")