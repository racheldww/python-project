import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print (" After a night of drinking and signing by the bonfire, "
  "you and your friends decide to go to sleep. After an hour, "
  "you are awakened by the growling noises from outside your tent. "
  "You decide to explore where this intriguing noise is coming from. "
  "While trying to make sure you remember where your campside is, "
  "you start climbing a small hill. Then suddenly, you hear "
  "a grotesque sound emitting animal behind you. A dragon is "
  "flying towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the dragon
  B. Lie down and wait for it to pass
  C. Run""")
  choice = raw_input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWell, that was quick. "
    "\n\nYou died! "
    "\n(Who throws a rock at a dragon?!) ")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock():
  print ("\nThe dragon is stunned, but regains control. He begins "
  "flying towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = raw_input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first "
    "rock thrown did much damage. The rock flew well over the "
    "dragon's head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Near the entrance, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Yes/No?")
  choice = raw_input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = raw_input(">>> ")
  if choice in answer_A:
    print ("\nWell okay.. So you're going to hide in the dark? I think "
    "dragons can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou waited for the dragon to come closer. The shimmering "
    " sword attracted the dragon, which thought you were no match. As he "
    "came closer and closer, your heart beat rapidly. As the dragon "
    "reached out to look at the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nWho doesn't pick up a sword while running from a dragon? "
     "You should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the dragon enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the dragon turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the dragon's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = raw_input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for a dragon. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()

def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a building, waiting for the dragon to come "
  "charging around the corner. You notice a yellow flower "
  "near your foot. Do you pick it up? Yes/No")
  choice = raw_input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its growling getting closer and closer and "
  "ready yourself for the impending dragon.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the yellow flower, somehow "
    "hoping it will stop the dragon. It does! The dragon was just looking "
    "for a friend. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()
