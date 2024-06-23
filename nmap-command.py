# known-ports.txt: 
# grep port scan result from Nmap, 
# contains only number per line, 
# unknown ports are filtered

file_path = 'known-ports.txt'
ports = ''
url = 'tempus-ex.com'

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Process each line here
        print(line.strip())

        ports += f'{line.strip()},'
    ports = ports[:-1]

command = f"nmap -T4 -A -p{ports} {url}"
print(command)
