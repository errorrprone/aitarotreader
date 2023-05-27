# let's get a tarot reading from an ai

import sys, time, random
from math import isnan
import openai

def slow_print(str):
   for c in str:
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

# fill out the card deck
def gen_deck():
    tarot_deck = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant",
        "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man",
        "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World",
    ]
    for suit in ["Wands", "Cups", "Swords", "Pentacles"]:
        for entry in ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]:
            tarot_deck.append(f"{entry} of {suit}")
        for entry in ["Page", "Knight", "Queen", "King"]:
            tarot_deck.append(f"{entry} of {suit}")
    return tarot_deck

# load the api key from a file
def load_api_key(filename):
    with open(filename, "r") as f:
        OPENAI_API_KEY = f.read().strip()
    openai.api_key = OPENAI_API_KEY

# generate interpretation
def generate_interpretation(query, cards):
    # prompts for tarot card draw
    prompt_basis = 'My tarot query: "%s" I drew: "%s."\
        Here is a brief interpretation of this reading in under 100 words, including 3 single-word motivations.'
    prompt = prompt_basis%(query, ", ".join(cards))

    max_tokens = max(100 * len(cards), 400)
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.65,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# prompt the user for a number of cards to draw
def prompt_num_cards():
    num_cards = 0
    while num_cards <= 0 or num_cards > 78 or isnan(num_cards):
        slow_print("\nHow many cards would you like to draw?\n\t")
        num_cards = int(input())
        if num_cards > 78:
            slow_print("Tarot decks only have 78 cards.")
        elif num_cards <= 0:
            slow_print("Please enter a positive number of cards.")
        elif isnan(num_cards):
            slow_print("Please enter a number between 1 and 78.")
    return num_cards

# pull the cards and reverse them randomly
def pull_cards(num_cards):
    tarot_deck = gen_deck()
    cards = random.sample(tarot_deck, num_cards)
    for i in range(0, num_cards):
        if random.random() > 0.5:
            cards[i] = cards[i] + " (reversed)"
    return cards

def full_reading():
    slow_print("\nWelcome to your personal tarot reader.\n")
    load_api_key(".key")
    num_cards = prompt_num_cards()
    cards = pull_cards(num_cards)
    slow_print("\nWhat is your query?\n\t")
    query = input()
    interpretation = generate_interpretation(query, cards)
    for i, card in enumerate(cards):
        slow_print(f"\nCard {i+1}: {card}\n")
    slow_print(f"\n{interpretation}\n\nPlease take care.\n")

# implementing name guarding. it's an ancient technique, but still commonly useful
if __name__ == '__main__':
    full_reading()
