import streamlit as st
import pandas as pd

# Initialize session state to track user inputs
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0

def save_response(question, response):
    st.session_state.responses[question] = response
    st.session_state.current_question_index += 1

def save_to_csv(responses):
    df = pd.DataFrame([responses])
    try:
        # Append to existing CSV if it exists
        df.to_csv("intake_responses.csv", mode="a", header=False, index=False)
    except FileNotFoundError:
        # Create a new CSV with headers if it doesn't exist
        df.to_csv("intake_responses.csv", mode="w", header=True, index=False)

# Intake form questions
questions = [
    ("What's your first name?", "text"),
    ("And your last name?", "text"),
    ("How did you hear about us?", "text"),
    ("What's your date of birth? (MM/DD/YYYY)", "text"),
    ("Is this appointment for a minor child?", "radio", ["Yes", "No"]),
    ("What is your sex assigned at birth?", "radio", ["Male", "Female", "Other"]),
    ("If you'd like, you can share your gender identity (optional).", "text"),
    ("Please enter your street address.", "text"),
    ("Is there an additional line for your address (like apartment number)?", "text"),
    ("What city do you live in?", "text"),
    ("What state?", "text"),
    ("And your zip code?", "text"),
    ("What's your email address?", "text"),
    ("Can you share your telephone number?", "text"),
    ("What brings you to us at this time? Is there something specific, like an event or situation?", "text"),
    ("Tell us more about the type of mental health care you are seeking.", "text"),
    ("Have you seen a mental health professional before?", "radio", ["Yes", "No"]),
    ("Do you have any medication allergies?", "text"),
    ("Do you have current thoughts of self-harm or harming others?", "radio", ["Yes", "No"])
]

st.title("Intake Form Chatbot")
st.write("Hi there! Let's get started with your intake process. I'll ask you some questions to ensure we can provide you with the best care possible.")

# Fetch the current question
current_index = st.session_state.current_question_index

if current_index < len(questions):
    question, input_type, *options = questions[current_index]

    # Display the current question based on its type
    if input_type == "text":
        response = st.text_input(question)
    elif input_type == "radio":
        response = st.radio(question, options[0])

    # Add a submit button to move to the next question
    if st.button("Submit"):
        if response:  # Ensure the user provides an answer
            save_response(question, response)
else:
    st.success("Thank you! Your intake form is complete.")
    st.write("Here is the information you provided:")
    for key, value in st.session_state.responses.items():
        st.write(f"**{key}**: {value}")

    # Save the responses to a CSV file
    save_to_csv(st.session_state.responses)
    st.write("Your responses have been saved successfully!")
