# Multi model Audio to Text conversion

#Audio file to English conversion and finding the output for the response

#System role not required for audio response

from openai import OpenAI

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

audio_response=client.audio.transcriptions.create(
    model="whisper-1",
    file=open("tutorial_audio.mp3", "rb"),
    response_format="text"
)

response=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Summarize the below tutorial context: "+audio_response}
    ]
)

print(response.choices[0].message.content)