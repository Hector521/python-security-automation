# python-security-automation

A beginner Python script that scans a login log file and counts failed login attempts,
the first step in detecting brute-force attacks.

## How to run
```
python security_check.py
```

## Example output
```
Security Scan Complete
Failed login attempts: 3
Checkmate!
```

## How it works
1. Starts a counter at 0.
2. Opens `security_log.txt` with `with open(...)`, which closes the file automatically.
3. Reads the file one line at a time.
4. If a line contains `"Failed login"`, adds 1 to the counter.
5. Prints the total.

## Sample log (`security_log.txt`)
```
Successful login - Hector
Failed login - 192.168.1.25
Successful login - Admin
Failed login - 192.168.1.55
Failed login - 192.168.1.25
Successful login - Hector
```

## What I learned
- Reading a file line by line in Python
- Using `in` to search for text inside a string
- Why counting failed logins matters: many failures in a short time can signal a password-guessing attack

## Next steps
- [ ] Count failed logins **per IP address** and flag any IP with 2+ failures
- [ ] Save the results to a JSON report
- [ ] Send an alert when an IP is flagged
