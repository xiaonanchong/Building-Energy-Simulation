OS: ubuntu 16  
```
$ sudo apt-get update  
$ sudo apt-get upgrade  
```
### install pip:  
```
$ sudo apt-get install python3-pip  
$ sudo apt-get install python-pip  
```

### install energyplus:  
```
$ wget https://github.com/NREL/EnergyPlus/releases/download/v8.8.0/EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  
$ sudo bash EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  
```
### run energyplus similation:  
```
$ mkdir test  
copy idf file and epw file into /test  
$ energyplus -i /usr/local/EnergyPlus-8-8-0/Energy+.idd -w USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw 5ZoneAirCooled.idf  
the simulation results can be plotted using test/epluszsz.csv  
```
more details on: https://energyplus.net/quickstart#run  

### clone energyplus 8.8.0 git:  
```
$ wget https://github.com/NREL/EnergyPlus/archive/v8.8.0.zip  
$ sudo apt-get install unzip  
$ unzip v8.8.0.zip  
```

### clone rl-testbed git:  
```
$ git clone https://github.com/IBM/rl-testbed-for-energyplus.git  
```
### apply patch to energyplus and build:  
```
$ cd <WORKING-DIRECTORY>/EnergyPlus  
$ patch -p1 < ../rl-testbed-for-energyplus/EnergyPlus/RL-patch-for-EnergyPlus-8-8-0.patch  
$ mkdir build  
$ cd build  
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/local/EnergyPlus-8-8-0 ..    # Ubuntu case  
$ cmake -DCMAKE_INSTALL_PREFIX=/Applications/EnergyPlus-8-8-0 .. # macOS case  
$ make -j4                                                                                              
```

set up environment variables and run.  

### minstall mpi4y and pandas:  
```
$ pip3 install git+https://bitbucket.org/mpi4py/mpi4py  
$ pip3 install pandas  
```

### install gym:  
```
$ git clone https://github.com/openai/gym.git  
$ cd gym  
$ pip install -e .  
```
### install tensorflow:  
```
$ pip install tensorflow  
```
### install baselines:  
```
$ sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev  
$ git clone -n https://github.com/openai/baselines.git  
$ git checkout 366f486  
$ cd baselines  
$ pip3 install -e .  
```

#### install opencv:  
```
$ pip3 install matplotlib   
$ sudo apt-get install python-opencv  
test installation  
$ python3    
In[1]: import cv2 as cv  
In[2]: print(cv.version) # 4.4.0  
```
#### install atari_py:  
```
pip3 install gym[atari]  
```
#### run baselines example: 
```
$ python3 -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4 --num_timesteps=2e7 --save_path=~/models/pong_20M_ppo2  
$ python3 -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4 --num_timesteps=0 --load_path=~/models/pong_20M_ppo2 --play  
```


## running  
$ time python3 -m baselines_energyplus.trpo_mpi.run_energyplus --num-timesteps 1000000000
