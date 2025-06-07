from fastapi import FastAPI
from routes import balance, swap
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Token Exchange MVP")

app.include_router(balance.router)
app.include_router(swap.router)
