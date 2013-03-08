import time
import numpy as np
import math
import sys

# connections
connections =              np.array([[0.0, 0.0, 1.0, 1.0, 1.0, 0.0]])
connections = np.append(connections,[[0.0, 0.0, 1.0, 1.0, 1.0, 0.0]],0)
connections = np.append(connections,[[0.0, 0.0, 0.0, 0.0, 0.0, 1.0]],0)
connections = np.append(connections,[[0.0, 0.0, 0.0, 0.0, 0.0, 1.0]],0)
connections = np.append(connections,[[0.0, 0.0, 0.0, 0.0, 0.0, 1.0]],0)
connections = np.append(connections,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)

weights =           np.array([[0.0, 0.0,-3.0, 2.0, 4.0, 0.0]])
weights = np.append(weights, [[0.0, 0.0, 2.0,-3.0, 0.5, 0.0]],0)
weights = np.append(weights, [[0.0, 0.0, 0.0, 0.0, 0.0, 0.2]],0)
weights = np.append(weights, [[0.0, 0.0, 0.0, 0.0, 0.0, 0.7]],0)
weights = np.append(weights, [[0.0, 0.0, 0.0, 0.0, 0.0, 1.5]],0)
weights = np.append(weights, [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)


# in this arrar i'm storing the "value" of the node
input = np.array([1.0, 2.0, 0.0, 0.0, 0.0, 0.0])
temporal = np.array([1.0, 2.0, 0, 0, 0, 0])

expected = np.array([0, 0, 0, 0, 0, 0.0])
error = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


#first propagation
for i in range(2,6):
    temporal[i] = sum(connections[:,i]*input*weights[:,i])
    input[i] = 1/(1+math.e**(-1*temporal[i]))

#error in node 6
error[5] = input[5]*(1-input[5])*(expected[5]-input[5])
print error[5]

#error in node 2 to 4
for i in range(2,5):
    error[i] = input[i]*(1-input[i])*sum(connections[i,:]*error*weights[i,:])

#new weights between the hidden layer and the output  
weights[2,5]=weights[2,5]+10*error[5]*input[2]
weights[3,5]=weights[3,5]+10*error[5]*input[3]
weights[4,5]=weights[4,5]+10*error[5]*input[4]



#new weights betwethen the input layer and the hidden layer  
weights[1,2]=weights[1,2]+10*error[2]*input[1]
weights[1,3]=weights[1,3]+10*error[3]*input[1]
weights[1,4]=weights[1,4]+10*error[4]*input[1]

weights[0,2]=weights[0,2]+10*error[2]*input[0]
weights[0,3]=weights[0,3]+10*error[3]*input[0]
weights[0,4]=weights[0,4]+10*error[4]*input[0]

print error
print input
print weights   

print "err_1 = %f" % error[0]
print "err_2 = %f" % error[1]
print "err_3 = %f" % error[2]
print "err_4 = %f" % error[3]
print "err_5 = %f" % error[4]
print "err_6 = %f" % error[5]
print "w_13 = %f" % weights[0,2]
print "w_14 = %f" % weights[0,3]
print "w_15 = %f" % weights[0,4]
print "w_23 = %f" % weights[1,2]
print "w_24 = %f" % weights[1,3]
print "w_25 = %f" % weights[1,4]
print "w_36 = %f" % weights[2,5]
print "w_46 = %f" % weights[3,5]
print "w_56 = %f" % weights[4,5]



