import random
import requests
import csv


def readscores(filename):
    scores = {}
    with open(filename, 'r') as csv_file:
        for row in csv.DictReader(csv_file):
            scores[row['player_name']] = int(row['score'])
    return scores


def writescores(scores, filename):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['player_name', 'score'])
        writer.writerows(scores.items())


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
    scores = readscores('score.csv')
    highest_score = max(scores.values())

    print('Hello stranger, Welcome to StarWars Top Trump!')

    player_name = input('What is your name?')
    print('The highest score to beat is', highest_score)
    game = input("Do you think you can beat this? y/n")
    if game == "y":
        print("Good luck!!")
    else:
        print("You've got this")
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
            print(player_name, 'You Win!')
            score = score + 1
        elif my_stat == opponent_stat:
            print('Its A Draw!')
        elif my_stat < opponent_stat:
            lives_remaining = lives_remaining - 1

        print(player_name,  'You have,', lives_remaining, 'lives remaining!')
        print('Your score is', score)

        scores[player_name] = score
        writescores(scores, 'score.csv')

        print('SCORE: ', score)
        if score > highest_score:
            highest_score = score
            print(highest_score)


run()
