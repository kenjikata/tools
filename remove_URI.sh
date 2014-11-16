#!/bin/bash
# URL
perl -p -i.bak1 -e 's/https?:\/\/[-_.!~*a-zA-Z0-9;\/?:\@&=+$,%#]+//g' aa.txt
# email
perl -p -i.bak2 -e 's/^[a-zA-Z0-9._-]+\@[a-zA-Z0-9.-]+//g' aa.txt
