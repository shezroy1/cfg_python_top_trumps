import random
import requests
from pprint import pprint


def random_number():
    return random.randint(1, 151)


def call_API_and_save_to_dict(number, dict_general):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'
    response = requests.get(url.format(number))
    json = response.json()
    dict_general["name"] = json["name"]
    dict_general["id"] = json["id"]
    dict_general["height"] = json["height"]
    dict_general["weight"] = json["weight"]


def one_turn():
    stat_comp = {
        'id': '',
        'name': '',
        'height': '',
        'weight': '',
    }

    how_many = int(input("How many Pokemon's do you want to get?"))

    if (how_many != 1):
        stat_user = []
        rand_id_user = []
        for i in range(0, how_many):
            rand_id_user.append(random_number())
            stat_user.append({
                'id': '',
                'name': '',
                'height': '',
                'weight': '',
            })

        for count in range(0, how_many):
            call_API_and_save_to_dict(rand_id_user[count], stat_user[count])
            pprint(stat_user[count])

        which_name = input("Type name of the pokemon you want to use ")

        for key in stat_user:
            if key["name"] == which_name:
                stats_dict = {"height": key["height"],
                              "weight": key["weight"]
                              }
    else:
        stats_dict = {}
        call_API_and_save_to_dict(random_number(), stats_dict)
        pprint(stats_dict)

    rand_id_comp = random_number()
    call_API_and_save_to_dict(rand_id_comp, stat_comp)

    pprint(stat_comp)

    winner = ''
    chosen_stat = input('Which stats do you want to compare? height/weight\n')
    if chosen_stat == 'weight':
        if stats_dict["weight"] >= stat_comp['weight']:
            print('You win!')
            winner = "user"
        else:
            print('Computer wins 😞')
            winner = "computer"
    if chosen_stat == 'height':
        if stats_dict["height"] >= stat_comp['height']:
            print('You win!')
            winner = "user"
        else:
            print('Computer wins 😞')
            winner = "computer"

    with open('./top_trumps/tournament.txt', 'a') as text_write:
        add = 'winner: {}'.format(winner) + ' ; comparing: {}'.format(chosen_stat) + ' ; score: {}'.format(
            stats_dict[chosen_stat]) + ' : {} \n'.format(stat_comp[chosen_stat])
        text_write.write(add)
        text_write.close()

    play_again = input("Want to play again? y/n\n")

    if play_again == "y":
        one_turn()
    else:
        exit(1)


one_turn()