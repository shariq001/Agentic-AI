import chainlit as cl
# Importing chainlit

@cl.on_message
async def main(message: cl.Message):

    await cl.Message(
        content=f"Received: {message.content}",
    ).send()