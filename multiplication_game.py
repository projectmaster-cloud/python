from running import run
print("Multiplication game")

running = True
while running:
    score = 0
    fails = 0
    num = int(input("Enter: Mutiplication Table #"))
    multiples = int(input("Enter: how many mutiples do you want? "))
    for i in range(1, multiples+1):
        ans = int(input(f"{num} x {i} = "))

        while ans != num * i:
         print("wrong")
         fails-=1
         ans = int(input(f"{num} x {i} = "))

        if ans == num * i:
           print("correct")
           score+=1

        if fails > 0: score-=1

    print(f"score: {score}/{multiples}")
    
    running = run()

    

