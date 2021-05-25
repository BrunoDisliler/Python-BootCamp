from random import choice
from Modules import Names_Data

followers = Names_Data.data
choose = choice(followers)
choose_2 = choice(followers)
current_score = 0
end_game = False

while not end_game:
    choose = choose_2
    choose_2 = choice(followers)
    print("""
        __  ___       __             
       / / / (_)___ _/ /_  ___  _____
      / /_/ / / __ `/ __ \/ _ \/ ___/
     / __  / / /_/ / / / /  __/ /    
    /_/ ///_/\__, /_/ /_/\___/_/     
       / /  /____/_      _____  _____
      / /   / __ \ | /| / / _ \/ ___/
     / /___/ /_/ / |/ |/ /  __/ /    
    /_____/\____/|__/|__/\___/_/     
    """)
    print(f'Compare A: {choose["name"]} a {choose["description"]}, from {choose["country"]}')
    print("""
     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    """)
    print(f'Against B: {choose_2["name"]} a {choose_2["description"]}, from {choose_2["country"]}')
    user_choice = str(input('Who has more followers? Type "A" or "B": ')).upper()
    if user_choice == 'A':
        if choose["follower_count"] > choose_2["follower_count"]:
            current_score += 1
            print(f'You´re right! Current score: {current_score}')
        else:
            print(f'You´re wrong! Final score: {current_score}')
            end_game = True
    if user_choice == 'B':
        if choose_2["follower_count"] > choose["follower_count"]:
            current_score += 1
            print(f'You´re right! Current score: {current_score}')
        else:
            print(f'You´re wrong! Final score: {current_score}')
            end_game = True
