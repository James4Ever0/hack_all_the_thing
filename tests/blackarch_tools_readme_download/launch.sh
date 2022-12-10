# bash download_main_list.sh # download the target html. in a single page.
# since we have it we comment it out.

# now we create CSV with pandas.
python3 extract_tools.py

# we download and create excerpts from unique URL? use some database?
python3 visit_webpage_save_html.py