#!/usr/bin/python
# coding: utf-8
#%matplotlib inline

# Author: Yan Wu
# the relationship between rating and age

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Get the directory of current script
ScriptPath = os.path.split( os.path.realpath(sys.argv[0]))[0]
path = ScriptPath + "/data"
print(path)

movies = pd.read_csv(path + '/movies.csv')
users = pd.read_csv(path + '/users.csv')
ratings = pd.read_csv(path + '/ratings.csv')
age = pd.read_csv(path + '/age.csv')
users1 = pd.merge(users, age)
data = pd.merge(pd.merge(ratings,users1),movies)

print(data.head())

#most_rated = lens.groupby('title').size().sort_values(ascending=False)
#movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
#movie_stats.head()
#atleast_100 = movie_stats['rating']['size'] >= 50
#movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)

# distribution of users' ages
users.age.plot.hist(bins=30)
plt.title("Distribution of users' ages")
plt.ylabel('count of users')
plt.xlabel('age');
plt.show()

data.groupby('age_group').agg({'rating': [np.size, np.mean]})
most_50 = lens.groupby('movie_id').size().sort_values(ascending=False)[:50]
lens.set_index('movie_id', inplace=True)
by_age = lens.loc[most_50.index].groupby(['title', 'age_group'])
by_age.rating.mean().head(15)
by_age.rating.mean().unstack(1).fillna(0)[10:20]




