# you decide not to remove stopwords?
# it does not affect my highlighting process anyway.

import en_core_web_sm
with open(".json",'r') as f:
    content = f.read()
    test_data = json.loads(content)