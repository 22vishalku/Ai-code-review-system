from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import openai
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Add middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can also use ["http://localhost:3000"] instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request body model
class CodeRequest(BaseModel):
    code: str

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def root():
    return {"message": "🚀 FastAPI backend is running"}

@app.post("/review")
async def review_code(request: CodeRequest):
    prompt = f"""You are an expert code reviewer. Review the following code and provide suggestions, improvements, and bug fixes:\n\n{request.code}"""
    
    try:
        # Use openai.chat_completions.create() method (correct method for OpenAI >=1.0.0)
        response = openai.chat_completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        
        # Return the AI-generated review
        return {"review": response["choices"][0]["message"]["content"]}
    
    except Exception as e:
        # Handle any errors
        return {"review": f"❌ Error: {str(e)}"}
