
from random import randint, random
from LOTlib.Miscellaneous import Infinity
from MHShared import MH_acceptance
from MultipleChainMCMC import MultipleChainMCMC


class ParallelTemperingSampler(MultipleChainMCMC):
    """
    Parallel tempering. Here the temperatures *all* refer to likelihood_temperatures
    """

    def __init__(self, make_h0, data, steps=Infinity, temperatures=[1.0, 1.1, 1.5], within_steps=50, swaps=1, yield_only_t0=False, **kwargs):

        self.yield_only_t0 = yield_only_t0 #whether we yield all samples, or only from the lowest temperature
        self.within_steps = within_steps
        self.swaps = swaps

        assert 'nchains' not in kwargs

        MultipleChainMCMC.__init__(self, make_h0, data, nchains=len(temperatures), steps=steps, **kwargs)

        # and set the temperatures
        for i, t in enumerate(temperatures):
            self.chains[i].likelihood_temperature = t

    def ll_at_temperature(self, i, t):
        """ The posterior  of chain i at temperature t"""
        return self.chains[i].current_sample.likelihood / t

    def next(self):

        self.nsamples += 1

        self.chain_idx = (self.chain_idx+1) % self.nchains

        if self.nsamples % self.within_steps == 0:

            for _ in xrange(self.swaps):
                i = randint(0, self.nchains-2)

                # the priors cancel, so this represents the posterior
                cur  = self.ll_at_temperature(i, self.chains[i].likelihood_temperature) + self.ll_at_temperature(i+1,   self.chains[i+1].likelihood_temperature)
                prop = self.ll_at_temperature(i, self.chains[i+1].likelihood_temperature) + self.ll_at_temperature(i+1, self.chains[i].likelihood_temperature)

                if MH_acceptance(cur, prop, 0.0):
                    tmp = self.chains[i].current_sample
                    self.chains[i].set_state(self.chains[i+1].current_sample, False)
                    self.chains[i+1].set_state(tmp, False)

                    # OLD: self.chains[i].current_sample, self.chains[i+1].current_sample = self.chains[i+1].current_sample, self.chains[i].current_sample

        if self.yield_only_t0 and self.chain_idx != 0:
            return self.next() # keep going until we're on the one we yield
            ## TODO: FIX THIS SINCE IT WILL BREAK FOR HUGE NUMBERS OF CHAINS
        else:
            return self.chains[self.chain_idx].next()


if __name__ == "__main__":

    from LOTlib import lot_iter
    from LOTlib.Miscellaneous import Infinity
    from LOTlib.Examples.Number.Model import generate_data, NumberExpression, grammar
    data = generate_data(300)

    make_h0 = lambda : NumberExpression(grammar)

    cnt = 0
    for h in lot_iter(ParallelTemperingSampler(make_h0, data, steps=1000, yield_only_t0=True)):
        print h.posterior_score, h
        cnt += 1

    print cnt