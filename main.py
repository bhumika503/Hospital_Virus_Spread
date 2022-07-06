import numpy as np

from model_virus import ModelVirusSpread


def calculate_min_time(A,M,N,B):

    time_counter = 0
    while True:
        if list(zip(*np.where(np.array(B) == 1))):
        # if any unifected ward remains

            B, count = ModelVirusSpread.execute_one_time_unit(A,M,N,B)

            time_counter += 1
            # print('count', count)
            # print(time_counter)

            if count == 0:
            # count 0 -> if no change in A and B after interaction
                return -1
            else:
                # Update the state after one time unit
                A = B.copy()
                continue

        else:
            return time_counter


if __name__ == '__main__':

    # Input the rows and columns of the hospital
    # Example Input: 3,3
    r, c = input('Input # rows and #columns :').split(',')

    rows = int(r)
    columns = int(c)

    # A: 2-D array
    # A: Initial State
    # Random matrix is constructed

    A = np.random.randint(3, size=(rows, columns))

    # B: Transient state used to update the matrix after virus interactions.
    B = A.copy()

    M,N = np.shape(A)

    # Input from pdf
    # A = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]
    # B = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]

    output = calculate_min_time(A,M,N,B)
    print(str(output))
