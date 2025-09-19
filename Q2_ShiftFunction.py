### Shift Function
# With direction param 'left' or 'right'
def shift (lst, k, direction = 'left'):
    N = len(lst)
    if direction == 'left':
        for i in range(0,k):
            lst.append(lst[i]) # add first k terms to end of lst

        for i in range(0, k):
            lst.remove(lst[0]) # remove first item k times

    elif (direction == 'right'):

        for i in range(0, N-k):
            lst.append(lst[i])  # add first (N-k) terms to end of lst

        for i in range(0, N-k):
            lst.remove(lst[0])  # remove first item (N-k) times
        return lst




### Test Code
lst = [1,2,3,4,5,6]
shift(lst, 2)
print(lst) # Expected o/p: [3,4,5,6,1,2]

lst = [1,2,3,4,5,6]
shift(lst, 2, 'right')
print(lst) # Expected o/p: [5,6,1,2,3,4]