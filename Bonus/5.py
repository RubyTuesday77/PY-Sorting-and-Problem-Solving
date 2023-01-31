#5: Write an algorithm that takes in an unsorted integer array and finds a pair with a given sum.
    #For example, for input: [5, 10, 4, 7, 6, 2] and target = 9, the output would be 7, 2.
    #If there are no pairs with sum equal to the target number, then the output should be 'no pairs sum to the target'.

def find_pair(lst, target):
    #Sort the list in ascending order.
    sorted_list = sorted(lst)

    #Set a variable called left equal to 0 and another variable called right equal to one less than the length of the list.
    #These variables should be initially set to the indices for the first and last element in the list.
    left = 0
    right = len(sorted_list) - 1

    #Write a while loop that runs the following code when left is less than right.
    while left < right:

        #If the value of the element at index or left plus the value of the element at index or right equals the target number, then print the pair and return.
        if sorted_list[left] + sorted_list[right] == target:
            return(sorted_list[left], sorted_list[right])

        #If the sum of the two elements is less than the target number, then increment left by 1.
        if sorted_list[left] + sorted_list[right] < target:
            left += 1
        
        #Otherwise, increment right by 1.
        else:
            right -= 1

    #Print 'no pairs sum to the target' if no two numbers sum to the target number.
    return('no pairs sum to the target')

# Test code:
lst = [8, 5, 7, 6, 2]
target = 15
print(find_pair(lst, target))
