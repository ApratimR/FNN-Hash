import numpy as np
import base64


def FNNH(data="",hash_size=16,rounds = 64):
	'''
	FNNH(Flexible Neural Network Hash)
	-----
	A flexible output size Hash Algorithm that uses Neural Network structure.

	data = the string for which the hash needs to be calculated (Default = "")

	hash_size = the size of hash (Default = 16)

	rounds = the number of rounds per block (Default = 64)

	'''

	data = str(data)
	data = data.encode(encoding="UTF-8")
	data = base64.b64encode(data)
	data = data.decode(encoding="UTF-8")
	data = list(data)

	#convert string to int
	data = [ord(x) for x in data]

	#rounds check
	if isinstance(rounds,int)==True:
		if rounds<=0:
			print("invalid rounds input.set to default size of 64")
			rounds=64
	else:
		print("invalid data type.hash size set to default size of 16")
		rounds=64

	#hash size check
	if isinstance(hash_size,int)==True:
		if hash_size<=0 and hash_size>1024:
			print("invalid hash_size input.set to default size of 16")
			hash_size=16
	else:
		print("invalid data type.hash size set to default size of 16")
		hash_size=16

	#sanity check
	data = list(data)
	input_size = 2*hash_size



	#presaved random array
	rnset = np.array([16,25,46,14,35,23,23,9,62,26,44,13,59,19,49,27,14,47,53,2,52,39,35,39,63,13,14,9,21,12,7,9,49,12,63,48,54,6,20,57,42,20,1,8,47,5,33,41,23,56,29,55,50,42,38,13,16,60,62,39,24,59,1,43,4,49,56,21,0,43,25,36,58,29,41,33,45,6,28,19,36,32,9,10,18,53,5,0,25,55,33,41,36,24,11,52,41,20,60,2,17,47,50,42,38,21,5,16,3,58,40,45,26,15,36,61,17,21,39,5,13,26,21,33,25,18,51,22,22,36,49,41,57,11,7,35,44,28,28,18,1,8,7,13,46,14,33,11,4,59,49,15,37,20,7,0,7,39,58,1,6,29,54,31,28,17,61,20,3,25,29,56,30,4,58,62,2,41,31,34,19,40,16,7,3,18,27,21,9,61,57,14,11,7,15,16,23,24,42,40,4,62,34,28,38,1,49,7,63,19,23,27,4,38,19,2,40,27,53,60,55,3,51,49,47,2,3,18,2,57,39,3,57,6,48,28,1,26,28,20,28,8,50,60,8,59,31,26,37,17,8,21,20,59,46,13,60,14,27,18,12,10,45,40,55,27,46,55,33,61,40,18,31,51,12,17,57,22,59,20,26,16,28,25,26,36,33,5,28,6,0,46,3,21,46,0,54,41,31,21,55,48,42,7,60,20,5,59,56,34,50,54,40,27,0,6,47,32,21,27,17,42,11,10,27,16,19,22,6,58,43,55,42,44,6,11,42,18,3,36,2,37,23,1,46,37,41,9,51,9,5,15,32,1,32,27,18,30,14,59,16,22,63,10,13,31,46,13,35,58,55,30,3,37,24,52,33,5,59,27,0,35,25,0,15,30,32,52,2,51,18,8,25,9,2,39,57,58,39,29,31,6,35,19,62,47,50,59,49,59,62,32,50,0,25,60,25,22,54,19,6,46,14,41,41,48,55,15,8,57,4,0,17,13,49,4,59,22,36,2,17,58,17,31,47,34,42,12,46,10,19,31,27,2,40,48,33,1,22,17,9,35,5,50,1,38,4,0,56,58,31,63,40,62,42,4,18,0,42,37,11,27,61,10,50,44,54,38,37,63,55,23,61,31,6,2,43,26,8,26,16,59,2,54,22,3,60,26,19,19,44,40,25,20,3,4,44,27,12,61,49,33,35,12,33,19,53,53,57,26,17,24,36,28,53,28,62,26,20,30,1,10,22,19,29,23,45,41,22,59,7,49,20,60,59,19,47,41,12,17,50,52,25,5,15,9,15,14,48,12,62,35,61,54,2,6,36,9,49,61,3,1,17,61,49,60,0,20,57,10,17,44,61,22,54,36,55,29,14,20,22,43,18,60,16,44,56,12,36,50,13,13,58,0,32,14,28,6,14,55,9,35,38,63,34,58,7,58,54,32,55,20,54,20,43,58,14,30,38,51,3,22,60,38,61,36,7,1,42,45,53,25,5,35,33,11,27,17,56,38,38,56,35,15,48,34,21,36,39,43,2,61,17,6,45,21,4,55,14,21,29,9,46,45,1,7,48,17,33,35,52,16,9,61,50,52,40,61,43,45,47,35,57,23,34,33,7,5,43,57,20,26,25,4,7,25,13,41,14,39,37,19,3,25,60,42,5,39,3,60,3,3,4,42,2,23,62,42,7,52,45,49,0,19,43,8,13,55,35,35,62,29,34,36,57,8,52,7,8,39,35,49,51,39,5,13,24,22,46,13,28,4,2,22,24,50,17,5,23,23,0,2,40,3,38,25,8,31,4,55,25,48,1,18,42,4,53,38,61,33,58,62,1,2,29,45,6,60,11,5,59,33,30,40,31,59,22,18,58,8,13,38,41,38,43,43,3,57,61,47,50,62,23,53,63,30,41,17,56,1,59,11,61,0,57,55,7,4,3,54,38,39,63,28,32,0,60,47,24,4,46,36,20,48,61,51,18,47,49,3,18,49,20,1,50,44,18,42,2,22,49,63,47,9,3,3,41,29,51,55,40,26,32,52,45,60,34,18,37,50,10,0,2,18,51,38,63,52,54,47,13,39,50,6,50,44,44,19,23,49,18,35,35,32,45,53,51,8,47,16,53,0,24,50,52,25,49,27,21,37,36,6,2,46,32,26,20,46,3,4,28,53,63,2,48,39,23,9,63,3,35,25,46,45,15,49,48,24,17,52,59,1,54,15,50,28,56,55,24,0,36,51,19,27,44,46,20,59,6,41,27,55,58,3,53,28,48,14,63,47,55,44,4,52,38,20,32,54,18,61,32,41,48,60,23,9,8,6,40,63,55,7,21,47],dtype=np.int8)


	#pointer used for what variable to use
	pointer = 0

	#allocate some RN to hash as the IV
	the_hash = np.array(rnset[0:hash_size],dtype=np.int8)

	#increamenting the pointer
	pointer = (hash_size)%len(rnset)




	amount_to_pad = input_size-(len(data)%input_size)
	
	data.extend([0]*amount_to_pad)
	
	#sums up all the input layer nodes
	def sum_with_weight(datainp,pointer):
		temp_sum = 0
		maxpointer = 0
		for temp in datainp:
			temp_sum = temp_sum + (temp * rnset[pointer])
			pointer = (pointer + 1)%len(rnset)

		return temp_sum,pointer

	def strlookup(the_list):
		refstr="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
		temp_str=str()
		for temp1 in the_list:
			temp_str+=refstr[temp1]
		return temp_str


	def rnset_messup(data_to_messup,seed):
		data_to_messup = np.roll(data_to_messup,data_to_messup[419]+seed)
		data_to_messup = (data_to_messup+data_to_messup[311]+seed)%64

		data_to_messup = np.roll(data_to_messup,data_to_messup[982]+seed)
		data_to_messup = (data_to_messup+data_to_messup[269]+seed)%64
		
		data_to_messup = np.roll(data_to_messup,data_to_messup[1006]+seed)
		data_to_messup = (data_to_messup+data_to_messup[1017]+seed)%64
		
		data_to_messup = np.roll(data_to_messup,data_to_messup[849]+seed)
		data_to_messup = (data_to_messup+data_to_messup[736]+seed)%64
		
		data_to_messup = np.roll(data_to_messup,data_to_messup[371]+seed)
		data_to_messup = (data_to_messup+data_to_messup[599]+seed)%64
		
		return data_to_messup

	#the main hash loop
	for temp1 in range((len(data)//hash_size)-1):

		#rounds
		for _ in range(rounds):

			temp_hash = np.concatenate((the_hash,data[(temp1*hash_size):((temp1+1)*hash_size)]),axis=None)
		
			for temp2 in range(hash_size):

				weight,pointer = sum_with_weight(temp_hash,pointer)

				if weight%64 <= the_hash[temp2] :
					pointer = (pointer+1)%len(rnset)
					the_hash[temp2]=rnset[pointer]
					
				else:
					pointer = (pointer+2)%(len(rnset))
					the_hash[temp2]=rnset[pointer]
				
				

			#mutate the rnadom number set
			rnset=rnset_messup(rnset,the_hash[0]+amount_to_pad)
		
		rnset = rnset_messup(rnset,the_hash[0])

	
	the_hash_str=strlookup(the_hash)
	return the_hash_str

def main():

	stringdata = str(input("Enter the Data for which you want to calculculate the hash : "))
	sizeofoutput=int(input("Enter the size of hash you want to generate (NOTE:max aloted size is 1024) : "))
	rounds = int(input("Enter the number of rounds : "))
	print("Hash of the given data is :",FNNH(stringdata,sizeofoutput,rounds))


if __name__ == "__main__":
	main()