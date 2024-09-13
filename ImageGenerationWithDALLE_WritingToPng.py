# Image generation with DALLE model 

#Image generation with prompt and returns a binary format of image

#'n' parameter indicates the variations or no. of output images

from openai import OpenAI
from base64 import b64decode

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

response=client.images.create(
    prompt="Generate a image of programmer on the moon",
    size="512x512",
    n=1,
    response_format="b64_json"
)

image_bytes=response.data[0].b64_json
image_file=open("programmerOnMoon.png", model="wb")
image_file.write(image_bytes)
image_file.close()