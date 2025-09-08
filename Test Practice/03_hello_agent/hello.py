import os
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Step1: Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider,
)

set_tracing_disabled(disabled=True)

agent = Agent(
    name = "Assistant",
    instructions = "You only respond in haikus.",
    model = model
)

async def main():
    result = await Runner.run(
        agent,
        "Tell me recursion in programming"
    )
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())