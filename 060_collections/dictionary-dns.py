# map = dictionary

dns = {
    "www.google.com": "216.58.206.36",
    "www.codevibe.de": "194.117.254.35"
}

# url ist im Format "http://www.codevibe.de/index.html"
def browse(url:str):
    s = url.removeprefix("http://")
    s = s.split("/")[0]
    ip = dns[s]
    print(f"Connecting to IP {ip}...")


browse("http://www.google.com/")