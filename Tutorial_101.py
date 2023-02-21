# Inlcude Python libraries that you need to use in your program.

import time as time


# Place your classes (objects) and functions (groups if instructions)
# that you want to use in your script.  

def NPC_response_1(name):
    """
    This is a function that represents a NPC character introduction.
    """
    introduction = "Hello " + name + "."
    print(introduction)
    time.sleep(2)
    follow_response = "I am NPC one."
    print(follow_response)

class OctaneCar():
    """
    This a model of a RL car.
    The car only points north (for simplicity)
    """

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.boost = 100


    def forward(self):
        self.pos_x = self.pos_x + 1
        print("Car has moved forward one space")


    def turnright(self):
        self.pos_y = self.pos_y + 1
        print("Car has moved right one space")


    def turnleft(self):
        self.pos_y = self.pos_y - 1
        print("Car has moved left one space")


    def reverse(self):
        self.pos_x = self.pos_x - 1
        print("Car has moved backwards one space")


    def jump(self):
        self.pos_z = 1
        print("The car is the air for a second")
        time.sleep(1)
        self.pos_z = 0
        print("The car is back on te ground")


    def turbo(self):
        if self.boost > 0:
            self.pos_x = self.pos_x + 3
            self.boost = self.boost - 20
        else:
            print("You are out of boost")

    def check_status(self):
        # Print the position of the car.
        print(
            "Current car position is X: ",
            self.pos_x,
            ", Y: ",
            self.pos_y,
            ", Z: ",
            self.pos_z
            )

        # Print how much boost is left
        print("The car has ", self.boost, r"% left.")


# This is the script. This area allows you to connect your code instructions.  

if __name__ == "__main__":
    
    '''
    # Lessons 2:
    # Create a function
    '''

    # name_in = "Araan"
    # print(NPC_response_1(name=name_in))

    '''
    # Lesson 3:
    # Create a class to represent a car (Python Rocket League).
    '''
    Player1 = OctaneCar()

    # Where is the car?

    Player1.check_status()

    # Move the car to four spaces forward and one right.

    Player1.turbo()
    Player1.forward()
    Player1.turnright()

    # Lets check our position.

    Player1.check_status()

    # Lets check the boost function

    Player1.turbo()
    Player1.turbo()
    Player1.turbo()
    Player1.turbo()
    Player1.turbo()

    Player1.check_status()

else:
    print("Running out of script")