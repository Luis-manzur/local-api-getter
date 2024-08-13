import socket

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def read_root(request: Request):
    client_host = request.client.host
    return {
        "client_ip": client_host,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
