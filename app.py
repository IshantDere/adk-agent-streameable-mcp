from fastapi import FastAPI
from pydantic import BaseModel
from agents.agent import agent

app = FastAPI()

class Query(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/chat")
async def chat(query: Query):
    response = agent.run(query.message)
    return {"response": response}