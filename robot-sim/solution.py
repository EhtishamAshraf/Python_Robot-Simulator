""" 
Code to pick Silver Tokens from the arena and pair them with Golden Tokens:

Robot checks the Unique ID associated with each Token (Silver/Golden) to make sure that one ID is ...
picked only once.

Robot scans the area once all the pairs are made (Both lists are filled with unique IDs) ... 
to confirm if any silver token is left behind. Once all pairs are made ... 
Robot returns back to the center of the Arean.

Adjust linear speed of the Robot as required: 
Line 222 for grabbing the Silver Tokens & Line 174 for pairing with Golden Tokens.

Robot turns left after grabbing the Silver Token and right after pairing it with Golden Token.

                                -------------------------------
Flow of the Code:
    1. Check if the unique ID of the visible Silver token is already present in the list or not?
       A. If already present then rotate the robot. 
       B. Otherwise, Robot picks up the visible silver token.
       C. Ammends the unique ID of the token in the list.
       D. Robot rotates in the arena to search for golden tokens.
    2. If Golden token is found, check if the unique ID of the token is not present in the list or not?
       A. If already present then rotate the robot. 
       B. Otherwise, Releases the silver token near the golden token (pairing the tokens.)
       C. Adds the unique ID of the visible golden token in the list.
       D. Robot rotates in the arena to search for next silver token.
    3. Repeat the above steps (1 to 2) untill both lists are full.
    4. If all the tokens are paired successfully then the Robot retuns back to the center of the arena.
    5. Code exit.

Following functions of the Robot class are used:

--R.see() = to get unique ID of each token, distance of robot from each token and rotation along y-axis.
--R.grab() = to grab the nearest token
--R.release() = to release the grabbed token.

"""
from __future__ import print_function
import time
from sr.robot import * # import * is used to import all functions and classes of the sr.robot module
""" Import required libraries"""

a_th = 2.0
a_th1 = 2.0
""" float: Threshold for the control of the linear distance for both Tokens (SILVER/GOLD)"""

d_th = 0.4
d_th1 = 0.5
""" float: Threshold for the control of the orientation for both Tokens (SILVER/GOLD)"""

counter=0
""" Integer: variable for controlling the Robot motion after all Tokens are placed / Stopping the Robot"""

i=0
j=0
Current_Silver=[None] * 6
Current_Golden=[None] * 6
""" Initializing Arrays of None and length 6, and variables for incrementing the arrays """

Check = False
"""
Check Variable is used to check if Silver & Golden Tokens ID is already stored in the List or not.
if Token ID is already stored in the List then we discard that Token.
"""


R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    
    Syntax: motor board srABC1, channel 1 to half power forward
    R.motor_boards["srABC1"].motors[1].power = 0.5
    """
    R.motors[0].m0.power = speed # setting power of motor 0 connected to motor board (motors[0]) of robot
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest silver token

    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    R.see() function details could be found here: https://github.com/CarmineD8/python_simulator 
    """
    dist=100
    for token in R.see(): # getting all the values of the R.see() function in token variable. 
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
            Silver_ID=token.info.code # This gives us the unique code associated with each Silver Token
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1, -1
    else:
   	return Silver_ID, dist, rot_y

