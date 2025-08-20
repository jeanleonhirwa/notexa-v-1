import streamlit as st
import analytics
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

analytics.load_analytics()
st.set_page_config(
    page_title="Notexa -Learning Made Simple.",
    page_icon="assets/logo.png"
)

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

def create_study_plan(subject, exam_date, confidence_level, available_hours):
    days_until_exam = (exam_date - datetime.now().date()).days
    
    prompt = f"""
    Create a detailed {days_until_exam}-day study plan for {subject} with these parameters:
    - Days until exam: {days_until_exam}
    - Current confidence level: {confidence_level}/10
    - Available study hours per day: {available_hours}

    Format the response as follows:
    ### Study Plan
    [day-by-day plan with topics, techniques, and schedules]

    ### Daily Schedule Template
    [break down of study sessions and breaks]

    ### Key Focus Areas
    [list main topics to master]

    ### Review Strategy
    [how to review previous days' content]
    """
    
    response = ask_gemini(prompt)
    if response.startswith("❌"):
        st.error(response)
        return None
    
    return response

def generate_quiz(topic):
    prompt = f"""
    Create a quick assessment quiz for: {topic}
    Include 5 multiple choice questions with explanations.
    
    Format as:
    ### Questions
    1. [Question 1]
    A) [Option A]
    B) [Option B]
    C) [Option C]
    D) [Option D]
    
    ### Answers
    1. [Correct option]: [Explanation]
    """
    
    response = ask_gemini(prompt)
    if response.startswith("❌"):
        st.error(response)
        return None
    
    return response

def generate_flashcards(topic):
    prompt = f"""
    Create 5 flashcards for {topic}.
    Format as:
    ### Flashcard 1
    Front: [key concept/question]
    Back: [explanation/answer]
    
    Continue for all 5 cards...
    """
    return ask_gemini(prompt)

def generate_mind_map(topic):
    prompt = f"""
    Create a simple mind map for {topic}.
    Format as a bulleted list with main topic in the center:
    
    • {topic}
        ◦ [Main Concept 1]
            ▪ [Sub-concept 1.1]
            ▪ [Sub-concept 1.2]
        ◦ [Main Concept 2]
            ▪ [Sub-concept 2.1]
            ▪ [Sub-concept 2.2]
    """
    return ask_gemini(prompt)

def get_learning_style_tips(learning_style):
    prompt = f"""
    Provide 5 specific study techniques for a {learning_style} learner.
    Format as:
    ### Study Techniques for {learning_style} Learners
    1. [Technique 1]
    2. [Technique 2]
    etc.
    
    Include practical examples for each technique.
    """
    return ask_gemini(prompt)

def create_pdf_summary(subject, plan, quiz):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add content
    pdf.cell(200, 10, txt=f"Study Plan: {subject}", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=plan)
    if quiz:
        pdf.add_page()
        pdf.cell(200, 10, txt="Practice Quiz", ln=True, align='C')
        pdf.multi_cell(0, 10, txt=quiz)
    
    # Return PDF as base64 string
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_base64 = base64.b64encode(pdf_output.getvalue()).decode()
    return pdf_base64

