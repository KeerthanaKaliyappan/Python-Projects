# Plagiarism detection using Embeddings model

#Embeddings are numberical or vector representation of word or a sentence.
#Numpy package's dot function is used to compare the embeddings and return a relativeness score

from openai import OpenAI
import numpy as np

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

texts=["Technological progress has led to major changes in various industries. Automation and modern tools have improved efficiency and created new opportunities. Specifically, the retail sector has seen a revolution with e-commerce, allowing consumers to shop from anywhere and at any time, compelling businesses to quickly adapt.", "With advancements in technology, various industries have undergone significant changes. The rise of automation and digital tools has optimized workflows and opened up new business opportunities. For example, the retail industry has been transformed by e-commerce, which allows customers to shop online from anywhere and at any time. This shift has forced businesses to adapt quickly to stay competitive.", "Digital innovation has dramatically altered many traditional industries. The use of new technologies and automation has enhanced efficiency and created growth opportunities. In particular, e-commerce has revolutionized retail by enabling online shopping from virtually any location, requiring businesses to evolve rapidly to meet customer expectations."]

response=client.embeddings.create(
    model="text-embedding-ada-002",
    input=texts
)

suspected_plagiarism_text_embedding=response.data[0].embedding

for i in range(1, len(texts)-1)
    similarity_score=np.dot(suspected_plagiarism_text_embedding, response.data[i].embedding)
    print("Text being compared: ", texts[0], "vs ", texts[i])
    print(similarity_score*100, %)