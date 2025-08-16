import streamlit as st
import analytics

analytics.load_analytics()
st.set_page_config(
    page_title="Notexa -Learning Made Simple.",
    page_icon="assets/logo.png"
)

# --- Go Premium Button in Sidebar ---
st.sidebar.markdown('''<hr style="margin-top:2em;margin-bottom:0.5em;">''', unsafe_allow_html=True)
st.sidebar.page_link(
    "pages/_Donate.py",
    label="🙏 Donate",
    icon="💝",
    use_container_width=True
)
st.sidebar.markdown(
    '<div style="margin-top:3em; margin-bottom:1em; font-size:1.05em;">'
    '📢 <b>Turn students and teachers into customers.</b> '
    '<a href="https://your-ad-link.com" target="_blank" style="color:#00b894; font-weight:bold; text-decoration:underline;">Advertise on Notexa</a>.'
    '</div>',
    unsafe_allow_html=True
)

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
