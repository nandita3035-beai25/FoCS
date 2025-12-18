def remove_duplicates(nums):
    list1=[]
    for i in nums:
        if i not in list1:
            list1.append(i)
    return list1
num_list=eval(input("Enter numbers in a list:"))
print(remove_duplicates(num_list))