# Add custom CSS for better UI
st.markdown("""
<style>
    /* Friendly colors and rounded corners */
    .stButton button {
        border-radius: 20px;
        padding: 15px 25px;
        font-size: 16px;
    }
    
    /* Different colors for different sections */
    .study-plan-section { background: #f0f8ff; padding: 20px; border-radius: 10px; }
    .materials-section { background: #fff0f5; padding: 20px; border-radius: 10px; }
    .progress-section { background: #f0fff0; padding: 20px; border-radius: 10px; }
    
    /* Make expanders more visible */
    .streamlit-expanderHeader {
        font-size: 1.1em;
        background: #f0f2f6;
        border-radius: 10px;
    }
    
    /* Better spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Custom CSS with modern design
st.markdown(""" 
<style> 
    /* Modern color palette */ 
    :root { 
        --primary: #3498db; 
        --secondary: #2ecc71; 
        --accent: #9b59b6; 
        --background: #f8f9fa; 
        --text: #2c3e50; 
    } 

    /* Card-like sections */ 
    .stApp { 
        background-color: var(--background); 
    } 

    .css-1d391kg { 
        padding: 2rem 1rem; 
    } 

    /* Button styling */ 
    .stButton > button { 
        width: 100%; 
        border-radius: 15px; 
        padding: 0.5rem 1rem; 
        background: linear-gradient(45deg, var(--primary), var(--secondary)); 
        color: white; 
        border: none; 
        transition: transform 0.2s; 
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Section containers */
    .section-container {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }

    /* Headers */
    h1, h2, h3 {
        color: var(--text);
        font-weight: 600;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background: white;
        border-radius: 10px;
        border: 1px solid #e1e4e8;
    }

    /* Progress bars and sliders */
    .stProgress > div > div > div {
        background-color: var(--secondary);
    }

    /* Radio buttons and checkboxes */
    .stRadio > div {
        gap: 1rem;
        flex-wrap: wrap;
    }

    .stRadio label {
        background: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        border: 1px solid #e1e4e8;
        transition: all 0.2s;
    }

    .stRadio label:hover {
        border-color: var(--primary);
    }

    /* Tooltips */
    .tooltip {
        position: relative;
        display: inline-block;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        background-color: var(--text);
        color: white;
        text-align: center;
        padding: 5px 10px;
        border-radius: 6px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Adaptive color scheme using Streamlit's theme */
    :root {
        --primary: var(--primary-color);
        --text: var(--text-color);
        --background: var(--background-color);
        --secondary-bg: var(--secondary-background-color);
    }

    /* Card-like sections with theme-aware colors */
    .section-container {
        background: var(--secondary-bg);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin: 1rem 0;
        border: 1px solid rgba(128, 128, 128, 0.1);
    }

    /* Modern buttons that work in both modes */
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(var(--primary), 0.2);
    }

    /* Headers with theme-aware colors */
    h1, h2, h3 {
        color: var(--text);
        font-weight: 600;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--secondary-bg);
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.1);
    }

    /* Radio buttons and checkboxes */
    .stRadio label {
        background: var(--secondary-bg);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.1);
        transition: all 0.2s;
    }

    .stRadio label:hover {
        border-color: var(--primary);
    }

    /* Success animation with theme-aware colors */
    .success-animation circle,
    .success-animation path {
        stroke: var(--primary);
    }
