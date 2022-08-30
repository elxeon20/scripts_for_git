import concurrent.futures
import argparse
import socket
import time

common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "TELNET",
    "25": "SMTP",
    "53": "DNS",
    "69": "TFTP",
    "80": "HTTP",
    "109": "POP2",
    "110": "POP3",
    "123": "NTP",
    "137": "NETBIOS-NS",
    "138": "NETBIOS-DGM",
    "139": "NETBIOS-SSN",
    "143": "IMAP",
    "156": "SQL-SERVER",
    "389": "LDAP",
    "443": "HTTPS",
    "546": "DHCP-CLIENT",
    "547": "DHCP-SERVER",
    "995": "POP3-SSL",
    "993": "IMAP-SSL",
    "2086": "WHM/CPANEL",
    "2087": "WHM/CPANEL",
    "2082": "CPANEL",
    "2083": "CPANEL",
    "3306": "MYSQL",
    "8443": "PLESK",
    "10000": "VIRTUALMIN/WEBMIN",
}


pars = argparse.ArgumentParser()
pars.add_argument("host", help="host IP")
pars.add_argument("--start", "-s", help="Start Port")
pars.add_argument("--end", "-e", help="End Port")
arguments = pars.parse_args()
host = arguments.host

if arguments.start:
    start_port = int(arguments.start)
else:
    start_port = 0

if arguments.end:
    end_port = int(arguments.end)
else:
    end_port = 65535

print("Сканирование %s портов.\n" % host)


def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    sock.connect((host, port))
    try:
        port_name = " (%s)" % common_ports.get(str(port), "")
        if port_name == " ()":
            port_name = ""
        ext_port_name = "%s%s" % (str(port), port_name)
    except KeyError:
        ext_port_name = str(port)
    print(" - Port {} is open".format(ext_port_name))


t1 = time.perf_counter()

ports = [j for j in range(start_port, end_port + 1)]

# количество потоков
with concurrent.futures.ThreadPoolExecutor(max_workers=160) as executor:
    executor.map(scan, ports)

t2 = time.perf_counter()
print("Сканирование %d портов завершено за %s сек." % (len(ports) , str(t2 - t1)))