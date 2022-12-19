# Read Me

The code in this zip are the code and results for q2-q4



## About Result

The 'q2.csv',  folder q3 and q4 are the result files for q2-q4.
I saved it as '.csv' file.

#### The naming principle I used for q3 result files is :

'goal' + formation + total overall score for that dreaming team.

#### The naming rules I used for q4 result files is :

nation name + average overall score (for each players) for that team + a (tip that mean average) + the best formation (in '433-442-4231') for that country to use. 

And because there were too many missing data, some countries could not form even a complete formation. In order to eliminate the impact of missing data on the result, I filled the missing positions with a non-existent placeholder, with the overall score was equal to the average scores of all the players in the table (for that country).

But sadly, I found that this simply worked for countries with only a few positions missing, but for countries with most positions missing, I could only get exactly the same scores for three formations.



## About code

### About q2

Order for running: data -> select_data -> q2


### About q3

Order for running:	slist -> q3_433
	 											q3_442
	 											q3_4231

#### Warning:
I put the code used in the original q3 in the q3.py folder. If you want to run it directly, you may need to **modify the path when calling tables and other data** or drag them out of q3 into current folder


### About q4

I encapsulated the scripts in q3 as functions and made some supplementary modifications. so you can directly run q4



## Appendix(About data)

Finally, I organized all the data files and decided to keep them in the current folder.

Cause move them might influence the path in the script.

Where 

1. <u>squad list(new) folder</u> is the result of q1 and the data used for *data.py*
2. <u>'snblist.csv'</u> is result of *data.py* and the data used for *selected_data.py*
3. <u>snb folder</u>  is result of *selected_data.py* and the data used for *q2.py*
4. <u>'q2.csv'</u> is result of *q2.py* as the answer for q2
5. <u>'slist.csv'</u> is the data used for *q3_xxx.py*, I am sorry that I forgot to save code for this part as python file format, but you might could find it in the **jupyter notebook** we submitted
6. <u>snb folder</u> is also the data we used for *q4.py*



