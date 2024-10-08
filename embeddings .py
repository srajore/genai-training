from openai import OpenAI
client = OpenAI(api_key="")

response = client.embeddings.create(
    model="text-embedding-3-large",
    input="The food was delicious and the waiter..."
)

print(response)