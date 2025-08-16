import streamlit as st

import analytics

analytics.load_analytics()
st.set_page_config(
    page_title="Notexa -Learning Made Simple.",
    page_icon="assets/logo.png"
)
# Hide sidebar using custom CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("Support Notexa 💖")
st.markdown("""
Thank you for considering a donation! Your support helps us keep improving Notexa and making learning easier for everyone.

**MTN MOMO Code:**  
`1783972`

**PayPal:**  
[Donate via PayPal](https://www.paypal.com/donate?hosted_button_id=YOUR_BUTTON_ID)

---

> *"The smallest act of kindness is worth more than the grandest intention."*  
> *"Your support fuels our mission to empower learners everywhere!"*

Every contribution, big or small, makes a difference. Thank you!
""", unsafe_allow_html=True)

# Add back button
if st.button("⬅️ Back to Notexa"):
    st.switch_page("Home.py")  # This works ONLY if you started with streamlit run Home.py