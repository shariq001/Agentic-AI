import chainlit as cl
import os
from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv, find_dotenv
# Imports

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Step1: Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
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

@cl.on_message
async def handle_message(message: cl.Message):

    result = await Runner.run(
        agent1,
        input = message.content,
        run_config= run_config
    )


    await cl.Message(content=result.final_output).send()







