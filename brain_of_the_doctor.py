
from dotenv import load_dotenv
load_dotenv()
#Step 1: Setup GROQ APL key
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


#Step 2: Convert image to required format
import base64


#image_path ="acne.jpg"

def encoded_image(image_path):
    image_file = open(image_path, "rb")           #rb- read image in binary
    return base64.b64encode(image_file.read()).decode('utf-8')


#Step 3: Setup multimodal LLM

from groq import Groq

query= " Is there something wrong with my face bcoz i have seen some read rashe on my forehead"
model="meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    client=Groq(api_key=GROQ_API_KEY) 
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    print(chat_completion.choices[0].message.content)

    

if __name__ == "__main__":

    analyze_image_with_query(query, model, encoded_image)
