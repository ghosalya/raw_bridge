import os
import random
import argparse
import yaml
import shutil


def deck_generator():
    Suites = [
        "Spades",
        "Hearts",
        "Diamonds",
        "Clubs"
    ]

    Cards = [
        "A",
        "K",
        "Q",
        "J"
    ]

    for n in range(2,11):
        Cards.append(str(n))
    
    Deck = []
    for Suite in Suites:
        for Card in Cards:
            Deck.append( Suite + " - " + Card)
    
    return Deck


def handcard_generator(n_players=4, hand_size=13):
    newdeck = deck_generator()
    handcards = []

    for player in range(n_players):
        hand = []
        for hand_index in range(hand_size):
            new_card = random.choice(newdeck)
            newdeck.remove(new_card)
            hand.append(new_card)
        handcards.append(sorted(hand))

    return handcards


def run(rounds=10):
    shutil.rmtree("bridge_output")
    for r in range(1, 1+rounds):
        handcards = handcard_generator(hand_size=r, n_players=3)
        for p in range(3):
            output_path = "bridge_output" + "/player" + str(p) + "/round" + str(r) + ".txt"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as outfile:
                yaml.dump(
                    dict(cards=handcards[p], point=0), 
                    outfile
                )

if __name__ == "__main__":
    run()