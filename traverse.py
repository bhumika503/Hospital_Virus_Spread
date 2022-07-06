
class Traverse:
    # traverse in top,right,bottom,left direction
    # relative to current position in 2D Array
    def top(y,x,M,N):
        if y == 0:
            y
        else:
            y = y-1
        return y, x

    def below(y,x,M,N):
        if y == M-1:
            y
        else:
            y = y+1
        return y,x

    def left (y,x,M,N):
        if x == 0:
            x
        else:
            x = x-1
        return y, x

    def right(y,x,M,N):
        if x == N-1:
            x
        else:
            x = x+1
        return y, x
