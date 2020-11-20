import time
import os


def build(pkg, url, kits, ads, agcs, signingAlias, signingFullname, signingOrganization, signingOrganizationalUnit, signingCountryCode, signingKeyPassword, signingStorePassword):
    folder = str("/tmp/pwa"+str(int(time.time()*1000)))
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
    os.system("echo " + pwacmd)
    os.system(pwacmd)
    os.system("cd " + folder + "; /usr/bin/zip -r pwa.zip *")
    return folder

