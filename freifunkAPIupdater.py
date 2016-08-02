#!/usr/bin/env python

import json
from json import dumps
import re
from datetime import datetime

jsonfiles = [ 'altdorf.freifunk.net.json', 'landshut.freifunk.net.json' ]
for index, jsonfile in enumerate(jsonfiles):
  print jsonfile
  json_data = open(jsonfile)
  data = json.load(json_data)
  json_data.close()

  try:
    with open('node_stats', 'r') as fn:
      numbers = re.findall(r'\d+', fn.readline())
      nodes = numbers[2]
  except Exception as ex:
    exit(ex)

  data["state"]["lastchange"] = datetime.now().isoformat('T')
  data["state"]["nodes"] = int(nodes)
  print data["state"]["lastchange"]
  print data["state"]["nodes"]

  try:
    with open(jsonfile, 'w') as fn:
      fn.write(dumps(data, indent=4))
      fn.close()
  except Exception as ex:
    exit(ex)

