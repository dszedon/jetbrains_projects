from random import randrange

win_book = {"user":0, "robot":0, "draw":0}
    

def check_user(user):
    if user == "exit game":
        return "quit"
    else:
        try:
            user = int(user)
            
            if user > 1000000:
                return "Invalid input! The number can't be bigger than 1000000."
            elif user < 0:
                return "The number can't be negative!"
            else:
                return "pass"
        
        except Exception:
            return "A string is not a valid input!"
              
   
def check_winner(goal_num, user, robot_num):
    user = int(user) 
    
    if abs(goal_num - robot_num) > abs(goal_num - user):
        win_book['user'] += 1
        return "user"
    elif abs(goal_num - robot_num) == abs(goal_num - user):
        win_book['draw'] += 1
        return "draw"
    else:
        win_book['robot'] += 1
        return "robot"
 

goal_num = randrange(0,1000000)
robot_num = randrange(0,1000000)

while True:
    user = input("What is your number?\n") 
    check_response = check_user(user)
    
    if check_response is "quit":
        print(f'''\nYou won: {win_book['user']},
The robot won: {win_book['robot']},
Draws: {win_book['draw']}.''')
        quit()
    elif check_response is not "pass":
        print(check_response)
    else:
        winner = check_winner(goal_num, user, robot_num)
        
        print(f'''The robot entered the number {robot_num}.
The goal number is {goal_num}.''')

        if winner == 'user':
            print("You won!")
        
        elif winner == "robot":
            print("The robot won!")
