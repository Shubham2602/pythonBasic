class Human:
  def __init__(self,n,o):
    self.name = n;
    self.occupation =o;

  def does_work(self):
    if self.occupation == "tennis player":
      print(self.name, " plays tennis.")
    elif self.occupation == "actor":
      print(self.name, " shoots movies")

  def speaks(self):
    print(self.name, " is stupd")

tom = Human("Tom Cruise","actor")
maria = Human("Maria Sharapova","tennis player")

x=int(input("Enter option (1/2) : "))
if x==1:
  tom.does_work()
  tom.speaks()
elif x==2:
  maria.does_work()
  maria.speaks()
