from ripgrepy import Ripgrepy
# The Ripgrepy class takes two arguments. The regex to search for and the folder path to search in
expression = "recursive"
filepath = "/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log"
rg = Ripgrepy(expression, filepath) # ignore case? how?
result = rg.with_filename().line_number().ignore_case().run()

