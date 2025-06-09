POPULAR_TOKENS = {
    "USDC": "EPjFWdd5AufqSSqeM2qN1xzybapC8n3Y2cBa3Ck5KXG",
    "USDT": "Es9vMFrzaCER84dDJrvsr667jVhJ55johhGSST92MYL7",
    "BONK": "DezXy1ZZWVzFcE9XzZRZ62EQg3Z4rGX5r3AFu3jT44oD",
}


def get_supported_tokens():
    return [{"symbol": symbol, "mint": mint} for symbol, mint in POPULAR_TOKENS.items()]