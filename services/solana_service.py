import os
from solana.rpc.api import Client
from solana.rpc.api import Pubkey

client = Client(os.getenv("RPC_URL"))

def get_balance(address: str) -> float:
    pubkey = Pubkey(address)
    response = client.get_balance(pubkey)
    lamports = response['result']['value']
    return lamports / 1_000_000_000  # SOL
