
IDEA: People tend to cycle more on Sundays than Saturdays.

*WHY? expand on why this question is interesting**

Null hypothesis: Average NUMBER OF bike trips for Saturday is the same or more than that of the Sunday. 
** what are you averaging over? what is the time period over which you will test your hypothesis? 
You should make sure that it is long enough that you do not hit special days, for example sport games or festivals 
may affect this result if you do not average over enough weeks. And even if you do the MEDIAN would be a 
better metric than the mean because it is more robust to outliers, though most of the tests you have seen so far are 
better suited to compare means**

Alternative hypothesis: Average bike trips for Sunday is more than that of Saturday's.

** the Ho and H1 are set up correctly for the question*

At a significance level of α=0.05

$H_0$ : Sat - Sun >= 0

$H_1$ : Sat - Sun < 0

** the formulae are ok but you should use  more suited math symbols **

$H_0$ : <N>_Sat - <N>_Sun >= 0

$H_1$ : <N>_Sat - <N>_Sun < 0


Figure 1: a better plot would be a scatter plot where the points are different colors for Saturdays and Sundays, or even a line plot but mark which is Saturday which is Sunday. As it is I cannot understand what the plot is saying.
the figure caption is lacking info: which day of the week was the day of the dip? what will you do about it in your analysis?
There is an obvious up down behavior, are the ups saturdays or sundays?
The following plots answer some of these questions but the captions are insufficient. remember to include "what" and "why": not just what you are shoing but why, what answer does this plot give or question prmopt?

To answer the question "are the means the same within some statistical significance" you also need the standard deviation of the sample so you need a new cell

overall_satsun_std = pd.DataFrame(new_satsun.groupby(['weekday'])['count'].std()).reset_index()

Once you have that you can plot it in the last plot as an errorbar

Otherwise the data is processed ok and it can support the answer to the question. 


**test**
As you set up the problem you want to test a difference of means, so a t-test is appropriate: specifically a one tailed t test 

SE = sqrt[(s1**2/n1) + (s2**2/n2)]


t = [ (m1 - m2) ] / SE

s1 is the standard deviation of sample 1, s2 is the standard deviation of sample 2, n1 is the sixe of sample 1 n2 is the size of sample 2, amd m1 and m2 are the means


https://stattrek.com/hypothesis-test/difference-in-means.aspx
