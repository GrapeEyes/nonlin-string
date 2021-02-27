

"""This class should create a basic string object that can be set up, excited, evolve and output audio.
Many of the funcionality probably will have to be moved to a base string class later on.
Initial iteration using hardcoded raised cosine initialisation and fixed (Dirichlet) boundary conditions"""

import numpy as np


def raised_cosine(x,centre=0.5, halfwidth=0.1):
    """Defined only for [0,1]"""
    ind = np.sign(np.max(np.append(-(x-centre-halfwidth/2)*(x-centre+halfwidth/2),0)))
    rc = 0.5*ind*(1+np.cos(2*np.pi*(x-centre)/halfwidth))

    return rc


class StringLinearElasticNoLoss:

    def __init__(self, sampling_rate, frequency_fundamental):
        
        # self.length = length
        # self.tension = tension
        self.sampling_rate = sampling_rate
        self.frequency_fundamental = frequency_fundamental
        
        self.gamma = 2*self.frequency_fundamental
        self.timestep = 1/self.sampling_rate

        lambda_ = 1 # Can play with it for numerical dispersion

        gridstep = self.gamma*self.timestep/lambda_
        self.N = np.floor(1/gridstep) # Number of gridpoints
        self.gridstep = 1/self.N 
        self.lambda_ = self.gamma*self.timestep/self.gridstep
        self.grid = np.linspace(0,1,int(self.N)+1)

    def initialize_displacement(self):
        pass

    def define_grid(self):
        pass

    def compute_next_sample(self):
        pass

    def 
        