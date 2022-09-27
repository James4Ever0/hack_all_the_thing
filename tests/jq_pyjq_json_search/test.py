demo={"abc":'defghiklm'}

mdict=[demo]*3
mdict={k:mdict for k in "ghi"}

import pyjq

mdict2 = {1:"def",2:"ghi",3:"defghi",4:["def","ghi"]}
# key of json dict must be string.
import json
mdict2=json.loads(json.dumps(mdict2))
mdict3={"Abc":"dEF","a":[1,2,{'de':{'t':'uwy'}}]}
#expression='.. try contains("def") catch false'
#expression='paths(type=="string")'
#
#expression='paths(try contains("def") catch false)' # a simple keyword search tool.
#expression='walk(if type == "string" then ascii_upcase else . end)'
# next we need 'lower'
#expression='to_entries'
#[[{'key': 'Abc', 'value': 'dEF'}, {'key': 'a', 'value': [1, 2, {'de': {'t': 'uwy'}}]}]]
# not so good?
expression='select(type == "string"'
values=pyjq.all(expression,mdict3)
#values=pyjq.all(expression,mdict2)
#values=pyjq.all(expression,mdict)
#print("mdict:",mdict)
#print("mdict2:",mdict2)
print("mdict3:",mdict3)
print("values:", values)
