# known-ports.txt: 
# grep port scan result from Nmap, : grep "open" filename | cut -d ' ' -f 1 | sed 's,/tcp,,'
# contains only number per line, 
# unknown ports are filtered

# The result of this script will be printed in the terminal and can be used for command in Nmap

file_path = 'known-ports.txt'
ports = ''
url = 'url.com'

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Process each line here
        print(line.strip())

        ports += f'{line.strip()},'
    ports = ports[:-1]

command = f"nmap -T4 -A -p{ports} {url}"
print(command)
