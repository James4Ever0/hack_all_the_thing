common problem over creating custom metasploit modules:

    Attempting to create a module in $HOME/.msf4/modules/. This won’t work because you need to specify if it’s an exploit or a payload or something. Check ls /opt/metasploit/apps/pro/msf3/modules/ (or where your install of Metasploit lives).
    Attempting to create a module in $HOME/.msf4/modules/auxiliary/. This won’t work because you need at least one level of categorization. It can be new, like auxiliary/0day/, or existing, like auxiliary/scanner/scada/.
    Attempting to create a module in $HOME/.msf4/exploit/ or $HOME/.msf4/posts/. Note the pluralization of the directory names; they’re different for different things. Exploits, payloads, encoders, and nops are plural, while auxiliary and post are singular.

full reference: https://docs.metasploit.com/docs/using-metasploit/intermediate/running-private-modules.html