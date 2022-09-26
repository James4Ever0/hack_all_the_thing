portrule = function(host, port) 
	    return port.protocol == "tcp" and port.number == 80 and port.state == "open" 
    end
action = function (host, port)
	print("test script")
	return "hello world"
end
