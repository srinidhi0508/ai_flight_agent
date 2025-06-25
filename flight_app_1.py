import streamlit as st
import google.generativeai as genai

# 🔐 Configure Gemini API key
genai.configure(api_key="GEMINI_API_KEY")

# 🧠 Load the model
model = genai.GenerativeModel("models/gemini-1.5-flash-8b-latest")

def ask_gemini(source, destination, date):
    prompt = f"""
    You are a helpful travel assistant.

    A user wants to travel from {source} to {destination} on {date}.
    Provide 3 made-up but realistic flight options. For each flight, include:
    - Airline name
    - Departure time
    - Arrival time
    - Duration

    Format the output in bullet points and make it easy to read.
    Don't mention that this is fictional or that you don't have real-time access.
    """
    response = model.generate_content(prompt)
    return response.text

# 🎨 Streamlit UI
st.set_page_config(page_title="Flight Booking AI", page_icon="✈️")
st.title("✈️ Flight Booking Assistant")

source = st.text_input("Enter source city")
destination = st.text_input("Enter destination city")
date = st.date_input("Enter travel date")

if st.button("Search Flights"):
    if source and destination and date:
        with st.spinner("Searching for flights..."):
            result = ask_gemini(source, destination, str(date))
        st.success("Here are your flight options:")
        st.markdown(result)
    else:
        st.error("Please fill all the fields.")