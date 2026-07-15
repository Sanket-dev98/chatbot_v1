import os
import json
from groq import Groq

# ----------------------------
# API KEY
# ----------------------------
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ----------------------------
# File
# ----------------------------
CHAT_FILE = "chat.json"

# ----------------------------
# System Prompt
# ----------------------------
SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are an AI Expert.

Your job is to help users learn:
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Python
- Programming
- Data Structures
- Web Development

Always explain concepts in a beginner-friendly way.

If code is requested,
give clean and well-commented code.

If user asks non-AI questions,
still answer politely.
"""
}

# ----------------------------
# Load Conversation
# ----------------------------
def load_chat():

    if os.path.exists(CHAT_FILE):

        with open(CHAT_FILE, "r") as file:
            messages = json.load(file)

    else:
        messages = [SYSTEM_PROMPT]

    return messages


# ----------------------------
# Save Conversation
# ----------------------------
def save_chat(messages):

    with open(CHAT_FILE, "w") as file:
        json.dump(messages, file, indent=4)


# ----------------------------
# Load old chat
# ----------------------------
messages = load_chat()

print("AI Chatbot")
print("Type 'exit' to quit.\n")

# ----------------------------
# Chat Loop
# ----------------------------
while True:

    user = input("You : ")

    if user.lower() == "exit":
        save_chat(messages)
        print("Conversation Saved.")
        break

    # Save user message
    messages.append({
        "role": "user",
        "content": user
    })

    # API Call
    chat = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=messages
    )

    answer = chat.choices[0].message.content

    print("\nAI :", answer, "\n")

    # Save AI message
    messages.append({

        "role": "assistant",
        "content": answer

    })

    # Save after every reply
    save_chat(messages)