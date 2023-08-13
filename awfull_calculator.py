#function that makes easy math
import sys

def calculator():
    print("Welcome to the world's worst calculator: only acepts 2 numbers:\n")
    print("Write CLOSE to close.")
    n1 = input("Insert number:  ")
    if n1 == "c" or n1 == "CLOSE" or n1 == "close":
      exit()
    oper = input("Insert operation symbol:  ")
    n2 = input("Insert number:  ")
    total = 0  
    if oper == "+":
      total = int(n1)+int(n2)
    elif oper == "-":
      total = int(n1)-int(n2)
    elif oper == "*":
      total = int(n1)*int(n2)
    elif oper == "/" and n2 == "0":
      print("You can't divide by 0, you silly.")
    elif oper == "/":
      total = int(n1)/int(n2)
    else:
      print("Something is wrong...")
    return print("TOTAL: {}\n".format(total))
    
def main():
  while True:
    #call the function and make it in a loop
    calculator()
    print("\n ------------ \n")

    
if __name__ == "__main__":
  main()
