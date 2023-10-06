from random import choice
def play_human_turn(n):
    num1 = int(input(f"Subtract 1, 2, or 3 from the current number to pick a number: "))
    while True:
        if num1 > 3 or num1 < 1 :
            print("Number inputed is invalid.\nInput 1, 2, or 3")
            num1 = int(input(f"Subtract 1, 2, or 3 from the current number to pick a number: "))
            continue
        else:
            break
        

    n -= num1
    print(f"Number of coins are {n}")
    if n == 0:
        print("user wins!")
        return n
    return n

def play_computer_turn(n):
    if n%4 != 0 and n > 0 :
            for num in range(n-3, n):
                if num % 4 == 0:
                    comp_choice = n - num
                    n = num
                    
                    if num != 0:
                        print(f"Computer😀: I pick {comp_choice}!")
                        print(f"Number of coins are {n}")
                        return n
                        
                        
                    else:
                        print(f"Computer😀: I pick {comp_choice}!\nI win!")
                        return n
                        

    elif n%4 == 0:
        num = choice(range(n-3, n))

        comp_choice = n - num
        n = num
                    
        if num != 0:
            print(f"Computer😀: I pick {comp_choice}!")
            print(f"Number of coins are {n}")
            return n
                
                        
        else:
            print(f"Computer😀: I pick {comp_choice}!\nYou win!")
            return n
                

