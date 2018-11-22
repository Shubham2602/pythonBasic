class Person:
  def __init__(self):
    print("INITIAL FUNCTION")
  def setName(self,firstName,lastName):
    self.firstName = firstName;
    self.lastName = lastName;
  def printName(self):
    print(self.firstName ," ", self.lastName);

personName = Person()
personName.setName("Shubham","Routh");
personName.printName();
  
