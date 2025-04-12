import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Hugging Face API token from .env file
API_TOKEN = os.getenv("HF_API_TOKEN")

# Set model endpoint (you can try different models too)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

# Prepare request headers
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_resume_text(data):
    """
    Generates professional resume text using Hugging Face Inference API.
    Removes prompt from the model output if echoed.
    """
    prompt = f"""
    Create a professional resume using the following details:
    Name: {data.name}
    Education: {data.education}
    Skills: {data.skills}
    Projects: {data.projects}
    
    Format it properly with clear headers like Summary, Education, Skills, Projects.
    Keep it concise and professional.
    """

    # Send request to Hugging Face
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    result = response.json()

    if "error" in result:
        raise Exception(f"Hugging Face API Error: {result['error']}")

    # Clean output by removing prompt echo (if exists)
    try:
        full_text = result[0]["generated_text"]
        cleaned_text = full_text.replace(prompt.strip(), "").strip()
        return cleaned_text
    except (KeyError, IndexError):
        return str(result)
