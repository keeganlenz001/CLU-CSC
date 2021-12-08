with open("Random-_1_-100_-Sheet1.txt", "r") as infile:
    nums = infile.readlines()
    arr1 = []
    arr2 = []
    for i in range(len(nums)):
        if i < (len(nums) / 2):
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])
