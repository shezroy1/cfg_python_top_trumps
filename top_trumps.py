# #1. generate random id
import random

how_many1=input("How many Pokemons do you want to get?")
how_many=int(how_many1)

stat_user=[]
rand_id_user=[]

for i in range(0,how_many):
    rand_id_user.append(random.randint(1, 151))
    stat_user.append({
    'id': '',
    'name': '',
    'height': '',
    'weight': '',
    })

rand_id_comp = random.randint(1, 151)
#
# #2. create storage space for stats


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

for count in range(0,how_many):
    call_API_and_save_to_dict(rand_id_user[count], stat_user[count])
    pprint(stat_user[count])

which_name=input("Type name of the pokemon you want to use ")

for key in stat_user:
    if key["name"]==which_name:
        stats_dict={"height":key["height"],
        "weight" : key["weight"]
        }
call_API_and_save_to_dict(rand_id_comp, stat_comp)


pprint(stat_comp)

# 4. choose stats to compare
winner = ''
chosen_stat = input('Which stats do you want to compare? height/weight')
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

# 5. record result to the file
with open('tournament.txt', 'a') as text_write:
    add = 'winner: {}'.format(winner) + ' ; comparing: {}'.format(chosen_stat) + ' ; score: {}'.format(
        stats_dict[chosen_stat]) + ' : {} \n'.format(stat_comp[chosen_stat])
    text_write.write(add)
    text_write.close()
