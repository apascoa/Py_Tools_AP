#Work By APascoa
#https://github.com/apascoa/

#test
def test():
    print("Working")

#Square_title
def square_title(text):
    largura = len(text)+4
    print("┏",(largura-2)*"-","┓\n| ",text," |\n┗",(largura-2)*"-","┛", sep="")

#Underline
def underline(text):
    print(len(text)*"-")
