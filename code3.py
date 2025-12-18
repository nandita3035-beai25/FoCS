def list_sorting(nums):
    nums.sort()
    print("Ascending order:", nums)
    nums.sort(reverse=True)
    print("Descending order:", nums)
list1=eval(input("Enter numbers:"))
list_sorting(list1)