
puts('hello world')
#result = run_single("search cve:2008")
# where is the damn search thing?
#puts(result) # return true
#check commandline and search/grep/ripgrep here:
#/opt/metasploit-framework/embedded/framework

# you are going to dig into the msf source code.
# can you run bare ruby script instead of this heavy shit?
search_string = Msf::Modules::Metadata::Search.parse_search_string("cve:2008")
result = Msf::Modules::Metadata::Cache.instance.find(search_string)
# there used to be an @ before.
puts("search end")
print(result)
exit
