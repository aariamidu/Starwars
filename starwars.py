import random
import requests


def random_person():
    person_number = random.randint(1, 82)
    url = 'https://swapi.dev/api/people/{}/'.format(person_number)
    response = requests.get(url)
    person = response.json()
    return {
        'name': person['name'],
        'height': person['height'],
        'mass': person['mass'],
        'birth year': person['birth_year'],
    }


def run():

    print('Hello stranger, Welcome to StarWars Top Trump!')
    player_name = input('What is your name?')
    lives_remaining = 3
    score = 0
    while lives_remaining > 0:
        my_person = random_person()
        print(player_name, ', you were given', my_person['name'])

        while True:
            stat_choice = input('Which stat do you want to use? ( height, mass, birth year)')
            if stat_choice.lower() not in ('height', 'mass', 'birth year'):
                print('Not an appropriate answer. Try again.')
            else:
                break

        opponent_person = random_person()
        print('The opponent chose', opponent_person['name'])
        my_stat = my_person[stat_choice]
        opponent_stat = opponent_person[stat_choice]

        if my_stat > opponent_stat:
            print(player_name, 'You Win! 🙌🏽')
            score = score + 1
            print(player_name, 'You have ', lives_remaining, 'lives remaining!')
            print('Your score is', score)
        elif my_stat == opponent_stat:
            print('Its A Draw!')
            print(player_name, 'You have', lives_remaining, 'lives remaining!')
            print('Your score is', score)
        elif my_stat < opponent_stat:
            lives_remaining = lives_remaining - 1
            print(player_name,  'You have', lives_remaining, 'lives remaining!')
            print('Your score is', score)


run()