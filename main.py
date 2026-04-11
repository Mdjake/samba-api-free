from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from sambanova import SambaNova
from typing import Optional
import uvicorn

app = FastAPI(title="SambaNova Simple API", description="API to query SambaNova model via query parameter")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def generate_response(query: str, api_key: Optional[str] = None):
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query parameter is required and cannot be empty")
    
    # Get API key from param, env var, or raise error
    api_key = api_key or os.getenv("SAMBANOVA_API_KEY") or "22240d44-0bff-46e5-ad35-069e2fcbc2f4"
    if not api_key:
        raise HTTPException(status_code=400, detail="API key required via ?api_key=... or env var SAMBANOVA_API_KEY")
    
    try:
        client = SambaNova(
            api_key=api_key,
            base_url="https://api.sambanova.ai/v1",
        )
        
        response = client.chat.completions.create(
            model="DeepSeek-V3-0324",
            messages=[
                {"role": "system", "content": "You are a strict librarian AI.

You must ALWAYS respond in valid JSON format only.

Format:
{
  "book": "Book Name",
  "message": "Your normal helpful response"
}

Rules:
- Always suggest exactly ONE book
- "book" must contain only the book name
- "message" must contain the explanation
- Do NOT add extra text outside JSON
- Do NOT add markdown, backticks, or explanation
- If no book is relevant, still return a best possible book

User question:."},
                {"role": "user", "content": query}
            ],
            temperature=0.1,
            top_p=0.1
        )
        
        ai_response = response.choices[0].message.content
        return {"owner":"Romeo_jake","response": ai_response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

