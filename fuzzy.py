#Fuzzy Logic

"""
NOTE: Please download fuzzy_functions.py along with this file to run this program, as it contains some of the functions.

Three descriptors for input

Small Dirt, Medium Dirt, Large Dirt
No grease, Medium Grease, Large Grease

Five descriptors for output

Very Small, Small, Medium, Large, Very Large
"""

"""
Rule base
   | NG MG LG
----------------
SD |   VS M  L
MD |   S  M  L
LD |   M  L  VL 

"""

import fuzzy_functions as f
import itertools

#Input : Dirt and Grease in percentage
print("This controller will give an estimate time in minutes of washing the clothes, depending on the percentage of grease and dirt.")
grease = int(input("Enter grease percentage: "))
dirt = int(input("Enter dirt percentage: "))

dirts = []
greases = []

#Assign the category to each input value accordingly.
if dirt in range(0,51):
	dirts.append({"0": f.small_dirt(dirt)})
	dirts.append({"1": f.medium_dirt(dirt)})
if dirt in range(50,101):
	dirts.append({"1": f.medium_dirt(dirt)})
	dirts.append({"2": f.large_dirt(dirt)})
	
if grease in range(0,51):
	greases.append({"0": f.small_grease(grease)})
	greases.append({"1": f.medium_grease(grease)})
if grease in range(50,101):
	greases.append({"1": f.medium_grease(grease)})
	greases.append({"2": f.large_grease(grease)})
	
#Get all possible combinations of them - did a cartesian product
combination = list(itertools.product(dirts,greases))
#Get the minimum value for the fuzzy function
rule_weights = []
max_weight_rule = {"name":"","value":0}
for i in combination:
	for x,y in zip(i[0],i[1]):
		#Also checking for the maximum weighted rule
		if min(i[0][x],i[1][y]) > max_weight_rule["value"]:
			max_weight_rule.update({"name":x+y,"value":min(i[0][x],i[1][y])})
		rule_weights.append({x+y : min(i[0][x],i[1][y])})
		
#Check in rule base and assign the appropriate function
if max_weight_rule["name"] == "00":  #VS
	mean_time = f.very_small_time(max_weight_rule["value"])
elif max_weight_rule["name"] == "10":  #S
	mean_time = f.small_time(max_weight_rule["value"])
elif max_weight_rule["name"] == "01" or max_weight_rule["name"] == "11" or max_weight_rule["name"] == "20":  #M
	mean_time = f.medium_time(max_weight_rule["value"])
elif max_weight_rule["name"] == "02" or max_weight_rule["name"] == "12" or max_weight_rule["name"] == "21":  #L
	mean_time = f.large_time(max_weight_rule["value"])
else:
	mean_time = f.very_large_time(max_weight_rule["value"])

#Printing the final time in minutes
print("Mean time required for the washing machine:",mean_time,"minutes")