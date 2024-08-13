import socket

from fastapi import FastAPI, Request

app = FastAPI()


def get_all_local_ips():
    local_ips = []
    try:
        # Obtener el nombre del host
        hostname = socket.gethostname()
        # Obtener todas las IPs asociadas con el hostname
        ips = socket.gethostbyname_ex(hostname)[2]
        # Filtrar solo las IPs locales (excluir loopback)
        local_ips = [ip for ip in ips if not ip.startswith("127.")]
    except Exception as e:
        print(f"Error al obtener IPs locales: {e}")
    return local_ips


@app.get("/")
async def read_root(request: Request):
    client_host = request.client.host
    all_local_ips = get_all_local_ips()
    return {
        "client_ip": client_host,
        "all_local_ips": all_local_ips
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
