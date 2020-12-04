import time
import os
import urllib.request
import requests

def build(pkg, url, kits, ads, agcs, signingAlias, signingFullname, signingOrganization, signingOrganizationalUnit, signingCountryCode, signingKeyPassword, signingStorePassword, iconUrl):
    folder = str("/tmp/pwa"+str(int(time.time()*1000)))
    icon = folder + "/ic_launcher.png"
    os.system("mkdir " + folder)
    os.system("echo " + agcs + " | base64 --decode > " + folder + "/agconnect-services.json")
    pwacmd = "/usr/bin/node /home/ubuntu/pwa_builder/make_hms.js --package " + pkg + " --url " + url + " --json " + folder + "/agconnect-services.json" + " --output " + folder
    pwacmd += " --signingAlias " + signingAlias
    pwacmd += " --signingFullname " + signingFullname
    pwacmd += " --signingOrganization " + signingOrganization
    pwacmd += " --signingOrganizationalUnit " + signingOrganizationalUnit
    pwacmd += " --signingCountryCode " + signingCountryCode
    pwacmd += " --signingKeyPassword " + signingKeyPassword
    pwacmd += " --signingStorePassword " + signingStorePassword
    try:
        response = requests.get(iconUrl)
        response.raise_for_status()
        urllib.request.urlretrieve (iconUrl, icon)
        pwacmd += " --icon " + icon
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops: There is some error:",err)
    os.system("echo " + pwacmd)
    os.system(pwacmd)
    os.system("cd " + folder + "; /usr/bin/zip -r pwa.zip *")
    return folder

