from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

chat = client.chats.create(
    model="gemini-2.5-flash-lite"
)

while True:
    question = input("You: ")

    if question.lower() == "quit":
        print("Goodbye!")
        break

    response = chat.send_message(question)

    print("\nAI:", response.text)
    print()
