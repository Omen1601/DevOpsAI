from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from embed import qa_chain
import openai


load_dotenv()
app = FastAPI()

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    result: str
    output: str

@app.post("/execute-code/", response_model=CodeResponse)
def execute_code_endpoint(request: CodeRequest):
    result = execute_code(request.code)
    return result

@app.get("/resolve-error/{error_message}")
def resolve_error(error_message: str):
    response = qa_chain.run(error_message)
    return {"suggested_solution": response}
