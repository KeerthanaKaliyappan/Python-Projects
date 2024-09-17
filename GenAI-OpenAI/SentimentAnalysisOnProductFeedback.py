# Sentiment analysis of feedback using Text model

#Passing the role or behaviour in System role & passing the prompt in user role

#Temperature field denotes the level of randomness or relevance of output to the prompt

from openai import OpenAI

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

response=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a Sentiment analyst."},
    {"role": "user", "content": """Identify the sentiment of below feedback:
The EcoBreeze Air Purifier uses advanced HEPA filtration technology to remove 99.97% of airborne pollutants, ensuring cleaner, fresher air in your home.
Feedback:
1. The EcoBreeze Air Purifier is incredibly quiet and efficient, making it perfect for my bedroom.
2. It does the job, but the design is a bit bulky for my liking.
3. I noticed a significant improvement in air quality within a few days of using it.
4. The filter replacement is quite expensive and not very convenient.
5. Great value for the money with its high-performance filtration system and ease of use."""}
    ],
    temperature=0.7,
    max_tokens=150
)

print(response.choices[0].message.content)