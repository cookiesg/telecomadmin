import json
from cmath import e
from prettytable import PrettyTable
import requests

log = '''
  __         .__                                          .___      .__        
_/  |_  ____ |  |   ____   ____  ____   _____ _____     __| _/_____ |__| ____  
\   __\/ __ \|  | _/ __ \_/ ___\/  _ \ /     \\__  \   / __ |/      \|  |/    \ 
 |  | \  ___/|  |_\  ___/\  \__(  <_> )  Y Y  \/ __ \_/ /_/ |  Y Y  \  |   |  \\
 |__|  \___  >____/\___  >\___  >____/|__|_|  (____  /\____ |__|_|  /__|___|  /
           \/          \/     \/            \/     \/      \/     \/        \/ 
'''


def getPwd(token, mac):
    url = "https://nos9.189cube.com/device/api?token={}&MAC={}".format(
        token, mac)

    data = {
        "Params": [],
        "MethodName": "GetTAPasswd",
        "RPCMethod": "CallMethod",
        "ObjectPath": "/com/ctc/igd1/Telecom/System",
        "InterfaceName": "com.ctc.igd1.SysCmd",
        "ServiceName": "com.ctc.igd1"
    }
#heads抓包获得
    heads = {
        "Content-Type": "application/json",
        "SDKVersion": "",
        "phoneNum": "",
        "phoneOS": "",
        "systemVersion": "",
        "AppKey": "",
        "User-Agent": ""
    }
    results = requests.post(url=url,data=json.dumps(data),headers=heads)
    
    try:
        return json.loads(results.text)["Params"][0]
    except Exception:
        return 

if __name__ == "__main__":
    print(log)
    token = "" #token必填
    mac = ""   #mac必填
    pwd = getPwd(token=token, mac=mac)
    x = PrettyTable()
    x.add_column("user",["telecomadmin"])
    x.add_column("pwd",[pwd])
    print(x)