from openai import OpenAI
from config import OPEN_API_KEY

client = OpenAI(api_key=OPEN_API_KEY)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a nutritionist."},
        {
            "role": "user",
            "content": "Give a shopping list with associated recipes for 3 days. I have half a butternut squash to use up."
        }
    ]
)

print(completion.choices[0].message)