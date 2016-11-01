#!/usr/bin/python

# Author: Yan Wu

import json
import os
import sys
import requests

def checkFolder(path):
	if not os.path.exists(path):
		os.makedirs(path)
	else:
		print("Already exists the folder")

def query(path):
	my_dictionary = {}

	f = open(path + "/users.json", 'w+')
	t_count = 500
	f.write("[")
	list = []

	input_file = open(path + "/questions.json", "r")

	json_decode=json.load(input_file)
	for item in json_decode:
		title = item.get("title")
		userId = item.get("owner").get("user_id")

		user = requests.get("https://api.stackexchange.com/2.2/users/" + str(userId) + "?site=stackoverflow&key=tpHQOQQZiglYz26b5zi5Gw((")
		# print user
		for u in user.json()["items"]:

			badgeCount = u.get("badge_counts").get("bronze") + u.get("badge_counts").get("silver")*2 + u.get("badge_counts").get("gold")*3

		# print badgeCount
		my_dictionary[title] = badgeCount

		# print unique users
		#if userId not in list:
		#	list.append(userId)
		for u in user.json()["items"]:
				t_count -= 1

				if t_count < 0:
				    break

				if t_count == 0:
				    f.write(json.dumps(u))
				    continue

				print(json.dumps(u))
				f.write(json.dumps(u))
				f.write(",") 
				f.write("\n")
	f.write("]")
	f.close()
	input_file.close()

	print("badge count by reverse order: ")
	for w in sorted(my_dictionary, key=my_dictionary.get, reverse=True):
		print(w, my_dictionary[w])

ScriptPath = os.path.split( os.path.realpath(sys.argv[0]))[0]
path = ScriptPath + "/stackApi"
checkFolder(path)
query(path)



