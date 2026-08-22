'''import keyword
print(keyword.kwlist)

print("Hello Python")
# Day 2 - Variables+Data Types

x='charan'


print(x[::-1])  # Reverse the string

print(x[0:int(len(x)/2)]+
      x[int(len(x)):int(len(x)/2)-1:-1])  # Reverse the string from the middle


ls=list(map(int, input("Enter the numbers: ").split()))
dc={"charan":23, "sai":24, "kumar":25}
dc["ramya"]=26
dc["kiran"]=27
print(ls)
print(dc)'''
x,y=map(int,input("Enter the numbers: ").split())
nums=list(range(0,2001,2))
n=sum(nums[x:y+1])
print(n)