import streamlit as st
import requests
import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

search_tool = DuckDuckGoSearchRun()


@tool
def get_weather_data(city: str) -> str:
    """
    Fetches current weather data for a given city.
    """
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return f"Weather API Error: {data['error']['message']}"

    return f"""
City: {data['location']['name']}
Country: {data['location']['country']}
Temperature: {data['current']['temp_c']}°C
Condition: {data['current']['condition']['text']}
Humidity: {data['current']['humidity']}%
Wind Speed: {data['current']['wind_kph']} kph
"""


model = ChatHuggingFace(llm=llm)

agent = create_react_agent(
    model=model,
    tools=[search_tool, get_weather_data]
)

st.set_page_config(
    page_title="Weather Research Agent",
    page_icon=" "
)

st.title("Weather Research Agent")
st.write("Ask any weather-related question.")

query = st.text_input(
    "Enter your query:",
    placeholder="Search Real time Weather of state you want"
)

if st.button("Run Agent"):
    if query:
        with st.spinner("Thinking..."):
            response = agent.invoke(
                {
                    "messages": [
                        HumanMessage(content=query)
                    ]
                }
            )

            st.success("Response Generated")
            st.write(response["messages"][-1].content)