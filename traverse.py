
class Traverse:
    # traverse in top,right,bottom,left direction
    # relative to current position in 2D Array
    def top(y,x,M,N):
        # Prevent top traversals for first row
        if y == 0:
            y
        else:
            y = y-1
        return y, x

    def below(y,x,M,N):
        # Prevent the bottom traversals for last row
        if y == M-1:
            y
        else:
            y = y+1
        return y,x

    def left (y,x,M,N):
        # Prevent left traversals for first column
        if x == 0:
            x
        else:
            x = x-1
        return y, x

    def right(y,x,M,N):
        # Prevent the right traversals for last column
        if x == N-1:
            x
        else:
            x = x+1
        return y, x

    def valid_traversals(y,x,M,N):

        # exclude the traversals which result in same coordinates as starting point
        return [(y_next, x_next) for (y_next,x_next) in [Traverse.top(y,x,M,N), Traverse.right(y,x,M,N), Traverse.below(y,x,M,N),Traverse.left(y,x,M,N)] if (y_next, x_next) != (y, x)]
