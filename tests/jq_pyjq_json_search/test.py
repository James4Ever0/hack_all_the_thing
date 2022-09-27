demo={"abc":'defghiklm'}

mdict=[demo]*3
mdict={k:mdict for k in "ghi"}

import pyjq

mdict2 = {1:"def",2:"ghi",3:"defghi",4:["def","ghi"]}
# key of json dict must be string.
import json
mdict2=json.loads(json.dumps(mdict2))
mdict3={"Abc":"dEF"}
#expression='.. try contains("def") catch false'
#expression='paths(type=="string")'
#
#expression='paths(try contains("def") catch false)' # a simple keyword search tool.
expression='select(type == "string")'
# next we need 'lower'
values=pyjq.all(expression,mdict3)
#values=pyjq.all(expression,mdict2)
#values=pyjq.all(expression,mdict)
print("mdict:",mdict)
print("values:", values)
