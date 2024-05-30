#!/bin/bash

for((number=0;number<=60;number=number+1)); do

python << END

file = open('RunNumber.dat', 'w')
file.write(str($number))
file.close()

END

python beamOn_rewriter.py
python electronGun_rewriter.py

. ./setupBuild.sh makefile
echo "SetupBuild is done"
./compileApp.sh makefile
echo "CompileApp is done"
./G4d2o
echo "G4d2o is done"
wait

echo "run: $number done"
done
exit 0;
