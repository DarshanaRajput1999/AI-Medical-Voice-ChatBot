# test.py

import os
import base64
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Step 1: Encode image to base64
def encode_image(image_path):
    print(f"📷 Checking image: {image_path}")
    if not os.path.exists(image_path):
        print(f"❌ Image not found at path: {image_path}")
        return None

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
        print("✅ Image encoded successfully.")
        return encoded

# Step 2: Send prompt and image to GROQ multimodal LLM
def analyze_image_with_query(query, model, encoded_image):
    if not encoded_image:
        print("⚠️ No encoded image provided. Aborting.")
        return "No Image Provided."

    print("🚀 Starting image analysis...")
    print("🔁 Sending image and query to GROQ model...")

    client = Groq(api_key=GROQ_API_KEY)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    try:
        chat_completion = client.chat.completions.create(
            model=model,
            messages=messages
        )
        response = chat_completion.choices[0].message.content
        print("🧠 Model Response:")
        print(response)
        return response
    except Exception as e:
        print(f"❌ Error during Groq model call: {e}")
        return "Error in imagic analysis"

# Step 3: Main execution
if __name__ == "__main__":
    image_path = "acne.jpg"
    query = "Is there something wrong with my face? I see red rashes on my forehead."
    model = "meta-llama/llama-4-scout-17b-16e-instruct"

    encoded = encode_image(image_path)
    response = analyze_image_with_query(query, model, encoded)
    print("📢 Final Response:\n", response)
