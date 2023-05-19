from fastapi import FastAPI
from fastapi.utils import *
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append("..")
from Server.subroutes import crypto
from Server.subroutes import database

app = FastAPI()
app.include_router(crypto.router, prefix="/crypto", tags=["crypto"])
app.include_router(database.router, prefix="/db", tags=["database"])

origins_regex = re.compile(r"https?://(?:localhost|127\.0\.0\.1)(?::[0-9]+)?(?![^:])")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=origins_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/ping")
def ping() -> str:
    """
    Returns a simple pong.\n
    :return: A simple pong\n
    """
    return "pong"


@app.get("/")
def root() -> dict:
    """
    Returns all the routes.\n
    :return: All the routes\n
    """
    out = {}
    paths = []
    paths = [i.path for i in app.routes]
    paths = sorted(paths)
    for i in paths:
        out[i] = [j.name for j in app.routes if j.path == i][0]
    return out