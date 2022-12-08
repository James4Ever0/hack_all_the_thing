email="randomvoidmail@foxmail.com"
key="637675539d539b208171dbec448c1159"
import os

# the log4j is protected in zoomeye. don't know what the fuck is going on.

os.environ["https_proxy"]=""
import fofa

if __name__ == "__main__":
    # email, key = ('test@test.com', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  
    # when you request fofa with free account,you won't get shit.
    client = fofa.Client(email, key)               
    query_str = 'header="thinkphp" || header="think_template"'                           
    data = client.search(query_str, size=100, page=1, fields="ip,city") 
    print("data?",data)
    for ip, city in data["results"]:
        print("%s,%s" % (ip, city))
