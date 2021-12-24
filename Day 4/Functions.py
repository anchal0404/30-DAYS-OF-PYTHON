#1st
def func1(*args):
    for i in args:
        print(i)

func1('Anchal','Himanshu','Vikas',2002,2001,2000)
#2nd
def addition(num):
    if num:
       return num + addition(num - 1)
    else:
        return 0

result = addition(10)
print(result)
#3rd 
x = [56,77,64,98,23,73]
print(min(x))
#4th
def res(k):
  if(k > 0):
    result = k + res(k - 1)
    print(result)
  else:
    result = 0
  return result
res(6)