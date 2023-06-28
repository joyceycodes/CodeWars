# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    url = url.split(".")
    if "www" in url[0]:
        return url[1]
    elif "http://" in url[0]:
        return url[0][7:]
    elif "https://" in url[0]:
        return url[0][8:]
    else:
        return url[0]

# top solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]