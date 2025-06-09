from fastapi import FastAPI
from routes import balance, swap
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from routes import balance, tokens


load_dotenv()

app = FastAPI(title="Token Exchange MVP")

app.include_router(balance.router)
app.include_router(swap.router)
app.include_router(balance.router)
app.include_router(tokens.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
