### Shift Function
# With direction param 'left' or 'right'
def reverse_list(lst, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1

    if low < 0 or high >= len(lst) or low > high:
        return lst

    while low < high:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1

def shift (lst, k, direction = 'left'):
    n = len(lst)
    if n == 0:
        return lst
    if direction == 'left':
        reverse_list(lst, 0, k - 1)
        reverse_list(lst, k, n - 1)
        reverse_list(lst)
    elif direction == 'right':
        reverse_list(lst)
        reverse_list(lst, 0, k - 1)
        reverse_list(lst, k, n - 1)
    else:
        raise ValueError("direction must be 'left' or 'right'")
    return lst

lst1 = [1,2,3,4,5,6,7,8,9]
shift (lst1, 4, direction='right')
print(lst1)
lst2 = [1,2,3,4,5,6,7,8,9]
shift (lst2, 4)
print(lst2)
#
# Right desired output: 45123
# left desired output: 34512
lst5 = [11,12,13,14,15,16,17,18,19,20]
reverse_list(lst5, 4,10)
print(lst5)

lst4 = [1,2,3,4,5,6,7,8,9]
reverse_list(lst4,1,4)
print(lst4)