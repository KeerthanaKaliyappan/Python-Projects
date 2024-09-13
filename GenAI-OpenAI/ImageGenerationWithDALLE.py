# Image generation with DALLE model 

#Image generation with prompt and returns a cloud storage url for the generated image

#'n' parameter indicates the variations or no. of output images

from openai import OpenAI

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

response=client.images.create(
    prompt="Generate a image of programmer on the moon",
    size="512x512",
    n=3
)

print(response)