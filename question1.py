import numpy as np

#generate a list of 10 between 1 and 100 random integers
array = np.random.randint(1, 101, 10)
print("The list of items is : ", array)

#define the function to find the maximum average
def max_average(the_array):
    #if only 1 element in the list, return 0 as we need 2 contiguos elements
    if len(the_array) == 1:
        return 0, [0]
    
    #if only 2 elements in the list, return their average and a list of the 2 elements
    if len(the_array) == 2:
        return sum(the_array) / 2, [the_array[0], the_array[1]]

    #split the list into 2 and recursively execute the function on the 2 sublists
    mid_point = len(the_array) // 2
    left_subarray = the_array[:mid_point]
    right_subarray = the_array[mid_point:]

    max_average_left, left_elements = max_average(left_subarray)
    max_average_right, right_elements = max_average(right_subarray)

    #find the average of the boundary elements incase they have the greatest average
    mid_point_average, mid_point_elements = (the_array[mid_point-1] + the_array[mid_point])/2, [the_array[mid_point-1], the_array[mid_point]]

    #compare the max averages of the left sublist, right sublist and boundary elements 
    # and return the greatest of them together with the elements that give the average
    if max_average_left > max_average_right:
        if max_average_left > mid_point_average:
            return max_average_left, left_elements
        else:
            return mid_point_average, mid_point_elements
    else:
        if max_average_right > mid_point_average:
            return max_average_right, right_elements
        else:
            return mid_point_average, mid_point_elements

#execute the function and print the results
average, indexes = max_average(array)
print("The largest average is:  ",average)
print("The items with the largest average are : ", indexes)