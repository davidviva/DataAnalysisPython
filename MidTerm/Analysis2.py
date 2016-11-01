#!/usr/bin/python

# Author: Yan Wu

import json
import os
import sys
import requests

def query(path):

	#f = open(path + "/tags.json", 'w+')
	#t_count = 500
	#f.write("[")

	input_file = open(path + "/users.json", "r")
	# tag_dic : {tag, {userId, reputation}}
	tag_dic = {}
	# user_dic : {userId, userInfo[userName, link, reputation]}
	user_dic = {}

	json_decode=json.load(input_file)
	for item in json_decode:
		userId = item.get("user_id")
		userName = item.get("display_name")
		link = item.get("link")
		reputation = item.get("reputation")

		# Construct the user dictionary
		userInfo = [userName, link, reputation]
		user_dic[userId] = userInfo

		requestUrl = "https://api.stackexchange.com/2.2/users/" + str(userId) + "/tags?order=desc&sort=popular&site=stackoverflow&key=tpHQOQQZiglYz26b5zi5Gw(("

		# Construct tag dictionary
		tags = requests.get(requestUrl)
		for u in tags.json()["items"]:
			tag = u.get("name")
			if tag in tag_dic.keys():
				tag_dic[tag][userId] = reputation
			else:
				tag_dic[tag] = {}
				tag_dic[tag][userId] = reputation

	for tag in tag_dic.keys():
		for user in sorted(tag_dic[tag], key=tag_dic[tag].get, reverse=True):
			print("userId: " + str(user))
			userInfo = user_dic[user]
			print("userName: " + userInfo[0])
			print("link: " + userInfo[1])


#		# map userId to the tags
#		my_dictionary[user] = list

		#for u in user.json()["items"]:
		#	t_count -= 1
#
#			if t_count < 0:
#			    break
#
#			if t_count == 0:
#			    f.write(json.dumps(u))
#			    continue
#
#			f.write(json.dumps(u))
#			f.write(",") 
#			f.write("\n")
#	f.write("]")
#	f.close()
	input_file.close()


ScriptPath = os.path.split( os.path.realpath(sys.argv[0]))[0]
path = ScriptPath + "/stackApi"
query(path)



