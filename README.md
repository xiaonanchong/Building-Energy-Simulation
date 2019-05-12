# Building-Energy-Simulation  

## Project Summary  

Building Energy Simulation through Deep Reinforcement Learning
Reinforcement learning has proved to be a successful optimization technique to find optimal behaviors in the absence of relevant data and learning for the experience.  
In this project, we propose to optimize and control dynamic power consumption in a building by means of Reinforcement learning techniques. To do so, we will rely on an existing testbed and will use different datasets.  

## Papers on 'Energy Control' and 'Deep Learning'     

[Building Energy Load Forecasting using Deep Neural Networks](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7793413) - using LSTM model to predict single room electricity consumtion in next 60 hours. different models are compared in cluding: standard LSTM, standard LSTM and delayed input, S2S model.  

[Intelligent Buildings of the Future Cyberaware, Deep Learning Powered, and Human Interacting](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7792825)  

[Reinforcement Learning Testbed for Power-Consumption Optimization](https://arxiv.org/pdf/1808.10427.pdf)  
TRPO - trust-region policy optimization algorithm  

[A review on optimized control systems for building energy andcomfort management of smart sustainable buildings](https://reader.elsevier.com/reader/sd/pii/S1364032114001889?token=E1802E55E595AC95AD959F51EB046249CE72155E2C9E31CD5A2CD3E1E4B5BFDCEE20E324124011ED90B93313694CE75A)- Model Predictive Control (MPC)  

[Demand reduction in building energy systems based on economic model predictive control](https://www.sciencedirect.com/science/article/pii/S0009250911005240)  

[Reinforcement learning for energy conservation and comfort in buildings](https://www.sciencedirect.com/science/article/pii/S0360132306001880)  

[Deep Reinforcement Learning for Building HVAC Control](https://ieeexplore.ieee.org/abstract/document/8060306)  

[Reinforcement Learning for Building Environmental Control ](https://mediatum.ub.tum.de/doc/1289297/file.pdf)  

[Advanced Building Control via Deep Reinforcement Learning](http://www.jinming.tech/papers/BuildingRL_ICAE_CR.pdf) - wrap EnergyPlus: no open source codes  

[Reinforcement learning for energy conservation and comfort in buildings](https://mediatum.ub.tum.de/doc/1289939/file.pdf)  

[A zone-level, building energy optimisation combining an artificial neural network, a genetic algorithm, and model predictive control](https://www.sciencedirect.com/science/article/pii/S036054421830522X#bib6)  

[A Long-Short Term Memory Recurrent Neural
Network Based Reinforcement Learning Controller
for Office Heating Ventilation and Air
Conditioning Systems](https://github.com/xiaonanchong/Building-Energy-Simulation/blob/master/A_Long-Short_Term_Memory_Recurrent_Neural_Network_.pdf)  

[PPT: Lighting/Daylighting Control and
Energy Study through EnergyPlus and
Matlab Co-simulation](https://www.ibpsa.us/sites/default/files/publications/SB10-PPT-IS08C-03-Wen.pdf) - configure MATLAB and EnergyPlus through BCVTB  

[vedio on EnergyPLus-CVBTB Co-simulation](https://www.youtube.com/watch?v=8kH8IxJrIU4)  

### Reinforcement Learning  
[Li FeiFei: reinforcement learning](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture14.pdf)

[Evolving simple programs for playing Atari games](https://arxiv.org/pdf/1806.05695.pdf) - evolutionary algorithm as an alternative to reinforcement learning  

[A Brief Survey of Deep Reinforcement Learning](https://spiral.imperial.ac.uk:8443/bitstream/10044/1/53340/2/1708.05866v1.pdf)  

[Trust Region Policy Optimization](https://arxiv.org/pdf/1502.05477.pdf) - reinforcement learning algorihtm used in [Reinforcement Learning Testbed for Power-Consumption Optimization](https://arxiv.org/pdf/1808.10427.pdf)   

[HIGH-DIMENSIONAL CONTINUOUS CONTROL USING GENERALIZED ADVANTAGE ESTIMATION](https://arxiv.org/pdf/1506.02438.pdf) - standardize returns  

[Gradient Estimation Using Stochastic Computation Graphs](https://arxiv.org/pdf/1506.05254.pdf) - hard attend and PG  

#### Reinforcement Learning Baselines Implementations:  
1, A2C-[Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/pdf/1602.01783.pdf)  
2, ACER-[Sample Efficient Actor-Critic with Experience Replay](https://arxiv.org/pdf/1611.01224.pdf)  
3, ACKTR-[Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation](https://arxiv.org/pdf/1708.05144.pdf)  
4, DDPG-[Continuous control with deep reinforcement learning](https://arxiv.org/pdf/1509.02971.pdf)  
> 'adapt the ideas underlying the success if Deep Q-Learning to the continuous action domain'  

5, DQN-[]()  
6, GAIL-[Generative Adversarial Imitation Learning](https://arxiv.org/pdf/1606.03476.pdf)  
> 'propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning'  

7, HER-[Hindsight Experience Replay](https://arxiv.org/pdf/1707.01495.pdf)  
8, __PPO__-[Proximal Policy Optimization Algorithms](https://arxiv.org/pdf/1707.06347.pdf)  
9, __TRPO__-[Trust Region Policy Optimization](https://arxiv.org/pdf/1502.05477.pdf)   

#### citation following  
TRPO -> [Approximately optimal approximate reinforcement learning](https://homes.cs.washington.edu/~sham/papers/rl/aoarl.pdf)  

#### suplyments  
[Fisher Matrix for Beginners](http://wittman.physics.ucdavis.edu/Fisher-matrix-guide.pdf)  
[A Natural Policy Gradient](https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf)  
[Actor-critic methods](http://mi.eng.cam.ac.uk/~mg436/LectureSlides/MLSALT7/L5.pdf)  
[Mastering the game of Go with deep neural networks and tree search](https://www.nature.com/articles/nature16961) (2016)  

### Deep Learning  
[Human-level control through deep reinforcement learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf) (DeepMind)  

[Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) (DeepMind 2013)  

[Blog: RL — DQN Deep Q-network](https://medium.com/@jonathan_hui/rl-dqn-deep-q-network-e207751f7ae4)  

### Energy Control  
[Blog: Why Energy Is A Big And Rapidly Growing Problem For Data Centers](https://www.forbes.com/sites/forbestechcouncil/2017/12/15/why-energy-is-a-big-and-rapidly-growing-problem-for-data-centers/#772cdb265a30)  
'AI is the future and its hungry for processing power'  

## Coding  
https://github.com/IBM/rl-testbed-for-energyplus   

[baselines](https://github.com/openai/baselines)  

### implementation  
[BCVTB-EnergyPlus-MATLAB 4.2](https://www.tandfonline.com/doi/full/10.1080/19401493.2010.518631?scroll=top&needAccess=true&#aHR0cHM6Ly93d3cudGFuZGZvbmxpbmUuY29tL2RvaS9wZGYvMTAuMTA4MC8xOTQwMTQ5My4yMDEwLjUxODYzMT9uZWVkQWNjZXNzPXRydWVAQEAw)  

[CO-SIMULATION FOR BUILDING CONTROLLER DEVELOPMENT: THE CASE STUDY OF A MODERN OFFICE BUILDING ](https://opticontrol.ee.ethz.ch/Lit/Sage_11_Proc-CISBAT11.pdf)  

[Tool coupling for the design and
operation of building energy and control
systems based on the Functional Mockup Interface standard](https://www.osti.gov/servlets/purl/1134244)  

[EnergyPlus external interface application guide](https://energyplus.net/sites/all/modules/custom/nrel_custom/pdfs/pdfs_v9.1.0/ExternalInterfacesApplicationGuide.pdf)  

## Data  
https://www.energycodes.gov/development/commercial/prototype_models  
