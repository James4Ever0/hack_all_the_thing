portrule = function(host, port) 
	print("portrule",host,port)
	    return port.protocol == "tcp" and port.number == 8022 and port.state == "open" 
    end

-- there can be multiple rules.

action = function (host, port)
	print("test script")
	return "hello world"
end
