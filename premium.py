import streamlit as st

st.set_page_config(page_title="Notexa Premium", page_icon="⭐", layout="centered")

st.markdown("""
    <style>
    # body, .stApp {
    #     background: linear-gradient(120deg, #f8fbff 0%, #e0e7ff 100%) !important;
    # }
    .premium-cards-row {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: stretch;
        gap: 2.5em;
        margin: 2.5em 0 2em 0;
        flex-wrap: nowrap;
        width: 100%;
        max-width: 1400px;
        margin-left: auto;
        margin-right: auto;
    }
    .premium-card {
        background: rgba(255,255,255,0.85);
        border-radius: 1.7em;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.10);
        padding: 2.7em 2em 2.2em 2em;
        min-width: 320px;
        max-width: 400px;
        width: 100%;
        min-height: 520px;
        border: 1.5px solid rgba(200,200,255,0.18);
        backdrop-filter: blur(8px);
        transition: box-shadow 0.2s, transform 0.2s, border 0.2s;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: stretch;
        position: relative;
    }
    .premium-card-center {
        background: linear-gradient(120deg, #e0eaff 0%, #b3d8ff 100%);
        box-shadow: 0 12px 48px 0 rgba(25, 118, 210, 0.18), 0 0 0 4px #1976d233;
        border: 2.5px solid #1976d2;
        z-index: 2;
        min-height: 560px;
        max-width: 440px;
        transform: scale(1.07);
    }
    .premium-card:hover, .premium-card-center:hover {
        box-shadow: 0 16px 48px 0 rgba(31, 38, 135, 0.18);
        transform: translateY(-6px) scale(1.03);
        border: 2.5px solid #1976d2;
    }
    .badge-popular {
        position: absolute;
        top: -22px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(90deg, #1976d2 0%, #00c6fb 100%);
        color: #fff;
        font-size: 1.05em;
        font-weight: 700;
        padding: 0.4em 1.5em;
        border-radius: 1.2em;
        box-shadow: 0 2px 8px rgba(25, 118, 210, 0.10);
        letter-spacing: 0.5px;
        border: 2px solid #fff;
        z-index: 3;
    }
    .plan-price {
        text-align:center; font-size:2em; font-weight:800; margin-bottom:0.3em; letter-spacing: -1px;
    }
    .plan-desc {
        color: #555; font-size: 1.08em; text-align:center; margin-bottom:1.2em;
    }
    .plan-list {
        list-style:none; padding-left:0; font-size:1.15em; margin-bottom:0.5em;
    }
    .plan-list li { margin-bottom: 0.5em; }
    .premium-btn {
        background: linear-gradient(90deg, #1976d2 0%, #00c6fb 100%);
        color: #fff;
        border: none;
        border-radius: 2em;
        padding: 0.9em 2.4em;
        font-weight: 700;
        font-size: 1.18em;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(25, 118, 210, 0.10);
        margin-top: 2.2em;
        transition: background 0.2s, box-shadow 0.2s;
    }
    .premium-btn:hover {
        background: linear-gradient(90deg, #00c6fb 0%, #1976d2 100%);
        box-shadow: 0 4px 16px rgba(25, 118, 210, 0.18);
    }
    .gold-btn {
        background: linear-gradient(90deg, #FFD700 0%, #FFB300 100%);
        color: #222;
    }
    .gold-btn:hover {
        background: linear-gradient(90deg, #FFB300 0%, #FFD700 100%);
    }
    .free-btn {
        background: #e0e0e0;
        color: #333;
    }
    .free-btn:hover {
        background: #f5f5f5;
    }
    @media (max-width: 1200px) {
        .premium-cards-row {
            flex-direction: column;
            align-items: center;
            gap: 2.5em;
        }
        .premium-card, .premium-card-center {
            max-width: 95vw;
            min-width: 0;
            transform: none !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-bottom:2.5em;'>
    <span style='font-size:2.3em; font-weight:900; letter-spacing:-1px; background: linear-gradient(90deg,#1976d2,#00c6fb); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Go Premium</span>
    <br>
    <span style='font-size:1.18em; color:#444; font-weight:500;'>Unlock your full learning potential. Choose your plan.</span>
</div>
<hr style="border: none; border-top: 2px solid #e0e7ff; margin-bottom: 2.5em; margin-top: 0.5em;">
""", unsafe_allow_html=True)

st.markdown("""
<div class="premium-cards-row">
    <div class='premium-card'>
        <h3 style='text-align:center; margin-bottom:0.7em;'>Free</h3>
        <div class='plan-price' style='color:#1976d2;'>0 RWF</div>
        <div class='plan-desc'>Start for free, no card required</div>
        <ul class='plan-list'>
            <li>📝 3 AI summary & quiz / day</li>
            <li>📑 3 Notes generator / day</li>
            <li>📚 3 Note summarizer / day</li>
            <li>📈 1 Revision helper / day</li>
        </ul>
        <div style='text-align:center; margin-top:auto;'>
            <button class='premium-btn free-btn'>Continue</button>
        </div>
    </div>
    <div class='premium-card premium-card-center'>
        <div class='badge-popular'>Most Popular</div>
        <h3 style='text-align:center; margin-bottom:0.7em;'>🔹 Premium</h3>
        <div class='plan-price' style='color:#1976d2;'>1,500 RWF</div>
        <div class='plan-desc'>(~$1.04) / month</div>
        <ul class='plan-list'>
            <li>🔓 1 Month Premium Access</li>
            <li>✅ Unlimited AI summaries</li>
            <li>✅ Quiz from your notes</li>
            <li>✅ Notes generator from topics</li>
            <li>✅ Smart revision support</li>
        </ul>
        <div style='text-align:center; margin-top:auto;'>
            <button class='premium-btn'>Start</button>
        </div>
    </div>
    <div class='premium-card' style='background:linear-gradient(120deg, #fffbe0 0%, #ffe6b3 100%);'>
        <h3 style='text-align:center; margin-bottom:0.7em;'>3-Month Plan</h3>
        <div class='plan-price' style='color:#ffb300;'>3,500 RWF</div>
        <div class='plan-desc'>(~$2.43) / 3 months</div>
        <ul class='plan-list'>
            <li>🔓 3 Months Premium Access <span style='color:#388e3c;'>(save 1,000 RWF!)</span></li>
            <li>✅ Unlimited summaries, quizzes, and smart tools</li>
            <li>🎓 Perfect for exams and long-term revision</li>
        </ul>
        <div style='text-align:center; margin-top:auto;'>
            <button class='premium-btn gold-btn'>Start</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Questions? Contact us at support@notexa.com or use the in-app help.")