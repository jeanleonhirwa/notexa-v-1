"""
Shared Gemini API utilities for Notexa
Handles rate limiting, retries, and consistent error handling
"""
import requests
import os
import time
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

def call_gemini_api(prompt, model="gemini-2.5-flash", max_retries=3):
    """
    Call Gemini API with rate limiting and retry logic
    
    Args:
        prompt (str): The prompt to send to Gemini
        model (str): The model to use (default: gemini-2.5-flash for better rate limits)
        max_retries (int): Maximum number of retry attempts
    
    Returns:
        str: The response from Gemini or error message
    """
    if not API_KEY:
        return "❌ API key not found. Please check your .env file."
    
    url = f"https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            # Extract the response text
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                content = result['candidates'][0].get('content', {})
                parts = content.get('parts', [])
                if parts and 'text' in parts[0]:
                    return parts[0]['text']
            
            return "❌ No valid response received from Gemini."
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Rate limit exceeded
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) * 3  # Exponential backoff: 3, 6, 12 seconds
                    st.warning(f"Rate limit reached. Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                    continue
                else:
                    return "❌ Rate limit exceeded. Please wait a few minutes and try again. Consider upgrading your API quota."
            elif response.status_code == 403:
                return "❌ API key invalid or quota exceeded. Please check your Gemini API key and billing."
            else:
                return f"❌ Gemini API error: HTTP {response.status_code} - {e}"
                
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                st.warning(f"Request timeout. Retrying... (attempt {attempt + 1})")
                continue
            else:
                return "❌ Request timeout. Please try again."
                
        except requests.exceptions.ConnectionError:
            if attempt < max_retries - 1:
                st.warning(f"Connection error. Retrying... (attempt {attempt + 1})")
                time.sleep(2)
                continue
            else:
                return "❌ Connection error. Please check your internet connection."
                
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"
    
    return "❌ Failed after all retry attempts."

# Specific functions for different use cases
def generate_summary_and_quiz(topic):
    """Generate summary and quiz for a topic"""
    prompt = (
        f"Give a short and clear summary about this topic: {topic}. "
        "Then generate 3 quiz questions with answers based on that topic."
    )
    return call_gemini_api(prompt)

def generate_detailed_notes(topic):
    """Generate detailed notes for a topic"""
    prompt = (
        f"Generate academic detailed notes that are not too long and easy to understand about this topic: {topic}. Keep it simple."
    )
    return call_gemini_api(prompt)

def summarize_notes(text):
    """Summarize academic notes"""
    prompt = (
        "Summarize the following all academic notes in simple, clear English that is easy to understand:\n\n"
        f"{text}\n\nSummary:"
    )
    return call_gemini_api(prompt)

def generate_quiz_from_notes(text):
    """Generate quiz from notes"""
    prompt = (
        "Generate academic quiz from this academic notes, Quiz should have 3 sections, "
        "section A(must include 8 multiple choice questions), "
        "section B(must include 4 questions, 2 of True or False and 2 questions of Fill in blanks) "
        "and Section C(must include 2 open-ended questions):\n\n"
        f"{text}\n\nQuiz:"
    )
    return call_gemini_api(prompt)