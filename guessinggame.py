import random
def guess():
    try:
        a = int(input("Put the lowest number of the range: "))
        b = int(input("Put the highest number of the range: "))
        number = random.randint(a,b)
        c = int(input("How many times you want to try: "))
        d = []
        if b-a >= c:
            for i in range(c):
                print("Guess number ", i+1, ":")
                e = int(input())
                d.append(e)
                if d[i] == number:
                    break
            for i in range (len(d)):
                if d[i] == number:
                    break
            if d[i] == number:
                return "Congratulations"
            else:
                return "Game Over. The correct number is: " + str(number)
        else:
            return "Please reduce the number of try to make the game better"
    except(ValueError):
        return "Please enter all integer numbers"

print(guess())
