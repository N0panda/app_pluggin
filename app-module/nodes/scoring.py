from timeflux.core.node import Node
import pandas as pd
import numpy as np

class Scoring(Node):
    """ --( note a ajouter )--

        Attributes:
        i (Port): Default input, expects DataFrame.
        o (Port): Default output, provides DataFrame.

    """
    def __init__(self, w_delta=0., w_theta=0., w_alpha=0., w_beta=0., w_gamma=0.):
        """ Weight for each waves """
        self.w_delta = w_delta   #"(float)"
        self.w_theta = w_theta   #"(float)"
        self.w_alpha = w_alpha   #"(float)"
        self.w_beta = w_beta     #"(float)"
        self.w_gamma = w_gamma   #"(float)"

    def update(self):
        if not self.i.ready():
            return
        print(type(self.i.data))

