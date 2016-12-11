# PythonFinal

## Dataset:  
  1.MovieLens:  
  (http://files.grouplens.org/datasets/movielens/ml-latest-small-README.html)
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
  2.pre-processing: 
  &emsp;(1) load all the files    
  &emsp;(2) extract publican year from movie titles and add a new column to store it  
  &emsp;(3) convert the rating timestamp into data and get the year and add a new column  
  &emsp;(4) based on genres column, extract unique_genre and record in new added columns  
  &emsp;(5) join the tables(movies.csv, users.csv, ratings.csv) to get a comprehensive table  
  &emsp;(6) drop NAN rows and duplicate rows  
  &emsp;(7) separate the new comprehensive table by genre and create new files for each genre, store them in /data/genres folder    
  
### Analysis1:  
  1.aim: calculate the average rating of each movie genre and show in plot chart and heapmap  
  2.process:  
      &emsp;step1: use argparse to get the input(age, gender, occupation, or all)  
      &emsp;step2: load data: load the comparehensive table, load occupation detail table, and merge
               get the unique_genres set  
      &emsp;step3: calculate average ratings of each genre in each dimension  
      &emsp;step4: generate heatmap and plot chart to present the results  
  3.result:   
      &emsp;(1.1) the average ratings for each genre from every age group  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis1/genre_age_fig.png)       
      &emsp;(1.2) the data of above figure  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis1/screenshot of csv files/genre_age.png)  
      &emsp;(2.1) the average ratings for each genre from every gender group    
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis1/genre_gender_fig.png)    
      &emsp;&emsp;(2.2) the data of above figure  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis1/screenshot of csv files/genre_gender.png)  
      &emsp;(3.1) the average ratings for each genre from every occupation group  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis1/genre_occupation_fig.png)  
      &emsp;(3.2) the data of above figure  7
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis1/screenshot of csv files/genre_occupation.png)
        
### Analysis2:  
  1.aim: classify users by age, gender, and occupation, and show the result with pie chart  
  2.process:  
      &emsp;step1: use argparse to get the input(age, gender, or occupation)   
      &emsp;step2: load data: load the users related tables: users, age, occupation, and merge
               them together to get full user informaiton  
      &emsp;step3: calculate the popularity in each age group, gender group, and occupation catagories   
      &emsp;step4: generate the pie chart to present the ratio each group  
  3.result:  
      &emsp;(1.1) the ratio of number users in each age group (pie chart)  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis2/figure_age.png)       
      &emsp;(1.2) the number of users in each age group  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis2/screenshot of csv files/age_count.png)  
      &emsp;(2.1) the ratio of number of users in each gender group (pie chart)  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis2/figure_gender.png)       
      &emsp;(2.2) the number of users in each age group  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis2/screenshot of csv files/gender_count.png)  
      &emsp;(3.1) the ratio of number of users in each occupation group (pie chart)  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis2/figure_occupation.png)       
      &emsp;(3.2) the number of users in each age group  
      &emsp;![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/Analysis2/screenshot of csv files/occupation_count.png)  
      
### Analysis3:  
  1.aim: calculate the average rating of each movie and sort it by men and women, then compare the rating of men  
  &emsp;and women, find the most disagreement movies  
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

### DashBoard:  
  1.use TKinter and tkMessageBox  
    ![](https://github.com/davidviva/DataAnalysisPython/raw/master/Final/output/dashboard.png)  
    
