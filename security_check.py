failed_logins = 0

with open("security_log.txt", "r") as file:
    for line in file:
        if "Failed login" in line:
            failed_logins += 1

print("Security Scan Complete")
print("Failed login attempts:", failed_logins)
print("Checkmate!")