import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig
from dotenv import load_dotenv, find_dotenv
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl
from agents.tool import function_tool

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Step1: Provider
provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Step2: Model
model = OpenAIChatCompletionsModel(
    model = "gemini-1.5-flash",
    openai_client=provider
)

# Step3: Run Config
run_config = RunConfig(
    model = model,
    model_provider= provider,
    tracing_disabled=True
)

@function_tool("get_weather")
def get_weather(location: str) -> str:
    return f"The weather in {location} is 22 degrees C."


# Step4: Agent
agent = Agent(
    name = "Muhammad Shariq Agent",
    instructions="You are a tool calling agent. Use get_weather tool to share get temperature for any location",
    tools=[get_weather]
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])

    await cl.Message(content="Hello from Muhammad Shariq tool calling agent! How can I help you today?").send()


@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role": "user", "content": message.content})

    result = Runner.run_streamed(
        agent,
        input = history,
        run_config= run_config
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            
            await msg.stream_token(event.data.delta)

    
    history.append({"role": "assistant", "content": result.final_output})

    cl.user_session.set("history", history)