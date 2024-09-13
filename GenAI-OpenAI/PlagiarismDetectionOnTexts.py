# Plagiarism detection using Embeddings model

#Embeddings are numberical or vector representation of word or a sentence.
#Numpy package's dot function is used to compare the embeddings and return a relativeness score

from openai import OpenAI
import numpy as np

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

texts=[]

response=client.embeddings.create(
    model="text-embedding-ada-002",
    input=texts
)

suspected_plagiarism_text_embedding=response.data[0].embedding

for i in range(1, len(texts)-1)
    similarity_score=np.dot(suspected_plagiarism_text_embedding, response.data[i].embedding)
    print("Text being compared: ", texts[0], "vs ", texts[i])
    print(similarity_score*100, %)