from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:1b"

)

system_prompt = "You are respectful agent. " \
"you give answers in a kind and humble way" \
"you can use correct data sources to give outputs."

agent = Agent(model=ollama_model, system_prompt=system_prompt) #by default it uses AWS -Amazon Bedrock 

user_input = input("You:")
agent(user_input)


