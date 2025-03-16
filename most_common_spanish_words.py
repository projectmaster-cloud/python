import random

spanish_dicts = [
    #verbs
    [("ser", "to be")],
    #nouns
    [("person", "persona")],
    #adjectives
    [("bueno", "good")],
    #adverbs
    [("muy", "very")],
    #prepositions
    [("a", "to")],
]
#Learn how to get a random key for dict
def all():
    return random.choice(random.choice(spanish_dicts))

running = True

while running:
    score = 0

    questions = int(input("How much questions do you want to do? "))
    #type_words = input("""Enter 'type' to get different caterioges of words or
#Enter random to get all sorts of words""")

    for i in range(0, questions):
        spanish_pair = all()

        player_ans = input(f"What is your answer from the word in spanish {spanish_pair[0]}? ")

        while player_ans != spanish_pair[1]:
            print("Wrong")
            player_ans = input(f"What is your answer from the word in spanish {spanish_pair[0]}? ")

        if player_ans == spanish_pair[1]:
            print("correct")
            score+=1
