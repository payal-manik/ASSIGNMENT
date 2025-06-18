#  Demonstrate multiple inheritance in Python. 

class writer:
    def write(self):
        print("Writer writes books.")
        
class painter:
    def paint(self):
        print("Painter paints pictures.")
        
class person(writer,painter):
    def display(self):
        super().write()
        super().paint()
        print("I am creative.")
        
        
person1 = person()
person1.display()