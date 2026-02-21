"""5) Request Logging – async-safe without passing state."""
import asyncio
from contextvars import ContextVar

request_id: ContextVar[str] = ContextVar("request_id")


def log(msg: str):
    print(f"  [{request_id.get()}] {msg}")


async def fetch_db():
    log("querying db")
    await asyncio.sleep(0.1)
    log("db done")


async def call_api():
    log("calling external api")
    await asyncio.sleep(0.2)
    log("api done")


async def handle_request(rid: str):
    request_id.set(rid)
    log("start")
    await fetch_db()
    await call_api()
    log("finished")


async def main():
    await asyncio.gather(
        handle_request("req-1"),
        handle_request("req-2"),
        handle_request("req-3"),
    )


asyncio.run(main())
