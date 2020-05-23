from requests import get
ip = open()
ip_new = get('https://api.ipify.org').text
while ip != ip_new:
    ip = get('https://api.ipify.org').text
    print ('My public IP address is:', ip)