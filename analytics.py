import streamlit as st

def load_analytics():
    GA_ID = "G-5TVTCD9932"  # replace with your Measurement ID
    GA_SCRIPT = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
    </script>
    """
    st.markdown(GA_SCRIPT, unsafe_allow_html=True)
