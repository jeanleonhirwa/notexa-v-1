import streamlit as st

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
        ⭐ Go premium
    </a>
''', unsafe_allow_html=True)

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
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/1_AI_Summary_&_Quiz.py",
        label="📝 AI Summary & Quiz",
        use_container_width=True,
        help="Get a quick summary and quiz for any topic you enter."
    )
    st.page_link(
        "pages/2_Note_generator.py",
        label="📑 Note Generator",
        use_container_width=True,
        help="Get detailed notes on any topic you enter. (Coming soon)"
    )
    
    

with col2:
    st.page_link(
        "pages/3_Note_summarizer.py",
        label="📚 Note Summarizer",
        use_container_width=True,
        help="Summarize your notes into easy-to-read points. (Coming soon)"
    )
    st.page_link(
        "pages/4_Quiz_from_notes.py",
        label="🧪 Quiz Generator from Notes",
        use_container_width=True,
        help="Turn your notes into practice quizzes."
    )
    
    
with col3:
    st.page_link(
        "pages/5_Revision_helper.py",
        label="📈 Smart Revision Helper",
        use_container_width=True,
        help="Get smart revision tips and reminders. (Coming soon)"
    )

st.markdown("---")
st.info("Notexa is designed to be simple, safe, and helpful for every student. Enjoy learning! 😊")
st.markdown("<p style='text-align: center;'>&copy; 2025. Made with ❤️ by the Hirwa Leon</p>", unsafe_allow_html=True)
