import numpy as np

from model_virus import ModelVirusSpread


def ultimate(A,M,N,B):
    time_counter = 0
    while True:
        if list(zip(*np.where(np.array(B) == 1))):
            # if any unifected ward remains

            B, count = ModelVirusSpread.execute_one_time_unit(A,M,N,B)

            time_counter += 1
            print('count', count)
            print(time_counter)

            if count == 0:
                # count 0 -> if no change in A and B after interaction
                return -1
            else:
                # Update the state after one time unit
                A = B.copy()
                continue

        else:
            return time_counter

# m = 3 # no: of rows
# n = 4 # no: of columns
if __name__ == '__main__':
    # A = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]
    # B = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]

    # A: Original state
    A = np.random.randint(3, size=(1000, 1000))

    # B: Transient state used to update the matrix after virus interactions.
    B = A.copy()

    M,N = np.shape(A)

    output = ultimate(A,M,N,B)
    print(output)
