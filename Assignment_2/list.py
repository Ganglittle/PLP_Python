# 1. Empty list
my_list = []

print ('Empty list: ', my_list)

# 2. Appending 10, 20,...
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print ('Actual list: ', my_list)

# 3. Adding 15 to the second place.
my_list.insert(1, 15)

print ('Updated list: ', my_list)

#4. Adding numbers with extend.
my_list.extend([50, 60, 70])

print ('Longer list: ', my_list)

# 5. Remove last number
my_list.pop()

print ('List less one: ', my_list)

# 6. Sort in ascending order
my_list.sort()

print ("Sorted list: ", my_list)

# 7. Find and print 30
index_of_30 = my_list.index(30)
print("Where's the 30? :", 'Position', index_of_30)

print("Final list:", my_list)
