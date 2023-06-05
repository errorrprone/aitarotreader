import openai
import time
from config import API_KEY

# Set up OpenAI API credentials. Please modify the config file to include your api key. Do not put the key in this file.
openai.api_key = API_KEY

question = input("Enter your question or situation: ")
prompt = f"""

Card 1:
Card 2:
Card 3:

Interpretation:
{question}
"""

def fisher_yates_shuffle(arr): # I chose the Fisher Yates shuffling algorithm over using random. Feel freet to add your own.
    for i in range(len(arr)-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_interpretation(cards):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + "\n".join(cards),
        max_tokens=300, # adjust the level of tokens as needed. If you pull more cards more tokens needed
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

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

fisher_yates_shuffle(tarot_deck)
cards = tarot_deck[:3]  # choose first three shuffled cards

interpretation = generate_interpretation(cards)

print("Card Draw:")
for i, card in enumerate(cards):
    print(f"Card {i+1}: ", end='', flush=True)
    for letter in card:
        print(letter, end='', flush=True)
        time.sleep(0.1)  # Delay between letters adjust as needed from 0.1 to whatever
    print()

print("\nInterpretation:")
for letter in interpretation:
    print(letter, end='', flush=True)
    time.sleep(0.1) # Delay between letters adjust number as needed from 0.1 to whatever
