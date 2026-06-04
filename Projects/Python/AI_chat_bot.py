import os
from openai import OpenAI


key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)

messages = []

def completion(message):
    global messages

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=messages
    )

    messages = {
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    }
    messages.append(messages)
    print(f'User: {message} \nAI: {response.choices[0].message.content}')

    # print(response)



# response = client.responses.create(
#     model="gpt-5.5",
#     instructions="You are a coding assistant that talks like a pirate.",
#     input="How do I check if a Python object is an instance of a class?",
# )

# print(response.output_text)
if __name__ == "__main__":
    user_question = input("Ask a question to the AI chat bot: ")
    ai_response = completion(user_question)
    print("AI Response:", ai_response.choices[0].message.content)




