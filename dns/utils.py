import ipaddr

def ip_to_int(ip):
    return int(ipaddr.IPV4Address(ip))

def int_to_ip(ip):
    return str(ipaddr.IPV4Address(ip))
