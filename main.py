import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider
)

agents = Agent(
    name = "Greeting Agents",
    instructions= '''
    You are a helpful and friendly greeting agent.
    Your job is to welcome users in a warm and polite manner.
    Start every conversation with a cheerful greeting based on the time of day (morning, afternoon, evening).
    Ask the user how you can assist them after greeting.
    Keep your tone positive and respectful at all times.
    If the user provides their name, greet them using their name in future responses.
    ''',
    model = model
)

questions = input("Plz Enter Your Questions : ")
result = Runner.run_sync(agents,questions)
print(result.final_output)