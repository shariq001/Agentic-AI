import os
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, agent
from dotenv import load_dotenv, find_dotenv
# Imports

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")



# Step1: Provider
provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Step2: Model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider
)

# Step3: Config
run_config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled=True
)

# Step4: Agent
agent1 = Agent(
    name="Muhammad Shariq Agent",
    instructions="You are a helpful assistant"
)

# Step5: Run
result = Runner.run_sync(
    agent1,
    input="What is the capital of Pakistan?",
    run_config = run_config
)

print(result)