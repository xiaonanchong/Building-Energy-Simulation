# Install Packages  

## install pip
$ sudo apt-get update  
$ sudo apt-get upgrade  
$ sudo apt-get install python-pip  

## install virtualenv to manage packages for different projects  
$ sudo apt install virtualenv | pip install virtualenv    
$ virtualenv venv/rl --python=python3  
$ . /path/to/venv/bin/activate  

## install baselines  
Prerequisites:  
$ sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev  
$ pip install tensorflow  

$ git clone https://github.com/openai/baselines.git  
$ cd baselines  
$ pip install -e .  

Test installation:  
$ pip install pytest  
$ pytest  

install MOjoco:  
[register with account number and computer id: ](https://www.roboti.us/license.html)  
to get computer id - download binary file getid_linux  
wget https://www.roboti.us/getid/getid_linux  
mark file as executable:  
$ chmod +x getid_linux  
$ ./getid_linux  
download Mujoco 2.0:  
& wget https://www.roboti.us/download/mujoco200_linux.zip  
$ unzip mujoco200_linux.zip  
put mjkey.txt in the same directory, then install  
$ export MUJOCO_PY_MJKEY_PATH=mjkey.txt  
$ export MUJOCO_PY_MUJOCO_PATH=mujoco200_linux/   
$ pip install -U 'mujoco-py<2.1,>=2.0'  