</style>
""", unsafe_allow_html=True)

# Remove all previous button CSS and replace with this single block:

st.markdown("""
<style>
    /* Button styling for both light and dark modes */
    .stButton > button {
        width: 100%;
        border-radius: 15px;
        padding: 0.75rem 1.5rem;
        background: linear-gradient(45deg, var(--primary-color), #00cc88);
        border: 1px solid rgba(128, 128, 128, 0.2);
        transition: all 0.3s ease;
        font-size: 1.1em;
    }

    /* Light mode specific */
    [data-theme="light"] .stButton > button {
        color: #000000 !important;  /* Force black text in light mode */
        background: linear-gradient(45deg, var(--primary-color), #00cc88);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    /* Dark mode specific */
    [data-theme="dark"] .stButton > button {
        color: #ffffff !important;  /* Force white text in dark mode */
        background: linear-gradient(45deg, var(--primary-color), #00cc88);
        border: 1px solid rgba(250, 250, 250, 0.2);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
    }

    /* Hover effects for both modes */
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--primary-color);
        opacity: 0.9;
    }

    /* Active state for both modes */
    .stButton > button:active {
        transform: translateY(0px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("📚 Your Study Buddy")
    
    # Age Group Selection
    age_group = st.radio(
        "I am a...",
        ["Primary School Student (Ages 7-12)", 
         "Secondary School Student (Ages 13-18)",
         "University Student (Ages 18+)"],
        horizontal=True,
        help="Select your age group for personalized help"
    )
    
    st.markdown("---")
    
    # Simplified Subject Selection based on age group
    if "Primary" in age_group:
        subjects = ["Mathematics", "Science", "English", "Social Studies", "Other"]
        helper_text = "What subject do you want help with? 😊"
    elif "Secondary" in age_group:
        subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography", 
                   "Literature", "Other"]
        helper_text = "Which subject are you studying? 📚"
    else:
        subjects = ["Other"]
        helper_text = "What course are you studying? 🎓"
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if "Other" in subjects:
            subject = st.text_input(helper_text)
        else:
            subject = st.selectbox(helper_text, subjects)
    
    with col2:
        exam_date = st.date_input(
            "When is your test/exam? 📅",
            min_value=datetime.now().date(),
            help="Select the date of your exam"
        )
    
    # Simplified Learning Profile
    st.markdown("### 📋 Your Learning Profile")
    col3, col4 = st.columns(2)
    
    with col3:
        confidence = st.select_slider(
            "How well do you know this subject?",
            options=["Not at all", "A little bit", "Somewhat", "Quite well", "Very well"],
            value="Somewhat",
            help="This helps us make a better plan for you"
        )
        
        # Convert text confidence to number
        confidence_map = {
            "Not at all": 2, "A little bit": 4, "Somewhat": 6,
            "Quite well": 8, "Very well": 10
        }
        confidence_num = confidence_map[confidence]
    
    with col4:
        if "Primary" in age_group:
            hours_options = [0.5, 1, 1.5, 2]
            default_hours = 1
        else:
            hours_options = [1, 2, 3, 4, 5, 6]
            default_hours = 2
        
        study_hours = st.select_slider(
            "How many hours can you study each day?",
            options=hours_options,
            value=default_hours,
            help="Be realistic! It's better to study a little bit every day"
        )
    
    # Learning Style with icons
    st.markdown("### 🧠 How do you learn best?")
    learning_style = st.selectbox(
        "I learn best when I...",
        ["👀 See pictures and diagrams (Visual)",
         "👂 Listen and discuss (Auditory)",
         "✍️ Read and write (Reading/Writing)",
         "🤹 Do practical activities (Kinesthetic)"],
        help="This helps us suggest the best study methods for you"
    )
    learning_style = learning_style.split("(")[1][:-1]  # Extract style name
    
    # Action Buttons
    st.markdown("### 🚀 Let's Get Started!")
    col5, col6 = st.columns(2)
    
    with col5:
        if st.button("📝 Create My Study Plan", use_container_width=True):
            if subject and exam_date:
                with st.spinner("Making your perfect study plan..."):
                    plan = create_study_plan(
                        subject,
                        exam_date,
                        confidence_num,
                        study_hours
                    )
                    
                    if plan:
                        sections = plan.split("###")
                        for section in sections[1:]:  # Skip first empty section
                            title, content = section.split("\n", 1)
                            with st.expander(f"📚 {title.strip()}"):
                                st.markdown(content.strip())
                                
                                if "Key Focus Areas" in title:
                                    if st.button("Generate Practice Quiz", key="quiz"):
                                        quiz = generate_quiz(subject)
                                        if quiz:
                                            st.markdown(quiz)
                    else:
                        st.error("Failed to generate study plan. Please try again.")
            else:
                st.warning("Please enter both subject and exam date.")

    with col6:
        if st.button("🎯 Make Study Materials", use_container_width=True):
            if subject:
                with st.spinner("Creating fun study materials..."):
                    # Generate Flashcards
                    with st.expander("📑 Flashcards"):
                        flashcards = generate_flashcards(subject)
                        if flashcards:
                            st.markdown(flashcards)
                    
                    # Generate Mind Map
                    with st.expander("🗺️ Mind Map"):
                        mind_map = generate_mind_map(subject)
                        if mind_map:
                            st.markdown(mind_map)
                    
                    # Learning Style Tips
                    with st.expander(f"💡 Tips for {learning_style} Learners"):
                        tips = get_learning_style_tips(learning_style)
                        if tips:
                            st.markdown(tips)
                    
                    # Export Options
                    if st.button("📥 Export Study Materials"):
                        pdf_data = create_pdf_summary(
                            subject,
                            mind_map,
                            generate_quiz(subject)
                        )
                        href = f'<a href="data:application/pdf;base64,{pdf_data}" download="study_plan.pdf">Download PDF</a>'
                        st.markdown(href, unsafe_allow_html=True)
            else:
                st.warning("Please enter a subject first.")

    # Progress Tracking (simplified for younger students)
    if subject:
        st.markdown("---")
        st.markdown("### 🌟 Track Your Progress")
        
        mood = st.select_slider(
            "How do you feel about your studying today?",
            options=["😟", "😐", "🙂", "😊", "🤩"],
            value="🙂"
        )
        
        if "Primary" in age_group:
            hours_studied = st.select_slider(
                "How long did you study today?",
                options=["30 minutes", "1 hour", "1.5 hours", "2 hours"],
                value="1 hour"
            )
        else:
            hours_studied = st.number_input(
                "Hours studied today",
                0.0, 24.0, 0.0, 0.5
            )
        
        if st.button("Save My Progress", use_container_width=True):
            st.success("Progress saved! Keep up the good work!")
            
            # Show progress visualization
            progress_data = {
                'Initial Confidence': confidence_num,
                'Current Confidence': confidence_num  # Assuming no change for simplification
            }
            fig, ax = plt.subplots()
            ax.bar(progress_data.keys(), progress_data.values())
            ax.set_ylim(0, 10)
            st.pyplot(fig)

if __name__ == "__main__":
    main()
