demo={"abc":'defghiklm'}

mdict=[demo]*3
mdict={k:mdict for k in "ghi"}

import pyjq

#expression='.. try contains("def") catch false'
#expression='paths(type=="string")'
#
expression='paths(try contains("def") catch false)'
values=pyjq.all(expression,mdict)
print("mdict:",mdict)
print("values:", values)
