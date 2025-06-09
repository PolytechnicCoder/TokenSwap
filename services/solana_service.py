import os
from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts
from solders.pubkey import Pubkey

# Завантажуємо RPC_URL з .env
load_dotenv()
client = Client(os.getenv("RPC_URL"))


def get_balance(address: str) -> float:
    """Повертає баланс SOL у одиницях SOL"""
    pubkey = Pubkey.from_string(address)
    response = client.get_balance(pubkey)
    lamports = response.value  # новий формат
    return lamports / 1_000_000_000


def get_spl_token_balance(address: str, mint_address: str) -> float:
    """
    Повертає баланс SPL токена по mint-адресі.
    Якщо акаунт не існує — повертає 0.0
    """
    owner = Pubkey.from_string(address)
    mint = Pubkey.from_string(mint_address)

    accounts = client.get_token_accounts_by_owner(
        owner,
        TokenAccountOpts(mint=mint)  # обовʼязковий формат для нових версій
    )

    value = accounts.value
    if not value:
        return 0.0  # У користувача немає такого токена

    token_account_pubkey = Pubkey.from_string(value[0].pubkey)
    balance_info = client.get_token_account_balance(token_account_pubkey)

    return float(balance_info.value.ui_amount or 0.0)
