from random import randint

ans = {1:'r',2:'p',3:'s'}
while 1==1:
    print('Welcome in Rock Paper Scissors game')
    chosen1 = input('1) first player choose: r for rock, p for paper, s for scissors\n')
    chosen2 = ans[randint(1,3)]

    if chosen1 == 'r' and chosen2 == 'p':
        print('you rock and computer paper, computer wins')

    elif chosen1 == 'r' and chosen2 == 's':
        print('you rock and computer scissors, you win')


    if chosen1 == 'p' and chosen2 == 'r':
        print('you paper and computer rock, you win')

    elif chosen1 == 'p' and chosen2 == 's':
        print('you paper and computer scissors, computer wins')


    if chosen1 == 's' and chosen2 == 'r':
        print('you scissors and computer rock, computer wins')

    elif chosen1 == 's' and chosen2 == 'p':
        print('you scissors and computer paper, you win')

    elif chosen1 == chosen2:
        print('No body wins')

    else:
        print('wrong input')

