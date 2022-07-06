import numpy as np



def top(y,x):
    if y == 0:
        y
    else:
        y = y-1
    return y, x

def below(y,x):
    if y == M-1:
        y
    else:
        y = y+1
    return y,x  # XXX:

def left (y,x):
    if x == 0:
        x
    else:
        x = x-1
    return y, x

def right(y,x):
    if x == N-1:
        x
    else:
        x = x+1
    return y, x

def reaction(incoming, present):
    if incoming == 2 and present == 1:
        present = 2
    else:
        present
    return present

def action(A, y, x, B):
    incoming = A[y][x]
    if incoming == 2:
        valid_directions = [(y_next, x_next) for (y_next,x_next) in [top(y,x), right(y,x), below(y,x),left(y,x)] if (y_next, x_next) != (y, x)]
        for (y_next,x_next) in valid_directions:

            present = A[y_next][x_next]
            B[y_next][x_next] = reaction(incoming, present)
    else:
        pass

    return B

def execute_one_time_unit(A, M, N, B):
    for y in range(M):
        for x in range(N):
            # new_matrix is only used for the update
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
    B = A.copy()

    M,N = np.shape(A)

    output = ultimate(A,M,N,B)
    print(output)
