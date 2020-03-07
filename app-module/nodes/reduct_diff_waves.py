from timeflux.core.node import Node
import numpy as np
import pandas as pd
import json

class Log_(Node):
    """ Do a the log() of each element in the Dataframe

    Attributes:
        i (Port): Default input,expects Dataframe.
        o (Port): Default output,expects Dataframe.

    """
    def update(self):
        if not self.i.ready():
            return
        self.o = np.log(self.i)
