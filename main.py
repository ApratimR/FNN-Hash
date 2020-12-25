import numpy as np
import base64
from tqdm import tqdm

#test data
data  = "qwertyuiopasdfghjklzxcvbnm"


def Neural_hash(data,output_size=12):
	data = str(data)
	data = data.encode(encoding="UTF-8")
	data = base64.b64encode(data)
	data = data.decode(encoding="UTF-8")
	data = list(data)

	#convert string to int
	data = [ord(x) for x in data]


	maxpointer = 0


	#sanity check
	data = list(data)
	output_size=int(output_size)
	input_size = 2*output_size

	if output_size<=0 and output_size>1024:
		raise Exception("invalid output size")

	if len(data)==0:
		raise Exception("no data provided")

	#presaved random array
	rnset = np.genfromtxt("rn.csv",dtype=np.uint8,delimiter=",")


	#pointer used for what variable to use
	pointer = 0

	#allocate some RN to hash as the IV
	the_hash = np.array(rnset[0:output_size],dtype=np.int8)

	#increamenting the pointer
	pointer = (output_size)%len(rnset)




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
	for temp1 in tqdm(range((len(data)//output_size)-1)):

		#rounds
		for _ in range(64):

			temp_hash = np.concatenate((the_hash,data[(temp1*output_size):((temp1+1)*output_size)]),axis=None)
		
			for temp2 in range(output_size):

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

print(temp:=Neural_hash(data,32))