# Python Robot Simulator
Python Robotics Simulator is developed by [Student Robotics](https://studentrobotics.org/). 
I have made use of the simulator to simulate a mobile robot to find and grab the Silver tokens from the Arena and to pair them with the Golden Tokens. 

![FlowChart](https://github.com/EhtishamAshraf/Python_Robot-Simulator/blob/main/Simulation%20Environment.png)


# Download the Simulator
Open shell and execute the following commands:
```bash
sudo apt-get update
```
```bash
sudo apt-get install git
```
```bash
git clone https://github.com/EhtishamAshraf/Python_Robot-Simulator
```

# Libraries required for the Simulator
The simulator requires a Python 2.7 installation, the pygame library, PyPyBox2D, and PyYAML.

### Installing Python2 and Pip
Python2 and pip2 are required for the simulator. Following are the commands which will help in installing everything, which is required for the simulator:
```bash
sudo add-apt-repository universe
``` 
```bash    
sudo apt update
``` 
```bash 
sudo apt install python2 python2-dev
```    
```bash
sudo apt-get install python2-dev
```    
```bash
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
```    
```bash
sudo python2 get-pip.py
```    
    
### Installing Libraries
Following are the commands:

Pygame:
```bash
sudo pip2 install pygame
```  
PyYAML:
```bash    
pip install PyYAML
```  
PyPyBox2D:
```bash    
sudo pip install pypybox2d
```  

# Test the code on the Simulator 
Now open terminal, move to the robot-sim directory and type the following commands:
    To check the simulator environment: 
    ```  
    python2 run.py task.py
    ```  
    To check execution of the code: 
    ```  
    python2 run.py solution.py
    ```  

# Flow of the code
1. Check if the unique ID of the visible Silver token is already present in the list or not?
    A. If already present then rotate the robot. 
    B. Otherwise, Robot picks up the visible silver token.
    C. Ammends the unique ID of the token in the list.
    D. Robot rotates in the arena to search for golden tokens.
2. If Golden token is found, check if the unique ID of the token is present in the list or not?
    A. If already present then rotate the robot. 
    B. Otherwise, Release the silver token near the golden token (pairing the tokens.)
    C. Adds the unique ID of the visible golden token in the list.
    D. Robot rotates in the arena to search for next silver token.
3. Repeat the above steps (1 to 2) untill both lists are full.
4. If all the tokens are paired successfully then the Robot retuns back to the center of the arena.
5. Exit the code.
![FlowChart](https://user-images.githubusercontent.com/108629700/197865764-5dd690fd-3648-47b4-b128-cb0b4e0046ea.png)

