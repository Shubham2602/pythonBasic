def fiboseries(c,d):
  a,b = 0,1
  for value in range(c,d):
    print(a)
    c=a+b
    a=b
    b=c

fiboseries(0,10)
  
  
