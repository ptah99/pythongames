import random

while True:
    def play():
        user = input("what's you choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            return 'it\'s a tie'
        # r > s, s > p, p > r
        if is_win(user, computer):
            return 'you won!'
        return 'you lost!'


    def is_win(user, computer):
        # return true if player wins
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
                or (user == 'p' and computer == 'r'):
            return True
    print(play())
