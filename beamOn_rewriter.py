#We're opening a file with the next energy/runNumber that was created in a loop in our shell file
runNfile = open('RunNumber.dat')
#runNumber is the same as energy we are trying to vary. The following line reads it from a created file to a string
runNumber = runNfile.readline()
# Remove the last character of \n added by readline function
runNumber = runNumber.rstrip()
runNfile.close()


readfile = open('beamOn_original.dat', 'r')
writefile = open('beamOn.dat', 'wt')

# We only want to chenge the first line with the number of the run we give to the output file
origline = readfile.readline()
writefile.write(str(runNumber) + '		//Run-number\n')

i = 0
# The lines we want to copy fully. The file has in total 19 lines (with the first we changed)
while i < 19:
  origline = readfile.readline()
  writefile.write(str(origline))
  i = i + 1
  
writefile.close()
readfile.close()
