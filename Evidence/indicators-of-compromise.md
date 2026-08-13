# Indicators of Compromise

## Overview

Indicators of Compromise (IOCs) are observable artifacts that may help security teams identify WannaCry-related activity.

## Host-Based Indicators

Potential host-based indicators include:

- Unexpected file encryption
- Files renamed with unusual extensions
- Ransom notes appearing on affected systems
- Unexpected processes running on Windows systems
- Suspicious changes to files and directories
- Unusual system activity following SMB connections

## Network Indicators

Potential network indicators include:

- Unusual SMB traffic
- Large numbers of connection attempts to TCP port 445
- Internal scanning activity
- Unexpected connections between Windows systems
- Rapid connection attempts across multiple hosts

## Malware Indicators

WannaCry-related investigations may include:

- Malicious executable files
- Suspicious processes
- Ransom-note files
- File-encryption activity
- Attempts to communicate with other vulnerable systems

## Important Vulnerability

The major vulnerability associated with WannaCry propagation was:

**CVE-2017-0144**

The vulnerability affected SMBv1 implementations in vulnerable Microsoft Windows systems.

## Detection Considerations

Security teams should correlate multiple indicators rather than relying on a single artifact.

Useful sources include:

- Windows event logs
- Endpoint detection logs
- Firewall logs
- IDS/IPS alerts
- DNS logs
- Network packet captures
- File-system monitoring

## Defensive Action

When suspicious WannaCry activity is detected:

1. Isolate the affected host.
2. Investigate related network connections.
3. Identify other potentially affected systems.
4. Apply required security updates.
5. Disable SMBv1 where appropriate.
6. Review endpoint and network logs.
7. Restore systems using verified backups where necessary.
