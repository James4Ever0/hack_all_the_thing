# use itertools?
# permutations, remember the hack though.
# there are not so many repeated chars in the damn password. maybe you got this right.
import itertools
pwchars="0123456789abcdefghijklmnopqrstuvwxyz"
pwchars=list(pwchars)
# where is the tool generate chars from regex? that is used in my lazero project isn't it?
import progressbar as pb
with open("passwd.txt","w") as f:
    for l in pb.progressbar(range(4,8)):
#        pwlist=[]
        for comb in itertools.product(pwchars, repeat=l):
            pwd=''.join(comb)
#            pwlist.append(pwd)
            f.write(pwd+'\n')
