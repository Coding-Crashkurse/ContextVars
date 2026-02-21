"""4) copy_context() – Snapshots & Isolation."""
from contextvars import ContextVar, copy_context

theme: ContextVar[str] = ContextVar("theme", default="light")

theme.set("dark")
print(f"before: {theme.get()}")

ctx = copy_context()


def change_theme():
    theme.set("neon-pink")
    print(f"inside: {theme.get()}")


ctx.run(change_theme)
print(f"after:  {theme.get()}")
