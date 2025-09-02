import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Say hello",
    max_tokens=5
)
print(response.choices[0].text)
