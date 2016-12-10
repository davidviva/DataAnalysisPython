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
	age = data[data['age'] == int(args.age)]
	gender = age[data['gender'] == args.gender]
	occupation = gender[data['job_description'] == args.occup]
	mean_ratings = pd.pivot_table(occupation, values= 'rating',index=['title'],columns='gender',aggfunc='mean')
	
	return  mean_ratings[:int(args.topK)]

result = calculate(df)
result.to_csv(path + '/Analysis5/recommendation.csv')
print(result)

