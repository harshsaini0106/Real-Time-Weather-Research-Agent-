import requests
import os 
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

from langchain_community.tools import DuckDuckGoSearchRun

API_KEY = os.getenv("WEATHER_API_KEY")



search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
                                                          
  response = requests.get(url)

  data=response.json()
  if "error" in data:
        return f"Weather API Error: {data['error']['message']}"
  
  return f"""
    City: {data['location']['name']}
    Country: {data['location']['country']}
    Temperature: {data['current']['temp_c']}°C
    Condition: {data['current']['condition']['text']}
    Humidity: {data['current']['humidity']}%
    Wind: {data['current']['wind_kph']} kph
    """


model=ChatHuggingFace(llm=llm)

agent = create_react_agent(
    model=model,
    tools=[search_tool, get_weather_data]
)

response = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Find the capital of Tamil Nadu, then find its current weather condition"
            )
        ]
    }
)


print(response["messages"][-1].content)