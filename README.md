# python-security-automation

A beginner Python script that scans a login log, counts failed logins per IP address, flags suspicious IPs, saves a JSON report, and sends an alert to Discord.

I'm a cybersecurity student learning automation. I typed and debugged every line of this project myself and can explain how each part works.

## What it does

1. Reads `security_log.txt` line by line
2. Counts every `Failed login` and tracks which IP it came from
3. Flags any IP at or above a threshold (default: 2 failures)
4. Saves the results to `report.json`
5. Sends a Discord alert if any IP was flagged

## Example output

```
Security Scan Complete
Failed login attempts: 3
Failed logins by IP:
 192.168.1.25: 2
 192.168.1.55: 1
Suspicious IPs (2+ failed logins):
 [ALERT] 192.168.1.25: 2 failed logins
Report saved to report.json
Discord alert status: 204
Checkmate!
```

Discord message:
> 🚨 Security Alert: 1 suspicious IP(s) found: 192.168.1.25

## Example report.json

```json
{
    "total_failed_logins": 3,
    "threshold": 2,
    "failed_by_ip": {
        "192.168.1.25": 2,
        "192.168.1.55": 1
    },
    "flagged_ips": ["192.168.1.25"]
}
```

## How to run it

1. Install Python 3 and the `requests` library:
```
   pip install requests
```
2. (Optional) For Discord alerts, create a webhook in your Discord server
   (Server Settings → Integrations → Webhooks) and paste the URL into a file named `discord_webhook.txt`.
   This file is in `.gitignore`, so it is never uploaded.
3. Run:
```
   python security_check.py
```

## Settings

| Setting | Where | What it does |
|---|---|---|
| `THRESHOLD` | top of `security_check.py` | How many failed logins before an IP is flagged |

## What I learned

- **Dictionaries:** `failed_by_ip.get(ip, 0) + 1` counts per IP without crashing on a new IP
- **String parsing:** `line.split(" - ")[1].strip()` pulls the IP out of each log line
- **JSON:** `json.dump(report, f, indent=4)` saves results in a format other tools can read
- **APIs and webhooks:** sending a POST request with a JSON body, and reading status codes (Discord returns `204 No Content` on success)
- **Secrets:** keeping the webhook URL out of the code and out of GitHub with `.gitignore`
- **Debugging:** fixed a bug where I opened a file `as file` but read from `f`, which was an old closed file from earlier in the script

## Next steps

- [x] Count failed logins per IP
- [x] Flag IPs over a threshold
- [x] Save a JSON report
- [x] Send Discord alerts
- [ ] Read a real log format (for example, Linux `auth.log`)
- [ ] Add timestamps and detect many failures within a short time window
