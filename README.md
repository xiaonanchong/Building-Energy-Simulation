# Install Packages  

## install pip
$ sudo apt-get update  
$ sudo apt-get upgrade  
$ sudo apt-get install python-pip  

## install virtualenv to manage packages for different projects  
$ sudo apt install virtualenv | pip install virtualenv    
$ virtualenv venv/rl --python=python3  
activate virtualenv  
$ . /path/to/venv/bin/activate  (. venv/rl/bin/activate)  

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

MUJOCO INSTALLATION FAIL  

[install opencv:](https://docs.opencv.org/3.4.1/d2/de6/tutorial_py_setup_in_ubuntu.html)  
$ pip install matplotlib  
$ pip install ipython  
$ sudo apt-get install python-opencv  
test installation  
$ ipython  
In[1]: import cv2 as cv  
In[2]: print(cv.$__version__$) # 4.4.0  

## install gym  
$ pip install gym  

## install EnergyPlus  
$ wget https://github.com/NREL/EnergyPlus/releases/download/v9.1.0/EnergyPlus-9.1.0-08d2e308bb-Linux-x86_64.sh  

$ chmod +x EnergyPlus-9.1.0-08d2e308bb-Linux-x86_64.sh  
$ sudo ./EnergyPlus-9.1.0-08d2e308bb-Linux-x86_64.sh  
or just  
$ sudo bash EnergyPlus-9.1.0-08d2e308bb-Linux-x86_64.sh   
pay attention to directory orgamization  

PROBELM: readvarseso --help COMMAND NOT FOUND  

## clone  
clone gitL rl-testbed-for-energyplus  
$ git clone https://github.com/IBM/rl-testbed-for-energyplus.git  
clone git: energyplus 8.8.0  
$ git clone https://github.com/NREL/EnergyPlus.git  

## run 
$ time python3 -m baselines_energyplus.trpo_mpi.run_energyplus --num-timesteps 100  
