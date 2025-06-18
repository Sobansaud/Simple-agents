import os
from agents import Agent , Runner , AsyncOpenAI , OpenAIChatCompletionsModel
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = client
)

agent1 = Agent(
    name="Full Stack Developer",
    instructions="You are a full stack developer. You only answer coding questions.",
    model=model
)

agent2 = Agent(
    name="General Assistant",
    instructions="You handle general questions not related to coding.",
    model=model
)

def decide(user_question):
    if "code" in user_question.lower() or "python" in user_question.lower() or "html" in user_question.lower() or "css" in user_question.lower() in "full stack":
        return agent1
    else:
        return agent2
    
user_input = input("What is your Questions : ")
selected = decide(user_input)
result = Runner.run_sync(selected , user_input)
print(f"Agent {selected.name} says: {result.final_output}")

