from fastapi import FastAPI
from agent.state import AgentState
from agent.nodes import handle_input

app = FastAPI()
state = AgentState()

@app.post("/chat")
def chat(user_input: str):
    response = handle_input(state, user_input)

    return {
        "user_input": user_input,
        "response": response,
        "stage": state.stage
    }