"""
Find N best number game hypotheses.

"""
from LOTlib.FiniteBestSet import FiniteBestSet
from LOTlib.Inference.MetropolisHastings import MHSampler
from LOTlib.Inference.PriorSample import prior_sample
from Model import *

# Global parameters for inference
domain = 100
alpha = 0.9
num_iters = 10000
N = 10
h0 = make_h0(grammar=grammar, alpha=alpha)
demo_data = [2, 4, 8, 16, 32, 64]


#=============================================================================================================

if __name__ == "__main__":

    prior_sampler = prior_sample(h0, demo_data, num_iters)
    mh_sampler = MHSampler(h0, demo_data, num_iters)

    hypos = [h for h in prior_sampler]
    for h in hypos:
        h.compute_posterior([8])

    hypos = sorted(set(hypos), key=lambda x: x.posterior_score)
    for h in hypos[-10:]:
        print str(h), h.posterior_score, h.likelihood, h.prior
    # hypotheses = FiniteBestSet(generator=prior_sampler, N=N, key="posterior_score")
    # for h in hypotheses:
    #     print str(h), h.posterior_score

