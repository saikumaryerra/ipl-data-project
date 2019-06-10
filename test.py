# import csv
# with open('matches.csv','r') as matches_csv:
# 	matches_reader = csv.reader(matches_csv)
# 	for row in matches_reader:
# 		print (row)


# import matplotlib.pyplot as plt

# a = [1,2,3,4,5,6,7,8,9]
# b = [10,20,30,40,50,60,70,80,90]
# plt.plot(a,b)
# plt.show()


import matplotlib.pyplot as plt
# plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example one")

plt.bar([2, 4, 6, 8, 10], [18, 6, 2, 5, 6], label="Example two", color='g')
plt.bar([2, 4, 6, 8, 10], [10, 12, 2, 5, 6], label="Example two", color='b')
# plt.bar([2, 4, 5, 7, 9], [10, 2, 7, 8, 2], label="Example 3", color='r')
# plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line! Whoa')

plt.show()
