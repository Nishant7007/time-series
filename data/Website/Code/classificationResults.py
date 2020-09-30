import pickle as pkl

dict = {"Lasalgaon" : "Normal",
	"Bangalore" : "Normal",
	"Kalyani" : "Normal",
	"Azadpur" : "Normal",
	"Bijnaur" : "Normal"}

file = open('classificationResults.p', 'wb')

# dump information to that file
pkl.dump(dict, file)

