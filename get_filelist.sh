#!/bin/bash
for file in `ls -l *.txt| awk '{print $9}'`
do
  cat $file >> aa.txt
done

for file in `ls -1 *.txt`
do
  cat $file >> bb.txt
done
