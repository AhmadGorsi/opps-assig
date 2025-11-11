class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
    def average(self):
        return self.mark1+self.mark2/2
std = student('Ahmad',66,88)
print()

      
        