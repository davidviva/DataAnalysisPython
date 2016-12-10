# PythonFinal

## Dataset:  
  1.MovieLens:  
  &emsp;users.csv: userId, gender, age, occupation, zipcode  
  &emsp;movies.csv: movieId, title, genres  
  &emsp;ratings.csv: userId, movieId, rating, timestamp  
  &emsp;tags.csv: userId, movieId, tag, timestamp  
  &emsp;links.csv: movieId, imdbId, tmdbId  
  &emsp;genome-tags.csv: tagId, tag  
  &emsp;age.csv: age, age_group  
  &emsp;occupation.csv: occupation, description  
  
### CollectData and pre-processing:  
  1.CollecteData: download .csv files directly  
  2.pre-processing: (1) load all the files    
                    (2) extract publican year from movie titles and add a new column to store it  
                    (3) convert the rating timestamp into data and get the year and add a new column  
                    (4) based on genres column, extract unique_genre and record in new added columns  
                    (5) join the tables(movies.csv, users.csv, ratings.csv) to get a comprehensive table  
                    (6) drop NAN rows and duplicate rows  
                    (7) separate the new comprehensive table by genre and create new files for each one  
### Analysis1:  
  1.aim: calculate the average rating of each movie genre and show in plot chart and heapmap  
  2.process: 
      &emsp;step1: use argparse to get the input(age, gender, occupation, or all)  
      &emsp;step2: load data: load the comparehensive table, load occupation detail table, and merge
               get the unique_genres set  
      &emsp;step3: calculate average ratings of each genre in each dimension  
      &emsp;step4: generate heatmap and plot chart to present the results  
  3.result:  
        
### Analysis2:  
  1.aim: classify users by age, gender, and occupation, and show the result with pie chart  
  2.process:  
      &emsp;step1: use argparse to get the input(age, gender, or occupation)   
      &emsp;step2: load data: load the users related tables: users, age, occupation, and merge
               them together to get full user informaiton  
      &emsp;step3: calculate the popularity in each age group, gender group, and occupation catagories   
      &emsp;step4: generate the pie chart to present the ratio each group  
  3.result:  
  
### Analysis3:  
  1.aim: calculate the average rating of each movie and sort it by men and women, then compare the rating of men and women,
      find the most disagreement movies  
  2.process:  
      &emsp;step1: use argparse to get the input(the threshold of fillter data, and the topk number)  
      &emsp;step2: load data: load the user_ratings table  
      &emsp;step3: use pivot table to calculate average rating of each gender and group by movie title   
      &emsp;step4: statistic the number of ratings of each movie, filter records that below the threshold   
      &emsp;step5: sort the ratings by gender and store   
      &emsp;step6: add a new column to store the rating differences between male and female   
      &emsp;step7: pick the topk * 2 (favored by male and female) to generate a barh chart  
  3.result  
  
  
### Analysis4:  
  1.aim: find the taste changes of each age_group of each movie genre  
  2.process:   
      &emsp;step1: use argparse to get the input(age, gender, or occupation)  
      &emsp;step2: load data: load the users related tables: users, age, occupation, and merge
               them together to get full user informaiton  
      &emsp;step3: calculate the popularity in each age group, gender group, and occupation catagories   
      &emsp;step4: generate the pie chart to present the ratio each group  
  3.result:  
  
### Analysis5:  
  1.aim: get the topk recommendations based on the given data  
  2.process:  
      &emsp;step1: use argparse to get the input(age_group, genre)  
      &emsp;step2: load data: load the genre_rating file according to the given genre , merge age_group with the rating data
      &emsp;step3: calculate the average ratings year by year for the given genre movies and age_group   
      &emsp;step4: generate the plot chart to present the taste change trends by years   
  3.result:  
  
### Analysis6:  
  1.aim: recommend registered users movies based on pearson algorithm  
  2.process:  
      &emsp;step1: use pearson algorithm to find similar users  
      &emsp;step2: train the engine first, and use the test data to test
  3.result
