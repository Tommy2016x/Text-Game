

class room1():

    def __init__(self):
        self.drawsearch = False
        self.drawempty = False
        self.keypickup = False
        self.inroom = True
        self.closetsearch = False
        self.batpickup = False


    def drawerresponse(self):

            if self.drawsearch == False:
                print("After searching the drawer you find only but a small key, perhaps it will unlock the door?")
                print("A key has been added to your inventory\n")
                self.drawsearch = True
                self.keypickup = True

            elif self.drawsearch == True:
                print("There is nothing else here\n")

    def roomstatus(self):
        return self.inroom

    def dooropen(self):
        if self.keypickup == False:
            print("The door is locked, maybe theres a key somewhere?\n")

        elif self.keypickup == True:
            print("The door opens with the key, want to leave the room? \n[1]: leave the room \n[2]: stay in room")
            response = input()

            if response == "1":
                self.inroom = False
                print("You have left the room\n")

            elif response == "2":
                print("You have decided not to leave the room yet\n")

    def closetopen(self):
        if self.closetsearch == False:
            print(
                "In the closet there are old rugged clothes and a sturdy wooden baseball bat, "
                "perhaps it could be used as a weapon?\n[1]: Pick up the bat \n[2]: close closet\n" )

            response = input()

            if response == "1":
                self.batpickup = True
                self.closetsearch = True
                print("You picked up the baseball bat\n")
                return 1

            elif response == "2":
                print("You closed the closet\n")

        elif self.closetsearch == True:
            if self.batpickup == False:
                print("The bat is still there, Pick it up? \n[1]: yes \n[2]: no")
                response = input()
                if response == "1":
                    self.batpickup = True
                    print("You picked up the bat\n")

                elif response == "2":
                    print("You leave the bat in there\n")
            else:
                print("There is nothing else of use here\n")

    def play(self):



        while self.inroom == True:

            print(
                "With the light now you can clearly see around the room, there is a drawer next to the bed, and a closet"
                " on the other side of the wall \n[1]: Search drawer \n[2]: Search closet \n[3]: Open door")

            response = input()

            if response == "1":
                 self.drawerresponse()

            elif response == "2":
                 self.closetopen()

            elif response == "3":
                self.dooropen()


class Hallway():
    def __init__(self):
        self.infogain = False
        self.walkdownhall = False
        self.roomattempt = False
        self.encounterchoice = False


    def play(self):

        while self.walkdownhall != True:
            print("You step outside the room, you are greeted by a long narrow hallway in which you cannot see the end"
                  "to.On the sides of the wall are doors similiar to the one you came from. The walls are a dull grey "
                  "color which appear as if they have not been taken care of for years. \n[1]: walk down the hall"
                  "\n[2]: Go back inside the room \n")

            response = input()

            if response =="1":
                print("You walk down the hall")
                self.walkdownhall = True

            elif response == "2":

                if self.roomattempt == False:
                    print(
                        "You decide you have seen enough and turn back around to open the door, the door is locked. You"
                        "reach for your key but it slips out of your hand and falls into a ventilation shaft on in the "
                        "floor. You stare at it in a panic like state\n")
                    self.roomattempt = True

                else:
                    print("You stare down at the ventilation grate in despair\n")
            else:
                print("Please select an option\n")

        while self.encounterchoice != True:
            print("As you walk down the hall you attempt to open the other doors you pass. They are all locked and "
                  "even an attempt at knocking doesn't trigger a response. However as you pass by one of the doors you"
                  "suddenly hear a voice scream in desperation, 'HELLO?!?!, is anyone there! PLEASE, if anyone is there"
                  "please answer me!' You are startled by this but at the same are glad someone else is here. Maybe"
                  "they can help you find out whats happening, what if its a trap? \n[1]: Respond \n[2] Keep walking")









