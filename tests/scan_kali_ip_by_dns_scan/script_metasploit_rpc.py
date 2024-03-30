from pymetasploit3.msfrpc import MsfRpcClient
PWD = "lazero"

client = MsfRpcClient(password = PWD, ssl=True) # requires ssl by default. otherwise won't work

# the module structure must be identical to the one at , otherwise it will not load.
client.core.addmodulepath("/root/Desktop/works/hack_all_the_thing/tests/scan_kali_ip_by_dns_scan/custom_msf_module") # return new stats.

# search api will not work.
# client.modules.search("test_payload")
# but loading the new module works.
# client.modules.use("payload", "test_payload")

# load or loadpath will not work.
# call_result = client.call("loadpath", opts=['/root/Desktop/works/hack_all_the_thing/tests/scan_kali_ip_by_dns_scan/custom_msf_module'])

# print("call result:") # dict, error
# dict_keys(['error', 'error_class', 'error_string', 'error_backtrace', 'error_message'])
# print(call_result)
# payload_module = client.modules.use("payload", "/root/Desktop/works/hack_all_the_thing/tests/scan_kali_ip_by_dns_scan/custom_msf_module/test_payload.rb")
# breakpoint()

exploit_id = "exploit/multi/samba/usermap_script"
exp_mod = client.modules.use("exploit", exploit_id)
# breakpoint()
exp_info = exp_mod.info # has info about the exploit.

# with keys:
# ['type', 'name', 'fullname', 'rank', 'disclosuredate', 'description', 'license', 'filepath', 'arch', 'platform', 'authors', 'privileged', 'references', 'targets', 'default_target', 'stance', 'options']

# you may be interested in the source code specified by filepath

# 4444
# client.modules.use("payload", "cmd/unix/reverse").info['options']['LPORT']

# payload source code:
print(open(client.modules.use("payload", "cmd/unix/reverse").info['filepath'],'r').read())

# question: how to write and load custom modules?
# answer: write it in structured directory, then load it with client.core.addcustommodule(absolute_path_to_module)