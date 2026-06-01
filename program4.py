x=[]
for i in range(5):
    y =int(input("Enter marks:"))
    x.append(y)
print(x)
print(max(x))
print(min(x))
print(sum(x))
for z in x:
    if z >= 30:
      print("Student passes")