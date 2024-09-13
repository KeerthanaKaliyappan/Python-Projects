# Sentiment analysis of feedback using Text model

#Passing the role or behaviour in System role & passing the prompt in user role

from openai import OpenAI

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

response=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a Sentiment analyst."},
    {"role": "user", "content": """
    
    """}
    ],
    temperature=0.7,
    max_tokens=150
)

print(response.choices[0].message.content)