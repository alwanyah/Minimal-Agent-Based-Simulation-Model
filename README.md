# Embodied Dyadic Interaction Increases Complexity of Neural Dynamics: A Minimal Agent-Based Simulation Model


#TODO 

-how to connect RNN output to webots
    -motor output 
        [float] between 0.0 and 1.0 for left and right weel, just going forward
    -sound output
        1 sound emiter, decays linear with distance
        dont know

-connect webot output to RNN
    -2 microphone inputs
    -microphones at 90° angle 
        [float] between 0.0 and 1.0 for left and right microphone, just intensity?




# overall goal
-train 2 interactive agents that achieve similar entropy to ~0.8
-record both behaviours and train multiple agents on each ghost interactively


# what to optimmize

100 times:
-96 solutions * 500 generations

optimze with evolutanary algorithm:
-weights and signs of the connections
-biases
-time-constants

evaluation:
-computed the entropy of the time series of neural activity taken from simulated trials.

This measure allowed us to operationalize the complexity
of internal neural dynamics exhibited by each agent in
various interaction conditions. In particular, neural entropy was
measured for each agent in trials where they were evolved
and interacted in pairs.