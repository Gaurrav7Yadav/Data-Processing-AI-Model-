import json
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
api_token = "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"
headers = {"Authorization": f"Bearer {api_token}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


number_source = int(input("Enter the number of source sentences: "))
source_sentences = []
s=[]

for j in range(number_source):
    while True:
        source_sentence = input("Enter source sentence: ")
        if source_sentence != "finish":
            source_sentences.append(source_sentence)
        else: 
            break
    s.append(" ".join(source_sentences))
    source_sentences= []  

number_input = int(input("Enter the number of input sentences: "))
input_sentences = []
I=[]

for j in range(number_input):
    while True:
        input_sentence = input("Enter input sentence: ")
        if input_sentence !="finish":
            input_sentences.append(input_sentence)
        else:
            break
    I.append(" ".join(input_sentences))
    input_sentences=[]


for source_sentence in s:
    data = query(
        {
            "inputs": {
                "source_sentence": source_sentence,
                "sentences": I 
            }
        }
    )
    print(data)
