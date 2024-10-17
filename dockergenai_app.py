from fastapi import FastAPI 
from transformers import pipeline

app=FastAPI()

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")

def home():
    return {"message": "Hello World"}

#define a function to handle the get request at /generate

@app.get("/generate")

def genrate(text:str):
    #use the pipeline to generate text from input text
    output=pipe(text)

    #return the generated text in JSON

    return {"output":output[0]['generated_text']}

