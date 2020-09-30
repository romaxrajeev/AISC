#Create the input graph
graph = [
	[0,4,3,0,0,0,0,0],
	[0,0,0,0,12,5,0,0],
	[0,0,0,7,10,0,0,0],
	[0,0,0,0,2,0,0,0],
	[0,0,0,0,0,0,2,5],
	[0,0,0,0,0,0,0,16],
	[0,0,0,0,0,0,0,4],
	[0,0,0,0,0,0,0,0]
	]


#Initialize the lists
openList = []
closedList = []
h = [14,12,11,6,4,11,1,0]
goalNode = 7
paths = []

#Add S to openList
data = { 
		"currNode": 0,
		"path": [0],
		"path_cost" : 0,
		"path_and_h": h[0]
		}
openList.append(data)

while openList != []:
	#Get minimum path cost from OpenList
	openList.sort(key=lambda x : x["path_and_h"])
	currNode = openList.pop(0)
	#Add to closed list
	closedList.append(currNode)
	
	#Check if current node is goal
	if currNode["currNode"] == goalNode:
		data = {
			"path":currNode["path"],
			"cost": currNode["path_and_h"]
			}
		paths.append(data)
	else:
		#Get all the nodes connected to current node
		for i in range(8):
			if graph[currNode["currNode"]][i] != 0:
				data = {
					"currNode":i,
					"path": currNode["path"] + [i],
					"path_and_h": currNode["path_cost"] + graph[currNode["currNode"]][i] + h[i],
					"path_cost": currNode["path_cost"] + graph[currNode["currNode"]][i]
					}
				#print("For current node",currNode["currNode"],"data is",data)
				openList.append(data)
paths.sort(key=lambda x : x["cost"])
print(paths[0])