from openai import OpenAI
client = OpenAI(api_key="")

response = client.images.generate(
    prompt="I want dog on moon (chandrayan)",
    size="1024x1024"
)

print(response.data[0].url)