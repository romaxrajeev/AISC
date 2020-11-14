#Making equations for dirt
def small_dirt(x):
	return((50-x)/50)

def medium_dirt(x):
	if x in range(0,51):
		return(x/50)
	return((100-x)/50)

def large_dirt(x):
	return((x-50)/50)

#Making equations for grease
def small_grease(x):
	return((50-x)/50)

def medium_grease(x):
	if x in range(0,51):
		return(x/50)
	return((100-x)/50)

def large_grease(x):
	return((x-50)/50)

#Making equations for wash time
def very_small_time(x):
	return(15 - 15*x)

def small_time(x):
	return( ( (x*15) + (30 - 15*x)) / 2)

def medium_time(x):
	return( ((15*x + 15) + (45 - 15*x)) / 2)

def large_time(x):
	return(( (15*x + 30) + (60 - 15*x) )/2)

def very_large_time(x):
	return(15*x + 45)
