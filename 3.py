#3: Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list in descending order (use the sorted() function).
    #The sorted() function sorts in ascending order, but it can sort in descending order by adding a reverse parameter with a boolean value of True.
unsorted_list = [7, 2, 9, 1, 0]
sorted_list = sorted(unsorted_list, reverse = True)

print(sorted_list)