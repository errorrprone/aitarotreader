#!/usr/bin/python3
#lets get a tarot reading from an ai

import random
import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Prompt for tarot card draw
prompt = """
You are about to pull three tarot cards from an entire tarot deck. Please focus on your question or situation.

Card 1:
Card 2:
Card 3:

Interpretation:
"""

# Generate interpretation using ChatGPT
def generate_interpretation(cards):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + "\n".join(cards),
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Full deck of tarot cards
tarot_deck = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant",
    "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man",
    "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World",
    "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands",
    "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands",
    "Queen of Wands", "King of Wands", "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups",
    "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups",
    "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups", "Ace of Swords", "Two of Swords",
    "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords",
    "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords", "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles",
    "Four of Pentacles", "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles",
    "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles",
    "King of Pentacles"
]

# Prompt user to pull three tarot cards
cards = random.sample(tarot_deck, 3)

# Generate interpretation
interpretation = generate_interpretation(cards)

# Print the card draw and interpretation
print("Card Draw:")
for i, card in enumerate(cards):
    print(f"Card {i+1}: {card}")
print("\nInterpretation:")
print(interpretation)
