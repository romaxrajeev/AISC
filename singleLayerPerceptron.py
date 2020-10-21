def roundOff(x):
	if abs(x - int(x)) >= 0.5:
		return int(x) + 1
	return int(x)

#Initialize the dataset
x = [1,2,3,4]
y = [1,4,5,9]

#Initialize the weights
w0,w1 = 0,0

#Learning rate
alpha = -0.01

#Number of iterations
NO_OF_ITERATIONS = 2000

#Calculate Y Pred
y_pred = [w0 + w1*i for i in x]

#Compute the cost function
costFunction = sum([int(y_pred[i] - y[i])**2 for i in range(len(x))])/len(x)
count = 0
while count < NO_OF_ITERATIONS:
	count += 1
	#Get new weights
	w0 = w0 + ( alpha * sum([2 * (y_pred[i] - y[i]) for i in range(len(x))]))
	w1 = w1 + ( alpha * sum([2 * (y_pred[i] - y[i]) * x[i] for i in range(len(x))]))
	
	#Calculate new Prediction
	y_pred = [w0 + w1*i for i in x]

	#Compute the new cost function
	costFunction = sum([int(y_pred[i] - y[i])**2 for i in range(len(x))])/len(x)

y_pred_round = [roundOff(x) for x in y_pred]
print(w0,w1)
print(y_pred,y_pred_round)