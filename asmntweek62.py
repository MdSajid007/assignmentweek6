fname = input("Enter the file name: ")
try:
    fhand = open(fname)

except FileNotFoundError:
    print(f"Error! File '{fname}' does not exist.")
    exit()
    

hosts = {}  

for line in fhand:
    if line.startswith("From:"):
        words = line.split()
        
        if len(words) > 1:
            email = words[1]
            email_parts = email.split("@")
            host = email_parts[1]
            
            if host in hosts:
                hosts[host] += 1
            else:
                hosts[host] = 1

for host in hosts.keys():
    print(f"\n{host}\n")

total_hosts = len(hosts)
print(f"Total {total_hosts} hosts printed.\n")

fhand.close()

