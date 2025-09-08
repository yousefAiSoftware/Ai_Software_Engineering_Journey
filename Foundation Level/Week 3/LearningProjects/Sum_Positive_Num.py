print("Welcome to our Summation numbers app...")
nums = [5,-4,6,8,-7,7,-9,3,-1,8,-5,4]
snum = 0
for num in nums:
    if num > 0:
        snum += num
print(f"The sum of nums is : {snum}")