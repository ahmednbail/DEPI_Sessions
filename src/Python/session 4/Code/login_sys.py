import random
def login_sys():
    u='test'
    p='1111'
    while True:
        x=input('enter your username:')
        if x ==u:
            y=input('enter your password:')
            if y ==p:
                s=random.randrange(10000,100000)
                print('Verification code is:',s)
                while True:
                    l=int(input('Enter the verification code:'))
                    if l ==s:
                        print('Access granted')
                        break
                    else:
                        print('invalid verification code : please try again')
                break
            else:
                print('Incorrect password!')
                continue
        else:
            print('Incorrect username !')
            continue