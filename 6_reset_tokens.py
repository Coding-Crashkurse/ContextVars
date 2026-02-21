"""6) Reset Tokens – undo for context changes."""
from contextvars import ContextVar

mode: ContextVar[str] = ContextVar("mode", default="production")

print(f"default: {mode.get()}")

token = mode.set("debug")
print(f"changed: {mode.get()}")

mode.reset(token)
print(f"reset:   {mode.get()}")
