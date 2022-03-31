from flask import Flask, jsonify
from random import choice, randint
import requests

app = Flask(__name__)

file_names = ['users.txt', 'animals.txt', 'colors.txt', 'cities.txt']

def import_data(input_file):
	item_list = []
	with open(input_file) as names:
		lines = names.readlines()
	for line in lines:
		line = line.strip().replace('\n','')
		item_list.append(line)
	return item_list

name_list = import_data(file_names[0])
animal_list = import_data(file_names[1])
color_list = import_data(file_names[2])
city_list = import_data(file_names[3])


@app.route('/<user>')
def send_json(user):
	return jsonify({'username':user}),200

@app.route('/<user>/post',methods=['post'])
def send_json_post(user):
        return jsonify({'username':user}),200

@app.route('/get_users')
def send_users():
	users = {}
	for num in range(25):
		users[num]={'animal_id':randint(10000,100000),'firstname':choice(name_list), 'lastname':choice(name_list),'location':choice(city_list)}
	return jsonify({'users':users}), 200

@app.route('/get_animals')
def send_animals():
	animals = {}
	for num in range(25):
		animals[num]={'id':randint(10000,100000),'species':choice(animal_list), 'name':choice(name_list), 'color':choice(color_list)}
	return jsonify({'animals':animals}), 200


@app.route('/get_users/post', methods=['post'])
def send_users_post():
        users = {}
        for num in range(25):
                users[num]={'id':randint(10000,100000),'firstname':choice(name_list), 'lastname':choice(name_list)}
        return jsonify({'users':users}), 200

@app.route('/get_animals/post',methods=['post'])
def send_animals_post():
        animals = {}
        for num in range(25):
                animals[num]={'id':randint(10000,100000),'species':choice(animal_list), 'name':choice(name_list)}
        return jsonify({'animals':animals}), 200

app.run(host='0.0.0.0',port=5007)




