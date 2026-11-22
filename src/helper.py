import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file (str): The path to the PDF file.

    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_openai(prompt, max_tokens=500):
    """
    Sends a prompt to the OpenRouter API and returns the response.

    Args:
        prompt (str): The prompt to send to the API.
        max_tokens (int): Maximum number of tokens in the response.

    Returns:
        str: The response from the API.
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
