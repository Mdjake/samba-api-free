# SambaNova Simple API

A simple FastAPI web API that wraps the SambaNova LLM inference code. Accepts a `query` parameter and returns the AI response.

## Setup
1. Set your SambaNova API key:
   ```
   set SAMBANOVA_API_KEY=22240d44-0bff-46e5-ad35-069e2fcbc2f4
   ```
   (Or pass `?api_key=your_key` in the URL)

2. Install dependencies:
   ```
   cd "C:\Users\pc\Desktop\sambanova-api"
   pip install -r requirements.txt
   ```

## Run the Server
```
cd "C:\Users\pc\Desktop\sambanova-api"
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
**Or run directly:**
```
python main.py
```

Server runs at http://localhost:8000

## Usage in Chrome
Open in browser:
- http://localhost:8000/?query=What is artificial intelligence?
- Add `&api_key=your_key` if not using env var.

Example response (JSON):
```json
{
  "response": "AI is ..."
}
```

## Interactive Docs
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## TODO
See TODO.md for progress.

