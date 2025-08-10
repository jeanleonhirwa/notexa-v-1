import streamlit as st

st.set_page_config(page_title="Notexa v1 - Futuristic Landing", layout="centered", page_icon="🧠")

# Futuristic Glassmorphism & Gradient CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #0f2027 0%, #2c5364 100%);
        }
        .block-container {
            padding-top: 2.5rem;
            padding-bottom: 2.5rem;
            max-width: 700px;
        }
        .glass {
            background: rgba(255,255,255,0.10);
            border-radius: 22px;
            box-shadow: 0 8px 32px 0 rgba(31,38,135,0.37);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.18);
            padding: 1.25rem 1rem 1rem 1rem;
            margin-top: 0.3rem;
        }
        .center {
            text-align: center;
        }
        .headline {
            font-size: 2.3rem;
            font-weight: 800;
            letter-spacing: 0.03em;
            background: linear-gradient(90deg, #4CAF50 20%, #00e6e6 80%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .tagline {
            font-size: 1.2rem;
            color: #e0e0e0;
            margin-bottom: 1.2rem;
        }
        .feature-list {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .feature {
            background: rgba(255,255,255,0.13);
            border-radius: 14px;
            padding: 1.1rem 1rem;
            margin: 0 0.5rem;
            min-width: 120px;
            box-shadow: 0 2px 8px 0 rgba(31,38,135,0.10);
        }
        .feature-icon {
            font-size: 2.1rem;
            margin-bottom: 0.3rem;
        }
        .cta-btn {
            background: linear-gradient(90deg, #4CAF50 40%, #00e6e6 100%);
            color: #fff;
            font-weight: bold;
            font-size: 1.1rem;
            border: none;
            border-radius: 12px;
            padding: 0.8rem 2.2rem;
            margin-top: 1.2rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 2px 8px 0 rgba(31,38,135,0.10);
            cursor: pointer;
        }
        .cta-btn:hover {
            filter: brightness(1.1);
        }
        .quote {
            font-size: 1.1rem;
            color: #b2fefa;
            margin-top: 2rem;
            font-style: italic;
        }
        @media (max-width: 700px) {
            .feature-list {
                flex-direction: column;
                align-items: center;
            }
            .feature {
                margin: 0.5rem 0;
                width: 90%;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='glass'><h4 align='center'>👋 Welcome to Notexa</h4></div>", unsafe_allow_html=True)

st.image("assets/logo.png", width=90)
st.markdown("<div class='center headline'>Notexa v1</div>", unsafe_allow_html=True)
st.markdown("<div class='center tagline'>The future of smart learning is here. <br>Summarize, quiz, and master knowledge with AI.</div>", unsafe_allow_html=True)

st.markdown("""
<div class='feature-list'>
    <div class='feature center'>
        <div class='feature-icon'>📄</div>
        <div><b>Instant Summaries</b><br><span style='font-size:0.95rem;'>Turn notes into concise insights.</span></div>
    </div>
    <div class='feature center'>
        <div class='feature-icon'>🧠</div>
        <div><b>Quiz Generator</b><br><span style='font-size:0.95rem;'>Create custom quizzes in seconds.</span></div>
    </div>
    <div class='feature center'>
        <div class='feature-icon'>⏳</div>
        <div><b>Save Time</b><br><span style='font-size:0.95rem;'>Accelerate your revision process.</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='center'>", unsafe_allow_html=True)
if st.button("🚀 Get Started with Notexa", key="get_started", help="Go to Login or App", use_container_width=True):
    st.switch_page("users/login.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class='center quote'>
    "The future belongs to those who prepare for it today."<br>
    <span style='font-size:1rem;margin-top:-500px;'>— Malcolm X</span>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
