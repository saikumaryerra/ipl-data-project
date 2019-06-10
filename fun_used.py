import matplotlib.pyplot as plt
def sort_dict(dic):
	output={}
	for key in sorted(dic):
		output[key]=dic[key]
	return output

def data_count(x,reader_name):

	#using Lists
	# output_x=[]
	# output_y=[]
	# for i in reader_name:
	# 	if i[x] in output_x:
	# 		j=output_x.index(i[x])
	# 		output_y[j]=output_y[j]+1
	# 	else:
	# 		output_x.append(i[x])
	# 		output_y.append(1)
	# return output_x,output_y

	#using dictionaries
	output={}
	for i in reader_name:
		if i[x] in output.keys():
			output[i[x]]=output[i[x]]+1
		else:
			output[i[x]]=1
	# plt.bar(output.keys(),output.values())
	# plt.show()
	# y={}
	# for key in sorted(output):
	# 	y[key]=output[key]
	y=sort_dict(output)
	return y
