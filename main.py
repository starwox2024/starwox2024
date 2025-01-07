import streamlit as st

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0

# Steps as functions
def personal_information():
    st.write("Hi there! Let’s get started with your intake process. I’ll ask you some questions to ensure we can provide you with the best care possible. Let’s begin!")
    st.text_input("What’s your first name?", key="first_name")
    st.text_input("And your last name?", key="last_name")
    st.text_input("How did you hear about us?", key="referral")
    st.date_input("What’s your date of birth? (MM/DD/YYYY)", key="dob")
    is_minor = st.radio("Is this appointment for a minor child?", ["Yes", "No"], key="is_minor")
    if is_minor == "Yes":
        st.text_input("Please provide your name.", key="guardian_name")
        st.text_input("What is your relationship to the child?", key="relationship")
        st.radio("Do you consent to your child receiving care, including potential prescriptions if necessary?", ["Yes", "No"], key="consent")
        st.text_input("Type your full name as your signature to confirm.", key="guardian_signature")

def contact_information():
    st.radio("What is your sex assigned at birth?", ["Male", "Female", "Other"], key="birth_sex")
    st.text_input("If you’d like, share your gender identity (optional).", key="gender_identity")
    st.text_input("Please enter your street address.", key="street_address")
    st.text_input("Is there an additional line for your address?", key="address_line2")
    st.text_input("What city do you live in?", key="city")
    st.text_input("What state?", key="state")
    st.text_input("And your zip code?", key="zip")
    st.text_input("What’s your email address?", key="email")
    st.text_input("Can you share your telephone number?", key="phone_number")

def visit_expectations():
    st.text_input("What brings you to us at this time? Is there something specific, like an event or situation?", key="reason_for_visit")
    st.text_input("Tell us more about the type of mental health care you are seeking.", key="mental_health_care")
    st.radio("Have you seen a mental health professional before?", ["Yes", "No"], key="seen_therapist")
    st.text_area("Have you been diagnosed or experienced any conditions? (List them)", key="conditions")
    st.radio("In the last six months, have you had frequent, intrusive thoughts or urges?", ["Yes", "No"], key="intrusive_thoughts")
    st.radio("Do you do repetitive behaviors like handwashing or reassurance-seeking?", ["Yes", "No"], key="repetitive_behaviors")
    st.radio("Over the last month, have these thoughts or behaviors significantly impacted your life?", ["Yes", "No"], key="impact")

def medical_history():
    st.text_area("List any medications or supplements you are currently taking, along with their purposes.", key="medications")
    st.text_input("If applicable, who is your prescribing doctor? (Include their name and contact information)", key="prescribing_doctor")
    st.text_area("Do you have any medication allergies?", key="medication_allergies")
    st.text_input("Do you drink alcohol? If yes, how much and how often?", key="alcohol")
    st.text_input("Do you use recreational drugs? If yes, what kind and how often?", key="recreational_drugs")
    st.radio("Do you have current thoughts of self-harm or harming others?", ["Yes", "No"], key="self_harm")
    if st.session_state.self_harm == "Yes":
        st.text_area("Please provide more details. If this is an emergency, call 911 immediately.", key="self_harm_details")

def personal_life():
    st.text_input("What is your living situation like? Do you live alone, with family, or others?", key="living_situation")
    st.text_input("What’s your highest level of education, and what type of degree do you have?", key="education")
    st.text_input("What is your current occupation, and how long have you been doing it?", key="occupation")
    st.radio("Do you have any hearing impairments that require accommodations for sessions?", ["Yes", "No"], key="hearing_impairments")

def final_steps():
    st.write("Please click the link below to securely add your insurance and payment information:")
    st.write("[Secure Link]")
    st.write("Before we finish, review our Terms of Use and practice policies below:")
    st.write("[Link to Terms of Use and Policies]")
    st.radio("Do you agree to our Terms of Use and policies?", ["I Agree"], key="terms_agree")
    st.success("Thank you! Your intake is now complete. We look forward to supporting you!")

# Steps in sequence
steps = [
    personal_information,
    contact_information,
    visit_expectations,
    medical_history,
    personal_life,
    final_steps
]

# Render current step
if st.session_state.step < len(steps):
    steps[st.session_state.step]()  # Call current step

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.step > 0 and st.button("Previous"):
            st.session_state.step -= 1
    with col2:
        if st.session_state.step < len(steps) - 1 and st.button("Next"):
            st.session_state.step += 1
else:
    st.success("You have completed the intake process!")
