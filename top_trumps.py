# #1. generate random id
import random

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
# #3. request from API
import requests
from pprint import pprint

url = 'https://pokeapi.co/api/v2/pokemon/{}/'


def call_API_and_save_to_dict(number, dict_general):
    response = requests.get(url.format(number))
    json = response.json()
    dict_general["name"] = json["name"]
    dict_general["id"] = json["id"]
    dict_general["height"] = json["height"]
    dict_general["weight"] = json["weight"]


call_API_and_save_to_dict(rand_id_user, stat_user)
call_API_and_save_to_dict(rand_id_comp, stat_comp)

pprint(stat_user)
pprint(stat_comp)

# 4. choose stats to compare
winner = ''
chosen_stat = input('Which stats do you want to compare? height/weight')
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

# 5. record result to the file
with open('tournament.txt', 'a') as text_write:
    add = 'winner: {}'.format(winner) + ' ; comparing: {}'.format(chosen_stat) + 'score: {}'.format(
        stat_user[chosen_stat]) + ': {}'.format(stat_comp[chosen_stat])
    text_write.write(add)
    text_write.close()
