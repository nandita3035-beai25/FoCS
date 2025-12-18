def count_number(num):
    even=0
    odd=0
    for i in num:
        if i%2==0:
            even+=1
        elif i%2!=0:
            odd+=1
    return (f"Even count:{even}, Odd count:{odd}")
nums=eval(input("Enter list of numbers:"))
print(count_number(nums))
