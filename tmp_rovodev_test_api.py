#!/usr/bin/env python3
"""
Test script to verify the Gemini API fixes work properly
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gemini_api import generate_summary_and_quiz, generate_detailed_notes, summarize_notes, generate_quiz_from_notes

def test_api():
    print("Testing Gemini API integration...")
    
    # Test 1: Simple summary and quiz
    print("\n1. Testing summary and quiz generation...")
    result = generate_summary_and_quiz("Python programming basics")
    if result.startswith("❌"):
        print(f"ERROR: {result}")
        return False
    else:
        print("✅ Success! Generated summary and quiz")
        print(f"Preview: {result[:100]}...")
    
    # Test 2: Note generation
    print("\n2. Testing note generation...")
    result = generate_detailed_notes("Machine learning fundamentals")
    if result.startswith("❌"):
        print(f"ERROR: {result}")
        return False
    else:
        print("✅ Success! Generated detailed notes")
        print(f"Preview: {result[:100]}...")
    
    print("\n✅ All tests passed! The API integration is working correctly.")
    print("\nKey improvements made:")
    print("- ✅ Unified API key usage from .env file")
    print("- ✅ Switched to gemini-2.5-flash for better rate limits")
    print("- ✅ Added exponential backoff for rate limit handling")
    print("- ✅ Centralized error handling")
    print("- ✅ Removed hardcoded API keys")
    
    return True

if __name__ == "__main__":
    test_api()