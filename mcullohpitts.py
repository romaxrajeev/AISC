#Take inputs
inputs, output = [[0,0],[0,1],[1,0],[1,1]], [0,0,0,1]

#Initialize weights and bias
w1, w2, b = 1,1,1

#Activation function
def activation(summation):
	if summation >= 0:
		return 1
	return 0 

i = 0
while True:
	x = inputs[i][0]
	y = inputs[i][1]
	summation = x*w1 + y*w2 + b
	if activation(summation) > output[i]:
		b -= 1
	elif activation(summation) < output[i]:
		b += 1
	if activation(summation) == output[i]:
		i += 1
	if i == len(output):
		break
	
print(w1,w2,b)