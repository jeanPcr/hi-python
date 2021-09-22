import random
def start(range):
    a = range[0]
    b = range[1]
    counter = 0
    print ("********💡 Welcome to the Guessing Game 💡********")
    pc_number = random.randint(a,b)
    user_number = int(input("🤖 I have chosen a number ! Try to find it in the range [%s,%s] : " % (a,b)))
    counter = 1
    while user_number != pc_number :
        if user_number > pc_number and user_number <= b :
            b = user_number
        elif user_number > b:
            print("🤖 You have to chose a number in the range [%s,%s] : " % (a,b))
        if user_number < pc_number and user_number > a :
            a = user_number
        elif user_number < a:
            print("🤖 You have to chose a number in the range [%s,%s] : " % (a,b))
        
        user_number = int(input("🤖 Missed ! Try again in the range [%s,%s] : " % (a,b)))
        counter = counter +1

    print ("Congrats !🎉 You've found it in %s tries. "%(counter))


start([0,100])