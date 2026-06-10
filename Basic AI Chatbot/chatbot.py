from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

print("Choose your AI mode")
print("Press 1 for Angry mode")
print("Press 2 for Funny mode")
print("Press 3 for Sad mode")

choice = int(input("Tell your response: "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."

elif choice == 3:
    mode = "You are a sad AI agent. You respond sadly and emotionally."

else:
    mode = "You are a helpful AI agent."

messages = [
    SystemMessage(content=mode)
]

print("\n-------- Welcome (Type 0 to Exit) --------\n")

while True:

    prompt = input("You: ")

    if prompt == "0":
        break

    messages.append(
        HumanMessage(content=prompt)
    )

    response = model.invoke(messages)

    messages.append(
        AIMessage(content=response.content)
    )

    print("Bot:", response.content)