# Python Robot Simulator
Python Robotics Simulator is developed by [Student Robotics](https://studentrobotics.org/). 
I have made use of the simulator to write down a simple code to find and grab Silver tokens from the Arena and pair them with Golden Tokens. 

# Downloading the Simulator
Open a shell and execute the following commands:
```bash
$ sudo apt-get update
```
```bash
$ sudo apt-get install git
```
```bash
$ git clone https://github.com/EhtishamAshraf/Python_Robot-Simulator
```

# Installing and Running
The simulator requires a Python 2.7 installation, the pygame library, PyPyBox2D, and PyYAML.

### Installing Python2 and Pip
Python2 and pip2 are required for the simulator. Following are the commands:
```bash
$ sudo add-apt-repository universe
``` 
```bash    
$ sudo apt update
``` 
```bash 
$ sudo apt install python2 python2-dev
```    
```bash
$ sudo apt-get install python2-dev
```    
```bash
$ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
```    
```bash
$ sudo python2 get-pip.py
```    
    
### Installing Libraries
Following are the commands:
```bash
Pygame: $ sudo pip2 install pygame
```  
```bash    
PyYAML: $ pip install PyYAML
```  
```bash    
PyPyBox2D: $ sudo pip install pypybox2d
```  

# Test the code on the Simulator 
Now open terminal, move to the robot-sim directory and run:
    To check the simulator environment: 
    ```  
    $ python2 run.py assignment.py
    ```  
    To check execution of the code: 
    ```  
    $ python2 run.py solution.py
    ```  

# Flow Chart of the code
![FlowChart](https://user-images.githubusercontent.com/108629700/197865764-5dd690fd-3648-47b4-b128-cb0b4e0046ea.png)

