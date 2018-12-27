#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
file = open("./demo.json")
line = file.readline()

dic = json.loads(line)

js = json.dumps(dic, sort_keys=True, indent=2, separators=(',', ':'))

file.close()

file_write = open("./ur_res.json", "w")
file_write.write(js)
file_write.flush()
file_write.close()