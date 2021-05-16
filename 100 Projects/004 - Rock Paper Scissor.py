from random import randint

me = int(input('What do you choose? Type 0 for Rock, '
               '1 for Paper or 2 for Scissors: '))

computer = randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


if (me == 0 and computer == 0) or (me == 1 and computer == 1) or (me == 2 and computer == 2):
    print('DRAW! Try Again')
elif me == 0 and computer == 1:
    print(f'{rock}\n Computer choose {paper}\n You Lose!')
elif me == 1 and computer == 0:
    print(f'{paper}\n Computer choose {rock}\n You Win!')
elif me == 2 and computer == 1:
    print(f'{scissors}\n Computer choose {paper}\n You Win!')
elif me == 2 and computer == 0:
    print(f'{scissors}\n Computer choose {rock}\n You Lose!')
elif me == 1 and computer == 2:
    print(f'{paper}\n Computer choose {scissors}\n You Lose!')
elif me == 0 and computer == 2:
    print(f'{rock}\n Computer choose {scissors}\n You Win!')
