# #1. generate random id
import random
import requests
from pprint import pprint


def store_result_to_file(winner_of_round, chosen_stat_of_round, stat_comp_of_round, stat_user_of_round):
    # 5. record result to the file
    with open('./top_trumps/tournament.txt', 'a') as text_write:
        add = 'winner: {}'.format(winner_of_round) + ' ; comparing: {}'.format(
            chosen_stat_of_round) + ' ; score: {}'.format(
            stat_user_of_round[chosen_stat_of_round]) + ' : {} \n'.format(stat_comp_of_round[chosen_stat_of_round])
        text_write.write(add)
        text_write.close()


def call_API_and_save_to_dict(number, dict_general):
    response = requests.get(url.format(number))
    json = response.json()
    dict_general["name"] = json["name"]
    dict_general["id"] = json["id"]
    dict_general["height"] = json["height"]
    dict_general["weight"] = json["weight"]


rand_id_user = random.randint(1, 151)
rand_id_comp = random.randint(1, 151)
#
# #2. create storage space for stats
stat_user = {
    'id': '',
    'name': '',
    'height': '',
    'weight': '',
}

stat_comp = {
    'id': '',
    'name': '',
    'height': '',
    'weight': '',
}

url = 'https://pokeapi.co/api/v2/pokemon/{}/'

call_API_and_save_to_dict(rand_id_user, stat_user)
call_API_and_save_to_dict(rand_id_comp, stat_comp)

pprint(stat_user)
pprint(stat_comp)

# 4. choose stats to compare
winner = ''
chosen_stat = input('Which stats do you want to compare? height/weight\n')
if chosen_stat == 'weight':
    if stat_user['weight'] >= stat_comp['weight']:
        print('You win!')
        winner = "user"
    else:
        print('Computer wins 😞')
        winner = "computer"
if chosen_stat == 'height':
    if stat_user['height'] >= stat_comp['height']:
        print('You win!')
        winner = "user"
    else:
        print('Computer wins 😞')
        winner = "computer"

store_result_to_file(winner, chosen_stat, stat_comp, stat_user)
