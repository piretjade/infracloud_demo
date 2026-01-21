from netmiko import ConnectHandler
from openpyxl import Workbook, load_workbook
import datetime
import os

# Gegevens van het toestel
device = {
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec9k.cisco.com",
    "port": 22,
    "username": "jade.piret",
    "password": "43JxCmOSInJU2_w_"
}

def main():
    command = "show version"
    excel_file = "show_version.xlsx"

    print(f"Verbinding maken en uitvoeren: {command}")
    sshCli = ConnectHandler(**device)
    output = sshCli.send_command(command)
    sshCli.disconnect()

    wb = Workbook()
    ws = wb.active
    ws.title = "show version"

    # Info bovenaan
    ws.append(["Command", command])
    ws.append(["Timestamp", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    ws.append([])  # lege rij
    ws.append(["Output"])  # kolomtitel

    # Elke regel van de output in één Excel-rij
    for line in output.splitlines():
        ws.append([line])

    wb.save(excel_file)
    print(f"Excel-bestand aangemaakt: {excel_file}")

if __name__ == "__main__":
    main()