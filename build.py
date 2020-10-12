import subprocess
import time

def build(url):
    folder = str("/tmp/pwa"+str(int(time.time()*1000)))
    subprocess.run(["/home/ubuntu/.nvm/versions/node/v14.4.0/bin/pwabuilder", url, "-d", folder])
    return url