def find_golden_token():
    """
    Function to find the closest golden token

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist1=100
    for token in R.see():
        if token.dist < dist1 and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist1=token.dist
            Golden_ID=token.info.code # This gives us the unique code associated with each Silver Token
	    rot_y1=token.rot_y
    if dist1==100:
	return -1, -1, -1
    else:
   	return Golden_ID, dist1, rot_y1


def Release_Silver_near_Gold():
    """
    Function to Release the Silver Token near Golden Token

    Robot checks distance from Golden token & when distance is lesser than set threshold then the Robot releases the Token
    Robot moves a bit and exits the loop so that code goes back to the main loop and pick up new Silver Token

    """
    global j # Making the variable j global so that we can use it inside the function
    while 1: # While loop to move the robot until Golden token is not found and silver token is not paied
    	Golden_ID, dist1, rot_y1 = find_golden_token() # Getting Golden token unique ID, dist from robot and rotation along y-axis
        print("----------------------------------------------------------------------------")
        print("Silver_ID: " + str(Silver_ID), "| Golden_ID: " + str(Golden_ID))
        print("Silver Distance: " + str(dist), "| Golden Distance: " + str(dist1))
        print("List containing Silver ID: ", Current_Silver, "| List containing Golden ID: ", Current_Golden, "\n")

        # Check if Currently visible Golden ID is present in our List? 
        # If it is present, then change the value of the Check variable else don't change...
        if Golden_ID in Current_Golden:
            Check = True
            print("Yes, Visible Golden Token's ID is present in the List !!!")
        else:
            Check = False
            print("No, Visible Golden Token's ID is not present in the List !!! \n")
        # Robot only pairs up the Silver Token with that Golden token whose Unique ID is not previously stored in our List
        if Check == False:
            if dist1==-1: # if no token is detected, we make the robot turn 
	            print("I don't see any Golden token!! \n")
	            turn(10, 1)
            # if Golden token is near then we release the Silver token to make the pair.
            # Also, add the current Golden Token ID in the list on the current index (starting from 0 index)
            # Also increase the value of the index so that the ID of next token is placed on the next index
            #Break the while loop after pairing operation is completed
            elif dist1 <d_th1: 
                print("Golden Token Found!")
                R.release()
                Current_Golden[j]=Golden_ID
                print("Grabbed Silver Token is paired with Golden Token having unique ID: ", Current_Golden[j])
                print("List containing Silver ID: ", Current_Silver, "| List containing Golden ID: ", Current_Golden, "\n") 
                j=j+1          
                drive(-30,2)
                turn(20,1.5)
                break # Break the loop if Golden Token is released
            elif -a_th1<= rot_y1 <= a_th1: # if the robot is well aligned with the token, we go forward
	        print("Ah, that'll do.\n")
                drive(100, 0.5)
            elif rot_y1 < -a_th1: # if the robot is not well aligned with the token, we move it on the left or on the right
                print("Left a bit...")
                turn(-2, 0.5)
            elif rot_y1 > a_th1:
                print("Right a bit...")
                turn(+2, 0.5)
        else:
            turn(10,1)
            drive(10,1)

"""Main While loop of the Code: """
while 1:
    # Getting Golden & Silver token unique ID, dist from robot and rotation along y-axis
    Silver_ID, dist, rot_y = find_silver_token()
    Golden_ID, dist1, rot_y1 = find_golden_token()
    print("----------------------------------------------------------------------------")
    print("Silver_ID: " + str(Silver_ID), "| Golden_ID: " + str(Golden_ID))
    print("Silver Distance: " + str(dist), "| Golden Distance: " + str(dist1))
    print("List containing Silver ID: ", Current_Silver, "| List containing Golden ID: ", Current_Golden, "\n")

    # Check if Currently visible Silver ID is present in our List? 
    # If it is present, then change the value of the Check variable else don't change...
    if Silver_ID in Current_Silver: 
        Check = True
        print("Yes, Visible Silver Token's ID is present in the List !!!")
    else:
        Check = False
        print("No, Visible Silver Token's ID is not present in the List !!! \n")

    # Robot only picks up the Silver Token if Unique ID of the token is not previously stored in our List
    if Check == False:
        if dist==-1: # if no token is detected, we make the robot turn 
	        print("I don't see any token!! \n")
	        turn(10, 1)
        elif dist <d_th: # if we are close to the token, we try grab it.
            print("Silver Token Found!")
            # if we grab the token, then we add the ID of the token on the current index of the list.
            # Also increase the value of the index so that the ID of next token is placed on the next index
            if R.grab(): 
                Current_Silver[i]=Silver_ID
                print("Silver Token having ID: ",Current_Silver[i], "is picked")
                print("List containing Silver ID: ", Current_Silver, "| List containing Golden ID: ", Current_Golden, "\n")
                i=i+1
	        turn(-25, 2)
	        Release_Silver_near_Gold() # If token is grabbed, we go to the function to pair it with Golden token
        elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
	    print("Ah, that'll do. \n")
            drive(100, 0.5)
        elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
            print("Left a bit...")
            turn(-2, 0.5)
        elif rot_y > a_th:
            print("Right a bit...")
            turn(+2, 0.5)
    else: # If Unique ID of the token is previously stored in our List then Robot turns a bit to scan the arean
        print("Scanning the area to find Silver Token which hasn't yet been picked up !!! \n")
        turn(10,1)
        # Check if all the 6 tokens are paired properly? If yes, then exit the code
        if None not in Current_Golden:
            print("All Tokens are paired properly ... Exiting the program ...\n")
            turn(15,0.5)
            drive(100,1.4)
            exit()