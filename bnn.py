
'''
Implementation of Boolean Neural Networks (BNN) Roman Kohut, Bernd Steinbach
TU Freiberg 2004


'''
import sys
import numpy as np
import math

#Modular Code.

Nx=2 #Number of Inputs#####################################################################
Ny=7 #Number of Outputs####################################################################


dataset=np.zeros(shape=(Nx**2,(Nx+Ny))) # The A matrix


#The training set is the Nx * (Nx+Ny) Matrix

#input using a text file.

if(len(sys.argv)==2):
	print 'Input file is :', sys.argv[1]
else:
	print 'Enter only one Argument i.e the input file name and change the Input and Output Correspondingly in the script'
	exit(-1)


file=open(sys.argv[1],"r")

for i in range(0,Nx**2):
	line=file .readline()
	dataset[i]=line.split(",")

#Extracting Data from the file assumming that the Data are seperated by ','


print dataset


#Define the matrixes required in the Algorithm

A=np.zeros(shape=(Nx**2,(Nx+Ny)))
D=np.zeros(shape=(Nx**2,1))
K=np.zeros(shape=(Nx**2,1))

K_mat=np.zeros(shape=(Nx**2,1))

# weights=np.array([])
# am_mat=np.array([])


am=np.zeros(shape=(1,(Nx+Ny)))
am_mat=np.zeros(shape=(1,(Nx+Ny)))


A=dataset

iteration=0

while (True): #Exit When all the Zeros in the D matrix becomes 0
	#We need to calculate the D matrix now for each row in dataset
	
	iteration=iteration+1

	print 'This is iteration  ', iteration

	# print 'The Matrix updated', A
	# print 'The activation function for neurons',K
	# print 'The Weights of the Connection',am
	
	



	for i in range(0,(Nx**2)):
		temp_or=np.zeros(shape=(1,1));

		for j in range(0,(Nx+Ny)):
			temp_or[0,0]=np.logical_or(temp_or[0,0],A[i,j])

		D[i,0]=temp_or


	#Now the D matrix is calculated.

	#Check here if the D Matrix is all 0.
	zero_count=0;
	for i in range(0,(Nx**2)):
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

		break



	#Get the index where D is 1.

	index1=0

	for i in range(0,(Nx**2)):
		if(D[i,0]==1):
			break
		else:
			index1=index1+1


	am[0]=A[index1]

	#Now compute K
	for i in range(0,(Nx**2)):
		temp_or=np.zeros(shape=(1,1));
		temp_and=np.zeros(shape=(1,1));

		for j in range(0,(Nx+Ny)):

			temp_and[0,0]=np.logical_and(A[i,j],am[0,j])

			temp_or[0,0]=np.logical_or(temp_or[0,0],(temp_and[0,0]))

		K[i,0]=np.logical_and(temp_or,D[i,0])



	# We just need to update the matrix A


	for i in range(0,(Nx**2)):
		#temp_or=0;

		for j in range(0,(Nx+Ny)):
			temp_and[0,0]=np.logical_and(am[0,j],K[i,0])
			A[i,j]=np.logical_xor(A[i,j],temp_and[0,0])

	
	K_mat=np.concatenate((K_mat,K),axis=1)
	am_mat=np.concatenate((am_mat,am),axis=0)

	#Now since the A is updated just store the Weights and Am of this iteration
	













