from ripgrepy import Ripgrepy
# The Ripgrepy class takes two arguments. The regex to search for and the folder path to search in
expression = "recursive"
filepath = "/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log"
rg = Ripgrepy(expression, filepath) # ignore case? how?
# but this does not include the preprocessor.
# i mean the processor of connecting lines together.
result = rg.with_filename().line_number().ignore_case().json().run().as_dict
# result = rg.with_filename().line_number().ignore_case().json().run() # this will produce list. is it right?

# import rich
for elem in result:
    searchType=elem['type']
    data = elem['data']
    path_text = data['path']['text']
    line_text = data['lines']['text']
    line_number = data['lines']['line_number']
    submatches = data['submatches']
    matched_word_set = set(match['match']['text'] for match in submatches)
# rich.print(result)
#     {
#         'type': 'match',
#         'data': {
#             'path': {
#                 'text': 
# '/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log'
#             },
#             'lines': {
#                 'text': '       erator will be efficient. In the example below the 
# recursive call by _range\n'
#             },
#             'line_number': 2268,
#             'absolute_offset': 87045,
#             'submatches': [{'match': {'text': 'recursive'}, 'start': 58, 'end': 67}]
#         }
#     }