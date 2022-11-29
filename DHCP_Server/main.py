reserved = {}
current_state = {}
excluded = []
ip_addr = 100

def get_key(my_dict,val):
    for key, value in my_dict.items():
        if val == value:
            return key

def load():
    f = open('reserved.csv', 'r')
    for line in f.readlines():
        line = line.strip().split(';')
        reserved[line[0]] = line[1]
    f.close()

    f = open('excluded.csv', 'r')
    for line in f.readlines():
        line = line.strip()
        excluded.append(line)
    f.close()

    f = open('dhcp.csv', 'r')
    for line in f.readlines():
        line = line.strip().split(';')
        current_state[line[0]] = line[1]
    f.close()

def request(mac: str):
    global ip_addr

    # A mac cím már foglalva van
    if mac in current_state:
        return
    
    # Mac cím szerepel a fenntartások között
    if mac in reserved:
        current_state[mac] = reserved[mac]
        return

    # Mac cím nem szerepel a fenntartások között
    while (f"192.168.10.{ip_addr}" in current_state.values() or\
            f"192.168.10.{ip_addr}" in excluded or\
                f"192.168.10.{ip_addr}" in reserved.values()) and\
                    ip_addr < 199:
        ip_addr += 1
    
    if ip_addr > 199:
        raise AssertionError("Nincs több IP cím")
    else:
        current_state[mac] = f"192.168.10.{ip_addr}"

    

def main():
    load()
    f = open('test.csv', 'r')
    for line in f.readlines():
        line = line.strip().split(';')
        if line[0] == 'request':
            request(line[1])
        elif line[0] == 'release':
            key = get_key(current_state,line[1])
            if key != None:
                del current_state[key]
            else:
                print(f"Tried to drop non existing ip: {line[1]}")
    f.close()

    f = open('dhcp_kesz.csv', 'w')
    for key, value in current_state.items():
        f.write(f"{key};{value}\n");
    f.close()
        

main()