#project_euler_question_1.py
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#the sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import numpy as np
import scipy as sp
#getting the remainders of the 1000 divided by 5 and 3 respectively 
five_remain=1000//5 # 200
three_remain= 1000//3 # 333

#using the arange fuction to create a list of the multiples of 3 and 5 w 
  
    
list_five_remain=np.arange(five_remain)*5

#added plus one to the end step to go from 0 to 333, not 332 since the end step of arrange is not inclusive
list_three_remain= np.arange(three_remain+1)*3 

#printed list to verify the numbers  I was expecting 
#print(list_five_remain) 
#print(list_three_remain)

#combining the list into one list
total_list= np.concatenate((list_three_remain,list_five_remain))
unique_total_list= np.unique(total_list)
#print(unique_total_list)
print(np.sum(unique_total_list))
#other method 
sum_five_remain=np.sum(list_five_remain)
sum_three_remain= np.sum(list_three_remain)
#print(np.arange((1000//15)+1)*15)
double_count_sum=np.sum(np.arange((1000//15)+1)*15)
#print(double_count_sum)
total_two= (sum_three_remain+ sum_five_remain)- double_count_sum
print(total_two)
