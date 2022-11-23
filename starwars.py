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
        'birth_year': person['birth_year'],
    }


def run():
    print('Hello stranger, Welcome to StarWars Top Trump!')
    player_name = input('What is your name?')
    my_person = random_person()
    print(player_name, ',you were given {}'.format(my_person['name']))
    stat_choice = input('Which stat do you want to use? ( height, mass, birth_year)')
    opponent_person = random_person()
    print('The opponent chose {}'.format(opponent_person['name']))
    my_stat = my_person[stat_choice]
    opponent_stat = opponent_person[stat_choice]
    if my_stat > opponent_stat:
        print(player_name, ',You Win! 🙌🏽')
    elif my_stat < opponent_stat:
        print(player_name, ',You Lose! 🥺Try Again')
    else:
        print('Its A Draw!')

    my_person = random_person()
    print(player_name, ',you were given {}'.format(my_person['name']))
    stat_choice = input('Which stat do you want to use? ( height, mass, birth_year)')
    opponent_person = random_person()
    print('The opponent chose {}'.format(opponent_person['name']))
    if my_stat > opponent_stat:
        print(player_name, ',You Win! 🙌🏽')
    elif my_stat < opponent_stat:
        print(player_name, ',You Lose! 🥺Try Again')
    else:
        print('Its A Draw!')

    my_person = random_person()
    print(player_name, ',you were given {}'.format(my_person['name']))
    stat_choice = input('Which stat do you want to use? ( height, mass, birth_year)')
    opponent_person = random_person()
    print('The opponent chose {}'.format(opponent_person['name']))
    if my_stat > opponent_stat:
        print(player_name, ',You Win! 🙌🏽')
    elif my_stat < opponent_stat:
        print(player_name, ',You Lose! 🥺Try Again')
    else:
        print('Its A Draw!')


run()