#!/bin/bash

git pull
python freifunkAPIupdater.py

git add altdorf.freifunk.net.json
git add landshut.freifunk.net.json
git commit -a -m "updated number of nodes"
git push git@github.com:tecff/freifunk.net-API.git
