class Tables:
  num=1
  def getData(self):
    num=int(input("Enter the number for which u want table : "))
    table1.calculate(num)
  def calculate(self,num):
    for i in range(1,11):
      print(num, " * ",i," = ",(num*i))

table1 = Tables()
table1.getData()

      
    
