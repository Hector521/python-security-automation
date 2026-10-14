import json
THRESHOLD = 2 #flag any IP with this many failed logins or more
failed_logins = 0
failed_by_ip = {} #dictionary: IP address -> number of failed logins

with open("security_log.txt", "r") as file:
    for line in file:
        if "Failed login" in line:
            failed_logins += 1

            # "failed login - 192.168.1.25" -> pull out just the IP
            ip = line.split(" - ")[1].strip()

            # add 1 to this ip's count (start at 0 if we haven't seen it yet)
            failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1
print("Security Scan Complete")
print("Failed login attempts:", failed_logins)

print("Failed logins by IP:")
for ip, count in failed_by_ip.items():
    print(f" {ip}: {count}")

flagged_ips = [] # list of IPs that crossed the threshold
print(f"Suspicious IPs ({THRESHOLD}+ failed logins):")
for ip, count in failed_by_ip.items():
    if count >= THRESHOLD:
        flagged_ips.append(ip)
        print(f" [ALERT] {ip}: {count} failed logins")
if not flagged_ips:
    print(" None found")

#save everything we found to a JSON file
report = {
    "total_failed_logins": failed_logins,
    "threshold": THRESHOLD,
    "failed_by_ip": failed_by_ip,
    "flagged_ips": flagged_ips
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Report saved to report.json")


print("Checkmate!")