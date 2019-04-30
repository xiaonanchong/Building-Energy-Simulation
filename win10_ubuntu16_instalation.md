get ubuntu app from window  
control panel -> programs -> turn windows features on or off -> window subsystems for linux    

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
In[2]: print(cv.__version__) # 4.4.0  

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

## install EnergyPlus 8.8.0  
$ wget https://github.com/NREL/EnergyPlus/releases/download/v8.8.0/EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  
$ sudo bash EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  

## clone  
clone gitL rl-testbed-for-energyplus  
$ git clone https://github.com/IBM/rl-testbed-for-energyplus.git  
clone git: energyplus 8.8.0  
$ git clone https://github.com/NREL/EnergyPlus.git  

## apply patch to EnergyPlus and build  
$ cd EnergyPlus
$ patch -p1 < ../rl-testbed-for-energyplus/EnergyPlus/RL-patch-for-EnergyPlus-8-8-0.patch    # 5 out of 5 hunk failed  
$ mkdir build
$ cd build
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/local/EnergyPlus-8-8-0 ..  
$ make -j4   # error  

$ sudo make install   # error  

## before run  
[install mpi4y:](https://pypi.org/project/mpi4py/)  
$ pip install git+https://bitbucket.org/mpi4py/mpi4py  
install pandas:  
$ pip install pandas  

import sys and change os.exit() to sys.exit() in 'rl-testbed-for-energyplus/baselines_energyplus/trpo_mpi/run_energyplus.py'  

$ vim ~/.bashrc  
add environment variables  
export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"  
export ENERGYPLUS_MODEL="${MODEL_DIR}/2ZoneDataCenterHVAC_wEconomizer_Temp_Fan.idf"  
export ENERGYPLUS="${ENERGYPLUS_DIR}/energyplus"  

in 'rl-testbed-for-energyplus/gym_energyplus/envs/energyplus_env.py' comment a function which is not used:  
#def __del__(self):  
        # In case you forget to call env.stop()  
        # self.stop_instance()  

in '/baselines/baselines/trpo_mpi/trpo_mpi.py' change:  
def learn(*,  
to:  
def learn(*args,  

then: (remember activating the virtualenv - . venv/rl/bin/activate)  
$ cd baselines  
$ pip install -e .  

in 'rl-testbed-for-energyplus/baselines_energyplus/trpo_mpi/run_energyplus.py' line 51 change code to:  
trpo_mpi.learn(env=env, network=policy_fn,  
                   total_timesteps=num_timesteps,  

## run 
$ cd /rl-testbed-for-energyplus  
$ time python3 -m baselines_energyplus.trpo_mpi.run_energyplus --num-timesteps 100  
