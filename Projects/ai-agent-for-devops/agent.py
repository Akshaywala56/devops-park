from strands import Agent
from strands.models.ollama import OllamaModel
from strands.tools import tool
import requests

@tool
def http_request_tool(url: str, method: str = "GET", data: dict = None) -> str:
    """Make an HTTP request to fetch data from a URL."""
    response = requests.request(method, url, json=data)
    return response.text

# agent = Agent() #create an instance of the Agent
# By default it runs amazon bedrock in the background, but you can specify a different provider if you want
# agent = Agent(provider="azure") # to use Azure OpenAI 

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="gpt-oss:120b-cloud"               # Specify which model to use
)

system_prompt = "You are respectful agent. you give answers in a kind and humble way"\
"you can use tools whenever needed and make API Calls."

# Create an agent using the Ollama model
agent = Agent(model=ollama_model,
              system_prompt=system_prompt,
              tools=[http_request_tool])

# Use the agent
user_input = input("you:")
agent_response = agent(user_input)
# agent("what is happening in between iran and isrial today")