
class prson:
    name = ""
#   age
    def __init__(self,nameS):
       self.name = nameS
    def sey(self,xx):
        print("shuo :{0}".format(xx))
    def interDusc(self):
        print("my name is {0}".format(self.name))
#    test():
#    print("text")

p = prson("y")

p.sey("ca")

p.interDusc()




class simth(prson):
    fistName = "simth"
    allName = ""

    def __init__(self,name1,frist):
       prson.__init__(self,name1)
       self.allName = frist
    def interDusc(self):
        print("my name is simth {0}--{1}".format(self.name,self.allName))

sp = simth("y","made")
sp.sey("hh")
sp.interDusc()