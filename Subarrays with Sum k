# Function to find sublists with given sum in a list
def printallSublists(A, sum):
 
    # create a dict for storing end index of all sublists with
    # sum of elements so far
    dict = {}
 
    # To handle the case when the sublist with given sum starts
    # from 0th index
    dict.setdefault(0, []).append(-1)
 
    sum_so_far = 0
 
    # traverse the given list
    for index in range(len(A)):
 
        # sum of elements so far
        sum_so_far += A[index]
 
        # check if there exists at-least one sub-list with given sum
        if (sum_so_far - sum) in dict:
            list = dict.get(sum_so_far - sum)
            for value in list:
                print(A[value+1: index+1])
 
        # insert (sum so far, current index) pair into the dict
        dict.setdefault(sum_so_far, []).append(index)
 
 
if __name__ == '__main__':
 
    A = [3, 4, -7, 1, 3, 3, 1, -4]
    sum = 7
 
    printallSublists(A, sum)
