# Step 1: Bot Personality
bot_name = "CryptoBuddy"
bot_tone = "friendly"
greeting = f"Hi there! I'm {bot_name}, your friendly crypto buddy! 🌟"

# Step 2: Stored Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Step 3: Chatbot Logic
def crypto_advisor(user_query):
    user_query = user_query.lower()
    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"Invest in {recommend}! 🌱It's eco-friendly and has long-term potential!")

    elif "trending" in user_query or "growth" in user_query:
        profitable_coins = [
            coin for coin, info in crypto_db.items()
            if info["price_trend"] == "rising" and info["market_cap"] in ["high", "medium"]
        ]
        if profitable_coins:
            print(f"{profitable_coins[0]} is on the rise and has incredible growth potential! 🚀")
        else:
            print("No trending coins right now. Keep an eye on the market!")
    
    else:
        print("Sorry, didn't catch that. Try asking 'trending' or 'sustainable' crypto!")

# Step 4: Interactive Chat Loop
print(greeting)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye! 👋  Stay safe in crypto trading!")
        break
    crypto_advisor(user_input)

# Step 5: Disclaimer
print("⚠️ Disclaimer: Crypto is risky—always do your own research!")
