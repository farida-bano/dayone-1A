import streamlit as st

# Page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌱")

# Title and Introduction
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This is an AI-powered tool to guide you through your growth process.")

# Today's Growth Mindset Quote
st.header("Today's Growth Mindset Quote")
st.write("**“Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston Churchill**")

# User Challenge Input
st.header("What is Your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

# Conditional response to user's input
if user_input:
    st.success(f"You're facing: **{user_input}**. Keep pushing forward toward your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

# Display reflection response
if reflection:
    st.success(f"Great Insight! Your reflection: **{reflection}**")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties or lessons learned.")

# Achievement Section
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

# Conditional response to user's achievement
if achievement:
    st.success(f"Amazing! You achieved: **{achievement}**")
else:
    st.info("Big or small, every achievement counts! Share one now.")

# Footer
st.write("-" * 50)
st.write("Keep believing in yourself!")
st.write("**Created by Farida**")
