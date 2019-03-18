import random

def get_question_from_user(name_of_user):
    print("{}, what is your question?".format(name_of_user))
    question = raw_input()

    print("Your question is: {}".format(question))

def generate_random_number():
    random_number = random.randint(0,4)
    return random_number

friend = raw_input("What is your name? ")
type(friend)
#friend = "Guzide"

answer_list = ["yes", "no", "maybe", "ask again", "no chance"]

get_question_from_user(friend)
random_number = generate_random_number()
answer = answer_list[random_number]

#ask again
if answer == "ask again":
    print(answer)
    get_question_from_user(friend)
    random_number = generate_random_number()
    answer = answer_list[random_number]
    print(answer)
else:
    print(answer)
