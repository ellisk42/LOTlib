from copy import copy, deepcopy
import numpy
from Hypothesis import Hypothesis


class VectorHypothesis(Hypothesis):
    """Store n-dimensional vectors (defaultly with Gaussian proposals)."""

    def __init__(self, value=None, n=1, proposal=numpy.eye(1)):
        if value is None:
            value = numpy.random.multivariate_normal(numpy.array([0.0]*n), proposal)
        Hypothesis.__init__(self, value=value)
        self.n = n
        self.proposal = proposal
        self.__dict__.update(locals())

    def propose(self):
        ## NOTE: Does not copy proposal
        newv = numpy.random.multivariate_normal(self.value, self.proposal)
        return VectorHypothesis(value=newv, n=self.n, proposal=self.proposal), 0.0  # symmetric proposals
