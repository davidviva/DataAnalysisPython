#!/usr/bin/python

# Author: Yan Wu

import json
import os
import sys
import requests

# Get the directory of the collected data
ScriptPath = os.path.split( os.path.realpath(sys.argv[0]))[0]
path = ScriptPath + "/stackApi"

# key: tag, value: [number of questions, number of questions were answered]
tag_dict = {}

#f = open(path + "/dataForAnalysis4.json", 'w+')
#t_count = 500
#f.write("[")
input_file = open(path + "/questions.json", "r")
json_decode=json.load(input_file)
for item in json_decode:
	ques_id = item.get("question_id")
	# Get the list of tags of each questiones
	tags = item.get("tags")
	# Find if the questino is answered
	is_answered = item.get("is_answered")
	# Get the number of answers given for each question
	answer_count = item.get("answer_count")

	answered = 0
	if is_answered:
		answered = 1

	for tag in tags:
		if tag_dict.get(tag) is None:
			tag_dict[tag] = [1, answered]
		else:
			tag_dict[tag][0] += 1
			tag_dict[tag][1] += answered

	# write the extracted data into "dataForAnalysis4.json"		
#	t_count -= 1

#	if t_count < 0:
#		break

#	if t_count == 0:
#		f.write(json.dumps(u))
#		continue

#	f.write(json.dumps(u))
#	f.write(",") 
#	f.write("\n")
#f.write("]")
input_file.close()
#f.close()

for key in tag_dict.keys():
	print("tag: " + key + "  ")
	print("  # questions: " + str(tag_dict[key][0]))
	print("  # answered: " + str(tag_dict[key][1]))
	print("/n")






