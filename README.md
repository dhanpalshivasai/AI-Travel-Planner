# AI Travel Planner

## Overview
AI Travel Planner is a smart travel assistant that helps users find the best travel options between a given source and destination. It utilizes AI to generate various travel choices such as bike, car, train, bus, flight, and ship along with their estimated costs. Users can also choose a travel preference to get the most suitable recommendation.

## Features
- Supports multiple travel modes (Bike, Car, Train, Bus, Flight, Ship)
- Provides cost estimations for available travel options
- Recommends the best travel mode based on user preference
- Simple and interactive UI using Streamlit

## Technologies Used
- **Python**: Core programming language
- **Streamlit**: For building the interactive web application
- **LangChain**: To handle AI-driven responses
- **Google Generative AI (Gemini 2.0)**: AI model for generating travel insights

## Installation
### Prerequisites
- Python 3.x installed
- Google Generative AI API key

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-travel-planner.git
   cd ai-travel-planner
   ```
2. Install dependencies:
   ```sh
   pip install streamlit langchain-core langchain-google-genai
   ```
3. Set up your API key in the script:
   ```python
   chat_model = ChatGoogleGenerativeAI(api_key="your_api_key", model="gemini-2.0-flash-exp")
   ```
4. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Enter your **Source City** and **Destination City**.
2. Select your **Travel Preference** from options:
   - Cheapest
   - Fastest
   - Most Comfortable
   - Eco-friendly
   - Balanced
3. Click **Get Cost Estimate** to view available travel options and costs.



