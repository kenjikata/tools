#!/bin/bash
inputfile=aa.txt
word=`cat $inputfile`
command=``

## Example
$command << EOF >> result.txt
$word
EXIT
EOF
