nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

index = 0
while index <= len(nums) - 1 :
    if(nums[index] == x):
        print("found at index :", index)
        break
    else:
        print("finding...")
    index += 1
    


'''
Search for a number x in this tuple using while loop
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
'''