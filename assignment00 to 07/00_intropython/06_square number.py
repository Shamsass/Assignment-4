def main():
    
     number= float(input(" \033[1;3m Type a number to see it's square: \033[0m"))
     
     square = number * number

     print(f"\033[1;3m the square of {number} is {square} \033[0m")

if __name__== "__main__":
 main()