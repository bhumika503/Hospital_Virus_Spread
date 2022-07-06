import numpy as np

from traverse import Traverse


def interaction(source, sink):
    # interaction b/w source ward and sink ward
    if source == 2 and sink == 1:
        sink = 2
    else: # no interaction when sink == 2 | sink == 0
        sink
    return sink

def action(A, y, x, B):

    # identify source
    source = A[y][x]

    # virus only spreads from source == 2
    if source == 2:
        valid_directions = Traverse.valid_traversals(y,x,M,N)
        for (y_next,x_next) in valid_directions:
            sink = A[y_next][x_next]
            B[y_next][x_next] = interaction(source, sink)
    else: # alternate source
        pass

    return B

def execute_one_time_unit(A, M, N, B):
    for y in range(M):
        for x in range(N):
            B = action(A, y, x, B)
    return B

def ultimate(A,M,N,B):
        TIME_COUNTER = 0
        while True:
            if list(zip(*np.where(np.array(B) == 1))):


                B = execute_one_time_unit(A,M,N,B)

                TIME_COUNTER += 1


                if np.array_equiv(A,B):
                    print(TIME_COUNTER)
                    return -1
                else:
                    A = B.copy()
                    continue

            else:
                return TIME_COUNTER

# m = 3 # no: of rows
# n = 4 # no: of columns
if __name__ == '__main__':
    # A = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]
    # B = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]

    A = np.random.randint(3, size=(1000, 1000))

    # new_matrix is only used for the update
    B = A.copy()

    M,N = np.shape(A)

    output = ultimate(A,M,N,B)
    print(output)
