MidTerm: StackOverFlow
Author: Yan Wu

—————————— Per-site methods ——————————————————— 

/questions
/users/{ids}
/users/{ids}/tags


—————————— Collect methods ——————————————————— 

(1) stackApi  fetch
(2) request.get()

—————————— Files ——————————————————— 
1. FecthScript.py
   # Third-party library: StackAPI,   used to fetch 600 records by default(pick 500)
   # selcted tags: python, numpy 
   # store the result into questions.json

2. Analysis1.py
   # aim: sort the questions by the weightage of owner’s badges
   # steps: (1) read questions.json and extract the owner’s user_Id
            (2) request the user object according to the user_Id
	    (3) get the badge information, and set the weightage(gold 3, silver 2, bronze 1)
            (4) calculate the weightage of owner’s badges and sort the questions ascendingly

3. Analysis2.py
   # aim: sort users identified with each tag according to reputation
   # steps: (1) read users.json to get user information
            (2) request user identified with tags from the site 
            (3) build the related data structure
   # data structure:
            (1) list: userInfo  [userName, link, reputation]
            (2) dictionary: user_dictionary: {user_Id, userInfo}
            (3) dictionary: tag_dictionary: {tag, {userId, repution}}

4. Analysis3.py
   # aim: calculate the population of each type of badge
   # steps: (1) read users.json and fetch the badge information
            (2) calculate the number of people of each badge

5. Analysis4.py
   # aim: find number of questions and number of answered questions for each tag
   # step: (1)

6. Analysis5.py
   # aim: find the user whose questions have highest accumulated scores
   # steps:  (1) read questions.json and get the owner info and score
             (2) build a dictionary to calculate the score of each user
             (3) sort the dictionary by the value score