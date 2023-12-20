import re
import requests
import netmiko
from netmiko import ConnectHandler

class Cisco_Devices():
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def uptime(self):
        ip_list = ['172.30.8.171']

        for j in ip_list:
            login= ConnectHandler(device_type="cisco_ios", ip=j, username = self.username, password = self.password)

            req = login.send_command("sho version")
            regex1 = re.findall((r'\S+\suptime\sis\s(.+)'), str(req))
            print(regex1)


switch_state = Cisco_Devices('ipbo','ipbo').uptime()