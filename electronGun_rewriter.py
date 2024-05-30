#We're opening a file with the next energy/runNumber that was created in a loop in our shell file
runNfile = open('RunNumber.dat')
#runNumber is the same as energy we are trying to vary. The following line reads it from a created file to a string
runNumber = runNfile.readline()
runNumber = runNumber.rstrip()
runNfile.close()

# I copied the original G4d2oElectronGun.cc to a backup code used as a template to copy from, called gun_original.cc
readfile = open('gun_original.cc', 'r')
writefile = open('src/G4d2oElectronGun.cc', 'wt')

i = 0
# The lines we want to copy fully
while i < 94:
  origline = readfile.readline()
  writefile.write(str(origline))
  i = i + 1
# The line with energy we want to change. The changed energy is the same as "runNumber" and varies from 1 to 60 MeV
if i == 94:
  writefile.write('    sourceEnergy = (' + str(runNumber) + '.0000)*MeV;\n')
  origline = readfile.readline()
  i = i + 1  
# The rest of lines we want to copy fully
while i < 146:
  origline = readfile.readline()
  writefile.write(str(origline))
  i = i + 1
  
writefile.close()
readfile.close()
