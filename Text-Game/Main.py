
from Act1 import room1
from Act1 import Hallway

class textgame():

    def __init__(self):
        self.room = 1
        self.inventory = []

    def firstresponse(self,):

        valid = False

        while valid == False:

            print(
                "You wake up in an empty room, confused and groggy you realize that it is not your own room and are "
                "wondering if ""you are dreaming\n what do you do?"
                "\n[1]: Get out of bed \n[2]: Go back to sleep ,maybe its a bad "
                "dream")

            response = input()

            if response == "1":
                print("You got out of bed\n")
                valid = True

            elif response == "2":
                print("You try your best to sleep convincing yourself that this is all a dream but your anxiety keeps "
                      "you awake\n")
                valid = False


            else:
                print("Please select an option\n")
                valid = False


    def secondresponse(self,):

        valid = False

        while valid == False:

            print(
                "Standing in the empty room you can barely see anything. there are no windows and the lights are off, "
                "in front "
                "next to the door you notice a light switch \n[1]: Turn on the light \n[2]: Go back to bed "
                "\n[3]: Look around \n[4]: Open door" )

            response = input()

            if response == "1":
                print("You turned on the light\n")

                valid = True

            elif response == "2":
                print("You worrily lay back on your bed for a brief moment but your overwhelming anxiety prompts you to"
                      "jump out of it again\n")


            elif response == "3":
                print("In the vast darkness you attempt to walk around the room but cannot seem to find anything, the "
                      "only thing you can see is the door and the light switch next to it\n")


            elif response == "4" :
                print("You attempt to open the door but it is locked\n")


            else:
                print("Please select an option\n")



    def move(self, roomnum):
        self.room = int(roomnum)

    def pickup(self, object):
        self.inventory.append(object)




class leftchoice():

    def __init__(self):

        self.monsterfoundyou = False
        self.gunpickup = False
        self.desksearch = False


game = textgame()

R = room1()

endgame = False

game.firstresponse()

game.secondresponse()

R.play()

if R.batpickup == True:
    game.pickup("Bat")

if R.keypickup == True:
    game.pickup("Key")



print("inventory: ",game.inventory)

Hallway = Hallway()
Hallway.play()

# while response != "walk down hallway" and response != "walk down hall":
#
#     print(
#         "As you exit the room you find yourself in a long narrow hallway, with other doors similiar to yours along the "
#         "sides of the wall")
#
#     response = input()
#
#     if response == "go back" or response == "turn around":
#         print(
#             "You try to back inside the room you came from but the door is locked, as you attempt to take out the key it"
#             "slips out of your hands and falls into an open ventilation shaft")
#
#     if response == "look around":
#         print("you can only see doors with locks similiar to the one you were in, at the end of hall you can make a "
#               "subtle gleam of light, perhaps another doorway?")
#
#     if response == "walk down hallway" or response == "walk down hall":
#         print("You walk down the hallway, passing by many doors to the left and right of you, it is dimly lit with\n"
#               "suddenly you hear someone call out ",
#               "Hello? is anyone there? please help me i dont know where i am?!?!")
#
# print("They seem to be in distress, perhaps in a situation similiar to yours, do you respond or keep walking?")
#
# response = input()
#
# while response != "respond" or response != "keep walking":
#
#     if response == "respond":
#         print(
#             "You ask who's there, a faint voice says:\n you...you need to get out of here... theres this... thing... that "
#             "thats out there... i think it escaped!")
#         print(
#             "Before you can say anything else an alarm goes off in the hallway, with red sirens filling the room \n you "
#             "run to the end of the hall and are greeted with 2 passageways, one on your left and one on your right")
#
#     elif response == "Keep walking":
#         print("You decide to ignore the pleas for help and continue on down the hallway\n all of a sudden alarms and "
#               "red sirens go off and you in a panic run towards the end of the hall"
#               "\n you are greeted with two passageways one that leads to your left and one to your right")
#
#
# while response != "left" and response != "right":
#
#     print("Do you go to your left or your right?")
#
#     response = input()
#
#     if response == "left":
#         print("You decide to go to your left")
#
#         Left = leftchoice()
#
#         print("You stumble upon a large room with many monitors and graphs and images you cannot comprehend. There is a"
#               "desk which appears to be openable and a large closet next to you. ")
#
#     elif response == "right":
#         print("You decide to your left")







