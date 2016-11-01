#!/usr/bin/python

# Author: Yan Wu

import os
import sys
import json

ScriptPath = os.path.split( os.path.realpath(sys.argv[0]))[0]
path = ScriptPath + "/stackApi/users.json"

gold_count = 0
silver_count = 0
bronze_count = 0

input_file = open(path, "r+")
json_decode = json.load(input_file)
for item in json_decode:

	if item.get("badge_counts").get("bronze") != 0:
		bronze_count += 1
	if item.get("badge_counts").get("silver") != 0:
		silver_count += 1
	if item.get("badge_counts").get("gold") != 0:
		gold_count += 1

input_file.close()

print("number of users have gold badge: " + str(gold_count))
print("number of users have silver badge: " + str(silver_count))
print("number of users have bronze badge: " + str(bronze_count))




