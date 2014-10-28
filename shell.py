import os
import sys
import string

def parser(line):
	linelist = line.split()
	command = linelist[0]
	numargs = len(linelist) - 1
	arg = linelist[0:numargs+1]
	
	try:
		inputredirect = linelist.pop(linelist.index("<") + 1)
	except:
		inputredirect = None
    
	try:
		outputredirect = linelist.pop(linelist.index (">") + 1)
	except:
		outputredirect = None
		
	return  inputredirect, outputredirect, arg, command, linelist
	
def executor(command, arguments, inputredirect, outputredirect):
	#try:
	pid = os.fork()
	if pid == 0:
		Redirector(inputredirect, outputredirect)
		os.execvp(command, arg)
	os.wait()
		
	#except:
	#	print("%s\n" % "Invalid Command")

def Redirector(inputredirect, outputredirect):
	fileop = None
	if outputredirect != None:
		#try:
		fw = open(outputredirect, "w")
		os.dup2(fw.fileno(), sys.stdout.fileno())
		fileop = "out"
		#except:
		#print("File %s could not be opened for writing\n" % outputredirect)
	if inputredirect != None:
		#try:
		fw = open(inputredirect, "r")
		os.dup2(fw.fileno(), sys.stdin.fileno())
		fileop = "in"
		#except:
		#	print("File %s could not be opened for reading\n" % inputredirect)
	
	return fileop


##################################################### Main #####################################################

while True:
	line = raw_input("$")														#Receives Stdin, prints the argument to stdout
		
	inputredirect, outputredirect, arg, command, linelist = parser(line)  		#Run Parser
	#fileop = Redirector(inputredirect, outputredirect)  						#Run File Redirector
	
	if inputredirect != None:
		del arg[linelist.index("<")]
		arg.remove(inputredirect)												#Removes the file name and redirection operator from the argument string
	elif outputredirect != None:
		del arg[linelist.index(">")]
		arg.remove(outputredirect)
	
	print(outputredirect)														#DEBUG
	executor(command, arg, inputredirect, outputredirect) 														#Run Command execution

