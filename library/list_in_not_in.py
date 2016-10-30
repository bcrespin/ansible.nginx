#!/usr/bin/python

import json
import shlex
from ansible.module_utils.basic import *

DOCUMENTATION = '''
---
module: list_in_not_in
version_aded: 0.1
short_description: compare list for element in or not in  both lists
description: 
 - if is_in is true (default), return elements of list1 present in list2, if is_in is false, return elements of list1 not present in list2
options:
  list1:
    description:
      - TODO
	required : true
  list2:
    description:
      - TODO
	required : true	
  is_in:
    description:
      - TODO
	required : false
	default: true
author : "Brice C"	
'''

EXAMPLES = '''
# to return elements of [ 1,2,3,4] NOT in [ 2,3,4]  ( should be [1])
- list_in_not_in [ 1,2,3,4] [ 2,3,4]  is_in=false

# to return elements of [ 1,2,3,4] in [ 2,3,4]  ( should be [2,3,4])
- list_in_not_in [ 1,2,3,4] [ 2,3,4]  
'''

RETURN = '''
items:
  description:  elements in or not in both list depending of variable in
  type: list
  return: always
'''


def main():
    res = []
	
    fields = {
	   "list1": {"required":True, "type": "list"},
	   "list2": {"required":True, "type": "list"},
	   "is_in":  {"required":False," default": True, "type": "bool"},
    }
    module = AnsibleModule(argument_spec=fields)
    
    is_in=module.params['is_in'] 
    if (len(fields['list1']) >= len(fields['list2'])):
      my_array1=module.params['list1']
      my_array2=module.params['list2']
    else:
      my_array1=module.params['array2']
      my_array2=module.params['array1']
    i=0
    while i <  len(my_array1):
	  isFound=0
	  j=0
	  while j< len(my_array2) and isFound == 0 :
		if my_array1[i] == my_array2[j]:
		  isFound=1
		j=j+1
	  if isFound == 1:
		if is_in == True:
		  res=res + [my_array1[i]]
	  if isFound == 0:
		if is_in == False:
		  res=res + [my_array1[i]]
	  i=i+1
    print json.dumps({ "items": res}) 

if __name__ == '__main__':  
    main()
