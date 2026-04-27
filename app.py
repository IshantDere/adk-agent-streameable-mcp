from fastapi import FastAPI
from pydantic import BaseModel
from agents.agent import agent
from google.adk.runners import InMemoryRunner

app = FastAPI()

runner = InMemoryRunner(agent=agent)   # create once globally

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        result = await runner.run_debug(req.message)
        return {"status": "success", "output": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}