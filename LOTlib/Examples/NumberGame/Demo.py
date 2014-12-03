"""
Find N best number game hypotheses.

"""
from LOTlib import lot_iter
from LOTlib.FiniteBestSet import FiniteBestSet
from LOTlib.Inference.MetropolisHastings import MHSampler
from LOTlib.Inference.PriorSample import prior_sample
from Model import *

# Global parameters for inference
domain = 100
alpha = 0.99
num_iters = 1000000
N = 10
h0 = make_h0(grammar=grammar, domain=domain, alpha=alpha)
# demo_data = [2, 4, 8, 16, 32, 32, 64, 64]
demo_data = [1, 3, 7, 15, 31, 31, 63, 63]


#=============================================================================================================

if __name__ == "__main__":

    prior_sampler = prior_sample(h0, demo_data, num_iters)
    mh_sampler = MHSampler(h0, demo_data, num_iters)

    hypotheses = set()
    for h in lot_iter(prior_sampler):
        hypotheses.add(h)

    hypos = sorted(hypotheses, key=lambda x: x.posterior_score)
    for h in hypos[-10:]:
        print str(h)
        print h.prior, h.likelihood, h.posterior_score
    # hypotheses = FiniteBestSet(generator=prior_sampler, N=N, key="posterior_score")
    # for h in hypotheses:
    #     print str(h), h.posterior_score

