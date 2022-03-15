b=5000000
PIN=0000
chances = 3
print('**********************************************WELCOME TO Aadits smart bank*******************************************************')
while chances>=0:
    x=int(input('pls enter ur pin: '))
    if x==PIN:
        print('****Login Sucessful****')
        x = int(input('Press 1 to continue: '))
        if x == 1:
            print('1. Check Balance')
            print('2. Withdraw Amount')
            d=int(input('Enter Your Choice: '))
            if d==1:
                print('Your Balance is:')
                print(b)
            elif d==2:
                w=int(input('Enter amount to withdraw:'))
                if w<b:
                    print('withdraw successful')
                    b=b-w
                else:
                    print('insufficient funds')
        else:
            print('Successfully Logged Out')
    else:
        print('***********Invalid Password*************')
        chances=chances-1
        if chances==0:
            print('**************************Account Blocked********************************')
           