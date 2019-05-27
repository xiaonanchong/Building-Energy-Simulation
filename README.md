export OPENAI_LOGDIR=$HOME/logs/datacenter_ppo2_30000  
export OPENAI_LOG_FORMAT=csv  
python -m baselines.run --alg=ppo2 --env=gym_energyplus:EnergyPlus-v0 --num_timesteps=30000 --nsteps=128

