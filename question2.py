def checkAvailability(intervals):
    #loop through the array of intervals getting the start and end time of each
    for index, interval in enumerate(intervals):
        start_time = interval[0]
        end_time = interval[1]

        #get a list of previous items in the intervals array 
        # and check whether they overlap with the current interval
        previous_intervals = intervals[:index]

        for previous_index, previous_interval in enumerate(previous_intervals):
            previous_start_time = previous_interval[0]
            previous_end_time = previous_interval[1]

            #if the current interval starts before a previous interval ends 
            #then it overlaps
            if start_time < previous_end_time and previous_start_time < end_time:
                return False, [intervals[previous_index], intervals[index]]
    
    #if no intervals overlap, return true
    return True,[]

#Executing the function with an overlapping and a non overlapping list of intervals
overlapping_intervals = [[1,2],[2,5],[5,8]]
non_overlapping_intervals = [[6,7],[2,7],[8,12]]

print("Executing with list ", overlapping_intervals)
isAvailable, intervals = checkAvailability(overlapping_intervals)

if isAvailable:
    print("The intervals do not overlap")
else:
    print("There are overlapping intervals ", intervals)

print("Executing with list ", non_overlapping_intervals)
isAvailable, intervals = checkAvailability(non_overlapping_intervals)

if isAvailable:
    print("The intervals do not overlap")
else:
    print("There are overlapping intervals ", intervals)

# print(checkAvailability(overlapping_intervals))
# print("")
# print(checkAvailability(non_overlapping_intervals))