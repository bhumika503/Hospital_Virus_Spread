from traverse import Traverse
import numpy as np


class ModelVirusSpread():

    def interaction(source, sink, count):
        # interaction b/w source ward and sink ward
        # source: state of the source ward
        # sink: state of the ward towards which the virus is directed.
        # 0,1,2 are various states of wards
        # count: # of interactions between infected and uninfected ward.

        if source == 2 and sink == 1:
            sink = 2
            count +=1
        else: # no interaction when sink == 2 | sink == 0
            sink
        return sink, count

    def action(A, y, x, B, count):
        # models the spread of virus
        # stores the updated state of the sink ward after virus spread
        M,N = np.shape(A)

        # identify source
        source = A[y][x]

        # virus only spreads from ward with state 2
        if source == 2:
            valid_directions = Traverse.valid_traversals(y,x,M,N)
            for (y_next,x_next) in valid_directions:
                sink = A[y_next][x_next]
                B[y_next][x_next], count = ModelVirusSpread.interaction(source, sink, count)
        else: # alternate source
            pass

        return B, count

    def execute_one_time_unit(A, M, N, B):
        # count: # of interactions between infected and uninfected ward.
        # A: static state of the hospital at start of each time unit
        # B: intermediate dynamic state of hospital during and end of time unit.
        count = 0
        for y in range(M):
            for x in range(N):
                B, count = ModelVirusSpread.action(A, y, x, B, count)
        return B, count
