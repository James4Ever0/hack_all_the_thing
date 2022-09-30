from ripgrepy import Ripgrepy
# The Ripgrepy class takes two arguments. The regex to search for and the folder path to search in
expression = "recursive"
filepath = "/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log"
rg = Ripgrepy(expression, filepath) # ignore case? how?
# but this does not include the preprocessor.
# i mean the processor of connecting lines together.
result = rg.with_filename().line_number().ignore_case().json().run().as_dict
# result = rg.with_filename().line_number().ignore_case().json().run() # this will produce list. is it right?

import rich

rich.print(result)