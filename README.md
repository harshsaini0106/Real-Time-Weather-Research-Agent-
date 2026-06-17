## 🌦️ Weather Research Agent using LangGraph

An AI-powered Weather Research Agent built with **LangGraph**, **LangChain**, **Hugging Face**, **DuckDuckGo Search**, and **WeatherAPI**.

The agent can:

- Search the web for information
- Find locations and capitals
- Fetch real-time weather data
- Reason through multi-step queries using ReAct Agents

---

## Screenshot of Application

<img width="1236" height="663" alt="Screenshot 2026-06-17 161948" src="https://github.com/user-attachments/assets/8d651684-be7e-45cf-b64b-32d848ed071d" />


## 🚀 Features

- LangGraph ReAct Agent
- DuckDuckGo Search Tool
- Real-Time Weather API Integration
- Hugging Face LLM (Qwen2.5-7B-Instruct)
- Streamlit User Interface

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- Hugging Face
- Streamlit
- WeatherAPI
- DuckDuckGo Search

---

## 📂 Project Structure

```bash
weather-research-agent/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
WEATHER_API_KEY=your_weather_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd weather-research-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example Query

```text
Find the capital of Tamil Nadu, then find its current weather condition.
```

Another example:

```text
What is the capital of Japan and what is the weather there right now?
```

---

## ⚙️ How It Works

1. User enters a query.
2. LangGraph ReAct Agent analyzes the request.
3. DuckDuckGo Search finds required information.
4. Weather Tool fetches live weather data.
5. Agent combines results and generates the final answer.

---


## 👨‍💻 Author

Harsh Saini

Built using LangGraph + LangChain + Hugging Face.##
