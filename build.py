import subprocess
import time
import os


def build(url):
    folder = str("/tmp/pwa"+str(int(time.time()*1000)))
    os.system("/usr/bin/pwabuilder " + url + " -d " + folder)
    # subprocess.run(["/usr/bin/pwabuilder", url, "-d", folder])
    os.system("cd " + folder + "; /usr/bin/zip -r pwa.zip *")
    # subprocess.run(["/usr/bin/zip", "-r", folder+"/pwa.zip", folder+"/"])
    return folder

