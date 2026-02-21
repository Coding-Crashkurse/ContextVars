"""3) FastAPI – ContextVar per Request via Dependency."""
from contextvars import ContextVar
from fastapi import FastAPI, Depends, Header

app = FastAPI()
user_id: ContextVar[str] = ContextVar("user_id")


def set_user_context(x_user_id: str = Header(...)) -> str:
    """Dependency: setzt die ContextVar einmal pro Request."""
    user_id.set(x_user_id)
    return x_user_id


def log(msg: str):
    print(f"  [{user_id.get()}] {msg}")


async def generate_response(text: str) -> str:
    log(f"generating response for '{text}'")
    return f"reply to '{text}'"


@app.get("/chat")
async def chat(text: str, uid: str = Depends(set_user_context)):
    response = await generate_response(text)
    return {"user": uid, "response": response}
