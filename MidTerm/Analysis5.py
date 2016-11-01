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

	input_file = open(path + "/questions.json", "r")

	# user_dic : {userId, accumulated_score}
	score_dic = {}

	json_decode=json.load(input_file)
	for item in json_decode:
		userId = item.get("owner").get("user_id")
		score = item.get("score")

		# Construct the score dictionary
		if userId in score_dic.keys():
			score_dic[userId] = score_dic[userId] + score
		else :
			score_dic[userId] = score

	highest = 1
	for user in sorted(score_dic, key=score_dic.get, reverse=True):
		if highest == 1:
			print("userId: " + str(user))
			print("highest score: " + str(score_dic[user]))
			break;


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



