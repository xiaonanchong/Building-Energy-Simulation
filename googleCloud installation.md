$ sudo apt-get update  
$ sudo apt-get upgrade  

### install pip:  
$ sudo apt-get install python3-pip  
$ sudo apt-get install python-pip  

### install gym:  
$ git clone https://github.com/openai/gym.git  
$ cd gym  
$ pip install -e .  

### install tensorflow:  
$ pip install tensorflow  

### install baselines:  
$ sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev  
$ git clone https://github.com/openai/baselines.git  
$ cd baselines  
$ pip install -e .  

$ pip install pytest  
$ pytest    __# error__  

### install energyplus:  
$ wget https://github.com/NREL/EnergyPlus/releases/download/v8.8.0/EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  
$ sudo bash EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  

### clone energyplus 8.8.0 git:  
$ git clone https://github.com/NREL/EnergyPlus.git  

### clone rl-testbed git:  
$ https://github.com/IBM/rl-testbed-for-energyplus.git  

### apply path to energyplus and build:  
$ cd <WORKING-DIRECTORY>/EnergyPlus  
$ patch -p1 < ../rl-testbed-for-energyplus/EnergyPlus/RL-patch-for-EnergyPlus-8-8-0.patch  
$ mkdir build  
$ cd build  
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/local/EnergyPlus-8-8-0 ..    # Ubuntu case  
$ cmake -DCMAKE_INSTALL_PREFIX=/Applications/EnergyPlus-8-8-0 .. # macOS case  
$ make -j4    __# error__                                                                                          
                                                                                                                 
### run energyplus similation:  
$ mkdir test  
copy idf file and epw file into /test  
$ energyplus -i /usr/local/EnergyPlus-8-8-0/Energy+.idd -w USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw 5ZoneAirCooled.idf  
the simulation results can be plotted using test/epluszsz.csv  
more details on: https://energyplus.net/quickstart#run  
