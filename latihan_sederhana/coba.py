def foo(x,y=0):
  if y == 0:
    return x 
  else:
    return x + y  
print(foo(5))
print(foo(5,3))