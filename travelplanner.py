import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Initialize Output Parser
parser = StrOutputParser()

# Define Prompt Template
chat_template = ChatPromptTemplate(
    messages=[
        (
            "system",
            """ You are an expert Travel Planner.
                Assist users in finding optimal travel options between a given source and destination by the user.
                Generate various travel choices (Bike, car, train, bus, flight, Ship) along with their estimated costs.
                Give costs of different options available for each travel choice.
                Only show the travel choices which are available from source to destination.
                Also give the recommended mode of travel choice.
                Output should be clear and understandable by any user.
            """
        ),
        ("human", "Provide the cost estimation for traveling from {source} to {destination} considering {preference}."),
    ]
)

# Initialize Gemini AI Model-LOGIC2
chat_model = ChatGoogleGenerativeAI(api_key=st.secrets["api_key"], model="gemini-2.0-flash-exp")

# Chain Components
chain = chat_template | chat_model | parser

# Streamlit UI
st.title("AI Travel Planner")
st.write("Enter your source and destination..")

# User Inputs
source = st.text_input("Source City", "")
destination = st.text_input("Destination City", "")
preference = st.selectbox(
    "Select Your Travel Preference:",
    ["Cheapest", "Fastest", "Most Comfortable", "Eco-friendly", "Balanced"]
)


# Button to Fetch Cost Estimates
if st.button("Get Cost Estimate"):
    if source and destination:
        raw_ip = {"source": source, "destination": destination,"preference": preference}
        with st.spinner("Fetching estimated costs"):
            try:
                # Get Response
                response = chain.invoke(raw_ip)
                st.subheader(f"The estimated transportation cost from {source} to {destination}:")
                # Display String Response
                st.write(response)
            except Exception as e:
                st.error(f"Error fetching data: {e}")
    else:

        st.warning("Please enter both source and destination.")
