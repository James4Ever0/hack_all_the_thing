demo={"abc":'defghiklm'}

mdict=[demo]*3
mdict={k:mdict for k in "ghi"}

import pyjq

expression="path(..)"
values=pyjq.all(expression,mdict)
print("mdict:",mdict)
print("values:", values)
