import numpy as np

from model_virus import ModelVirusSpread


def calculate_min_time(A,M,N,B):
    # A: static state of the hospital at start of each time unit
    # B: intermediate dynamic state of hospital during and end of time unit.
    time_counter = 0
    while True:
        if list(zip(*np.where(np.array(B) == 1))):
        # if any unifected ward remains

            B, count = ModelVirusSpread.execute_one_time_unit(A,M,N,B)

            time_counter += 1
            # print('count', count)
            # print(time_counter)

            if count == 0:
            # if count== 0: no change in A and B after virus spread modelling
                return str(-1)
            else:
                # Update the state after one time unit
                A = B.copy()
                continue

        else:
            return str(time_counter)

def text2matrix(txt, r,c):
    # txt = "[[5, 3, 4], [1, 5, 8]]"
    x = txt.replace(".",'').replace("[",'').replace("]",'').replace(",",'').replace(' ','')
    list_a = [int(i) for i in x]
    array = np.reshape(list_a, (r,c))
    return array


if __name__ == '__main__':

    # 1. Input the rows and columns of the hospital
    # Example Input: 3,5
    r, c = input('Input # rows and #columns :').split(',')

    M = int(r)
    N = int(c)

    # 2. A: 2-D array and initial state
    # Example input: [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]
    matrix_str = input('Input the 2-D array :')
    A = text2matrix(matrix_str, M, N)

    # # other options for inputs
    # # Construct random matrix
    # A = np.random.randint(3, size=(M, N))

    # # Input example from pdf
    # A = [[2,1,0,2,1],[1,1,1,1,1],[1,0,0,2,1]]

    # B: Transient state used to update the matrix after virus interactions.
    B = A.copy()

    # M,N = np.shape(A)

    output = calculate_min_time(A,M,N,B)
    print(output)
