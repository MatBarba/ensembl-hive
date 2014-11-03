
from HiveRunnable import Process

import sys
import json
import numbers
import warnings

class TestRunnable(Process):

    def param_defaults(self):
        return {
            'pdef' : 78
        }

    def fetch_input(self):
        self.warning("Fetch the world !")
        print("alpha is", self.param('alpha'))
        self.param('new_param', 999)

    def run(self):
        self.warning("Run the world !")
        print("beta is", self.param_required('beta'))
        print("new_param is", self.param('new_param'))

    def write_output(self):
        self.warning("Write to the world !")
        print("gamma is", self.param('gamma'))
