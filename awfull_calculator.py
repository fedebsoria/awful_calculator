#function that makes easy math
import sys

def calculator():
  while True:
    print("Welcome to the world's worst calculator: only acepts 2 numbers:\n")
    print("Write CLOSE to close.")
    n1 = input("Insert number:  ")
    oper = input("Insert operation symbol:  ")
    n2 = input("Insert number:  ")
    total = 0
    if n1 == "c" or n1 == "CLOSE" or "close":
      sys.exit()
    else:  
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
      return print(total)
    
def main():
  #call the function and make it in a loop
  calculator()
    
if __name__ == "__main__":
  main()
