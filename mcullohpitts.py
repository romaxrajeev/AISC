#Take inputs
inputs, output = [[0,0],[0,1],[1,0],[1,1]], [0,0,0,1]

#Initialize weights and bias
w1, w2 = 0,0

#Activation function
def activation(summation):
	if summation == 2:
		return 1
	return 0 
print("Initial Weight 1:",w1)
print("Initial Weight 2:",w2)

i = 0
while True:
	x = inputs[i][0]
	y = inputs[i][1]
	summation = x*w1 + y*w2
	if activation(summation) > output[i]:
		w1 -= 1
		w2 -= 1
	elif activation(summation) < output[i]:
		w1 += 1
		w2 += 1
	if activation(summation) == output[i]:
		i += 1
	if i == len(output):
		break
	
print("Final Weight 1:",w1)
print("Final Weight 2:",w2)
