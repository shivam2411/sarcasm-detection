text_file = open("sar.txt", "r")
lines = text_file.readlines()
for line in lines:
	print line
#print len(lines)
text_file.close()