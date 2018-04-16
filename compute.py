import csv

def return_output(inputFile, outputFile):
	ans = 0	
	
	with open(inputFile) as files:
		reader = csv.reader(files, delimiter=' ')
	
		out = []
	
		for row in reader:
			out.append(row)
		try:	
			numOne = int(out[1][0])
			numTwo = int(out[2][0])
		except:
			print("Enter integers only")
			return

		if out[0][0] == 'Multiply':
			ans = numOne*numTwo	
		elif out[0][0] == 'Divide':
			ans = numOne/numTwo
		else:
			print("use either 'Multiply' or 'Divide'")
			return

	filesTwo = open(outputFile, 'w')
	filesTwo.write(str(ans) + '\n')
	filesTwo.close()

inputFile = 'input.txt'
outputFile = 'output.txt'

return_output(inputFile, outputFile)
