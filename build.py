import time
import os
import base64


def build(url, kits, ads, agcs):
    folder = str("/tmp/pwa"+str(int(time.time()*1000)))
    os.system("/usr/bin/pwabuilder " + url + " -d " + folder)
    os.system("echo " + agcs + " | base64 --decode > " + folder + "/agconnect-services.json")
    os.system("cd " + folder + "; /usr/bin/zip -r pwa.zip *")
    return folder

