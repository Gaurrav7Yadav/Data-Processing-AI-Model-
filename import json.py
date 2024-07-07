import json
import requests
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
api_token="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"
headers = {"Authorization":f"Bearer {api_token}"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
number = int(input("enter number of source files"))
l=[]
for j in range(0,number):
   file=input("enter source sentence")
   l.append(file)

number = int(input("enter number of input files"))
L=[]
for j in range(0,number):
   file=input("enter input sentence")
   L.append(file)

for i in l:
   data = query(
      {
            "inputs": {
               "source_sentence": i,
               "sentences":L
            }
      }
   )
   print(data)
# The 'data' variable now contains the API response, which includes the relevance scores.
