# # numbers=[1,2,3,4,5,6,7,8,9]
# # print(numbers)
# # for i in numbers
# # print(i)

# # for i in range(0,10,3):
# #   print(i)

# # # #
# # import random
# # print("think any secret number between 1 to 10!")
# # user_input= int(input("Enter the secret number(computer guess the number):"))

# # computer_num =  random.randint(1,10)
# # print(f"first guess of computer:{computer_num}")

# # while True:
# #  feedback= input("is this guess right?(greater/lesser/right):")

# # if feedback == "right":
# #    print("yes! computer has guess correctly")
# #    break;
# # elif feedback == "lesser":
# #     print("Too low..")
# # elif feedback == "greater":
# #     print("Too high..")
# # else:
# #   print("wrong input! only 'greater','lesser',or 'right'.")
# #    continue
# # computer_num = random.randint(1,10)
# # print(f"new guess of computrer: {computer_num}")

# import random

# print("Think of a secret number between 1 to 10!")
# user_input = int(input("Enter the secret number (computer will guess the number): "))

# computer_num = random.randint(1, 10)
# print(f"First guess of the computer: {computer_num}")

# while True:
#     feedback = input("Is this guess right? (greater/lesser/right): ").strip().lower()

#     if feedback == "right":
#         print("Yes! The computer has guessed correctly.")
#         break
#     elif feedback == "lesser":
#         print("Too low..")
#     elif feedback == "greater":
#         print("Too high..")
#     else:
#         print("Wrong input! Only 'greater', 'lesser', or 'right' are allowed.")
#         continue  # This helps restart the loop if input is invalid

#     computer_num = random.randint(1, 10)
#     print(f"New guess of the computer: {computer_num}")
# import streamlit as st
# import random 

# st.title("Number Guessing Game")
# Random_Number_Generating= random.randint(1,3)

# User_Input= st.number_input("Write your number",min_value=1,max_value= 3)
# User_selectbox =st.selectbox("Choose",[1,2,3])

# if st.button("Submit"):
#     if User_Input < Random_Number_Generating:
#         st.warning("least number has been selected it  should be greater number")
#     elif  User_Input > Random_Number_Generating:
#          st.warning("This time greater number has been selected it  should be lesser number")
#     else :
#         st.sucess("You won the game")
# import streamlit as st
# import random 

# st.title("Number Guessing Game")

# # Generate a random number between 1 and 3
# random_number = random.randint(1, 3)

# # Get user input
# user_input = st.number_input("Choose a number", min_value=1, max_value=3, step=1)

# if st.button("Submit"):
#     if user_input < random_number:
#         st.warning("Too low! Try a higher number.")
#     elif user_input > random_number:
#         st.warning("Too high! Try a lower number.")
#     else:
#         st.success("You won the game! 🎉")

import streamlit as st
import random 
st.title("This my number guessing game")

Random_Number_Generate_do= random.randint(1,5)

User_Input_box = st.number_input("Write Your Number",min_value=1,max_value=5)

if st.button("Check it"):
    if User_Input_box == Random_Number_Generate_do:
        st.success("Congragulations you won" )
    else:
        st.warning("You lost the game,please try again")