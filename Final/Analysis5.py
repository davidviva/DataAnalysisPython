#!/usr/bin/python
# coding: utf-8

# Author: Yan Wu

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import argparse

# get input 
parser = argparse.ArgumentParser(description='very simple recommendation')
parser.add_argument("gender", help="gender")
parser.add_argument("age", help="age")
parser.add_argument("occup", help="occupation")
parser.add_argument("topK", help="how manywant to see")
args = parser.parse_args()

# load data
ScriptPath = os.path.split( os.path.realpath(sys.argv[0]))[0]
path = ScriptPath + "/data"

user_ratings = pd.read_csv(path + '/user_ratings.csv')
occupation = pd.read_csv(path + '/occupation.csv')
age = pd.read_csv(path + '/age.csv')

df = pd.merge(age, pd.merge(user_ratings, occupation))
#print(userInfo.head())
path = ScriptPath + "/output"

def  calculate(data):
	data = data.sort_values(by = 'rating', ascending=False)
	#if data[data.age == args.age].size() is 0:
	#	return data.ix[:args.topK]
	age = data[data.age == args.age]

	#if data[data.gender == args.gender].size() is 0:
		#return age.ix[:args.topK]
	gender = age[data.gender == arge.gender]

	#if data[data.job_description == args.occup].size() is 0:
	#	return gender.ix[:args.topK]
	occupation = gender[data.job_description == arge.occup]
	
	return  occupation.ix[:args.topK]

result = calculate(df)
print(result)

