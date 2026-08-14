# WannaCry Indicator & Detection Matrix

## Purpose

This matrix connects observable WannaCry-related indicators to practical detection methods and analyst actions.

The objective is to demonstrate how technical evidence can be translated into actionable SOC investigation steps.

---

## Detection Matrix

| Indicator / Behavior | Evidence Source | Detection Method | Security Tool | Analyst Action |
|---|---|---|---|---|
| Unusual TCP/445 activity | Network traffic | Monitor abnormal SMB connections | Wireshark / IDS / Firewall | Identify source and destination hosts |
| Multiple SMB connections | Network traffic | Detect repeated connections to multiple hosts | SIEM / IDS | Investigate possible propagation |
| SMBv1 activity | Network configuration / traffic | Identify systems using SMBv1 | Network monitoring | Determine whether SMBv1 can be disabled |
| Suspicious executable | Endpoint telemetry | File and process monitoring | EDR / Antivirus | Isolate and investigate endpoint |
| Rapid file modification | Endpoint telemetry | Behavioral detection | EDR / File monitoring | Investigate possible ransomware activity |
| Ransom note | Host filesystem | File detection | EDR / SIEM | Identify affected system |
| Multiple affected hosts | SIEM / Endpoint logs | Correlate alerts across endpoints | SIEM | Determine incident scope |
| Vulnerable Windows host | Vulnerability scan | Identify missing security updates | Vulnerability scanner | Prioritize remediation |
| Internal scanning behavior | Network traffic | Detect connection attempts across many hosts | IDS / Network monitoring | Investigate source endpoint |
| Unexpected lateral movement | Network logs | Analyze east-west traffic | SIEM / NDR | Investigate compromised credentials or malware |
| Data encryption activity | Endpoint telemetry | Detect abnormal file-encryption behavior | EDR | Isolate endpoint immediately |

---

## Investigation Workflow

When a suspicious WannaCry-like event is detected:

### 1. Detect

Identify the initial alert or abnormal behavior.

### 2. Validate

Determine whether the activity is legitimate or potentially malicious.

### 3. Identify

Determine the source endpoint, destination systems, users, and relevant timestamps.

### 4. Scope

Search network and endpoint telemetry for additional affected systems.

### 5. Contain

Isolate confirmed or suspected compromised systems.

### 6. Investigate

Correlate network traffic, endpoint activity, vulnerability information, and other available evidence.

### 7. Remediate

Patch vulnerable systems, remove malicious activity, and address the underlying security weakness.

### 8. Recover

Restore affected systems from trusted backups and monitor them after recovery.

---

## Example SOC Alert

```text
ALERT: Suspicious SMB Propagation

Source Host:
10.10.20.15

Observed Behavior:
Multiple TCP/445 connection attempts

Destination Pattern:
Multiple internal hosts

Risk:
Potential automated network propagation

Priority:
HIGH
