portrule = function(host, port) 
	    return port.protocol == "tcp" and port.number == 8022 and port.state == "open" 
    end
action = function (host, port)
	print("test script")
	return "hello world"
end
