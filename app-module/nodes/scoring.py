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
        self.weight = np.array(w_delta, w_theta, w_alpha, w_beta, w_gamma)
        self.w_delta = w_delta   #"(float)"
        self.w_theta = w_theta   #"(float)"
        self.w_alpha = w_alpha   #"(float)"
        self.w_beta = w_beta     #"(float)"
        self.w_gamma = w_gamma   #"(float)"

    def update(self):
        if not self.i.ready():
            return
        data = self.i.data
        delta = data['A1_delta'].values[0]
        theta = data['A1_theta'].values[0]
        alpha = data['A1_alpha'].values[0]
        beta = data['A1_beta'].values[0]
        gamma = data['A1_gamma'].values[0]
        waves = np.array(delta, theta, alpha, beta, gamma)
        sum_ = np.sum(tab)
        score = 0
        for i in range(len(tab)):
            score += (waves[i] / sum_) * self.weight[i]
        self.o.data = score

