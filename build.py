import subprocess
import time


def build(url):
    folder = str("/tmp/pwa"+str(int(time.time()*1000)))
    subprocess.run(["/usr/bin/pwabuilder", url, "-d", folder])
    subprocess.run(["/usr/bin/zip", "-r", folder+"/pwa.zip", folder+"/"])
    return folder+"/pwa.zip"

