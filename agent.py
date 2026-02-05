from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:1b"

)

agent = Agent(model=ollama_model) #by default it uses AWS -Amazon Bedrock 

user_input = input("You:")
agent(user_input)
