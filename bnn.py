
'''
Implementation of Boolean Neural Networks (BNN) Roman Kohut, Bernd Steinbach
TU Freiberg 2004


'''
import sys
import numpy as np
import math

#Convert Nx and Ny to Xommand Line Arguments
# Nx=2 #Number of Inputs#####################################################################
# Ny=7 #Number of Outputs####################################################################





def evaluate(K_mat,am_mat,Nx,Ny,out,layers):

	print 'The Original A Matrix',out
	# print layers
	for i in range(Nx,Nx+Ny):

		for j in range(0,2**Nx):
			temp_xor=np.logical_and(K_mat[j,0],am_mat[0,i])
			for z in range(1,layers):
				temp_xor=np.logical_xor(temp_xor,(np.logical_and(K_mat[j,z],am_mat[z,i])))

			out[j,i]=temp_xor
			print temp_xor


	print 'The Evaluated A Matrix'
	print  out

	# return out



#Modular Code.





#The training set is the Nx * (Nx+Ny) Matrix

#input using a text file.

if(len(sys.argv)==4):
	print 'Input file is :', sys.argv[1]
	print  'Inputs:',sys.argv[2]
	print  'Outputs',sys.argv[3]
else:
	print 'Enter only one Argument i.e the input file name, Input and Output respectively'
	exit(-1)


Nx=int(sys.argv[2])
Ny=int(sys.argv[3])

dataset=np.zeros(shape=(2**Nx,(Nx+Ny))) # The A matrix

A=np.zeros(shape=(2**Nx,(Nx+Ny)))
out=np.zeros(shape=(2**Nx,(Nx+Ny)))

file=open(sys.argv[1],"r")

for i in range(0,Nx**2):
	line=file .readline()
	dataset[i]=line.split(",")
	A[i]=dataset[i]
	out[i]=dataset[i]

#Extracting Data from the file assumming that the Data are seperated by ','


print dataset


#Define the matrixes required in the Algorithm


D=np.zeros(shape=(2**Nx,1))
K=np.zeros(shape=(2**Nx,1))

K_mat=np.zeros(shape=(2**Nx,1))

# weights=np.array([])
# am_mat=np.array([])


am=np.zeros(shape=(1,(Nx+Ny)))
am_mat=np.zeros(shape=(1,(Nx+Ny)))


# A=dataset
# out=dataset

print 'The dataset copy',out

iteration=0

while (True): #Exit When all the Zeros in the D matrix becomes 0
	#We need to calculate the D matrix now for each row in dataset
	
	iteration=iteration+1

	print 'This is iteration  ', iteration

	# print 'The Matrix updated', A
	# print 'The activation function for neurons',K
	# print 'The Weights of the Connection',am
	
	



	for i in range(0,(2**Nx)):
		temp_or=np.zeros(shape=(1,1));

		for j in range(0,(Nx+Ny)):
			temp_or[0,0]=np.logical_or(temp_or[0,0],A[i,j])

		D[i,0]=temp_or


	#Now the D matrix is calculated.

	#Check here if the D Matrix is all 0.
	zero_count=0;
	for i in range(0,(2**Nx)):
		if(D[i,0]==0):
			zero_count=zero_count+1;


	if(zero_count==4):
		print 'The Model is Trained '

		am_mat=np.delete(am_mat,0,axis=0)
		K_mat=np.delete(K_mat,0,axis=1)
		# print K_mat
		# print am_mat

		#Print Whatever things needed
		print 'The K Matrix K1,... Kn in Columns '
		print K_mat
		print 'The Am Matrix am1, am2..... in rows'
		print am_mat
		# print dataset
		# print out
		break



	#Get the index where D is 1.

	index1=0

	for i in range(0,(2**Nx)):
		if(D[i,0]==1):
			break
		else:
			index1=index1+1


	am[0]=A[index1]

	#Now compute K
	for i in range(0,(2**Nx)):
		temp_or=np.zeros(shape=(1,1));
		temp_and=np.zeros(shape=(1,1));

		for j in range(0,(Nx+Ny)):

			temp_and[0,0]=np.logical_and(A[i,j],am[0,j])

			temp_or[0,0]=np.logical_or(temp_or[0,0],(temp_and[0,0]))

		K[i,0]=np.logical_and(temp_or,D[i,0])



	# We just need to update the matrix A


	for i in range(0,(2**Nx)):
		#temp_or=0;

		for j in range(0,(Nx+Ny)):
			temp_and[0,0]=np.logical_and(am[0,j],K[i,0])
			A[i,j]=np.logical_xor(A[i,j],temp_and[0,0])

	
	K_mat=np.concatenate((K_mat,K),axis=1)
	am_mat=np.concatenate((am_mat,am),axis=0)

	#Now since the A is updated just store the Weights and Am of this iteration
	
# evaluate(K_mat,am_mat,Nx,Ny,out,layers=(iteration-1))


















