#!/bin/python
import urllib2
import json
contents = urllib2.urlopen("http://localhost:9000/info.json").read()

json_content = json.loads(contents)
print(json_content)

