#!/bin/bash

git pull

python node_stats.py > node_stats
python freifunkAPIupdater.py

for i in altdorf landshut; do
	sed -i "s| $||" ${i}.freifunk.net.json
done

git add altdorf.freifunk.net.json
git add landshut.freifunk.net.json
git commit -m "updated number of nodes"
git push git@github.com:tecff/freifunk.net-API.git
git fetch origin
