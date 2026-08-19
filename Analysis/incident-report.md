# WannaCry Ransomware Incident Report

## 1. Executive Summary

This investigation analyzes network evidence associated with a WannaCry ransomware incident. The analysis focused on identifying suspicious SMB activity, affected hosts, relevant network indicators, and behaviors associated with the exploitation and propagation of the malware.

The investigation identified SMB traffic over TCP port 445, SMBv1 negotiation, and suspicious SMB requests involving the host `192.168.116.149`. The observed network behavior is consistent with activity associated with WannaCry's exploitation and propagation mechanisms.

## 2. Incident Overview

**Incident:** WannaCry Ransomware Activity  
**Primary Protocol:** SMB  
**Primary Port:** TCP/445  
**Key Host Observed:** `192.168.116.149`  
**Analysis Tool:** Wireshark  

The investigation was performed using captured network traffic and supporting analysis documentation.

## 3. Evidence Analyzed

The following evidence was examined during the investigation:

- Network packet capture
- SMB traffic
- SMBv1 negotiation
- IPC$ connection activity
- SMB `PeekNamedPipe` requests
- NT status responses
- Network analysis documentation
- Extracted indicators of compromise

## 4. Network Analysis Findings

The captured traffic showed communication over TCP port 445 using the SMB protocol.

The SMB negotiation identified the dialect:

`NT LM 0.12`

This indicates SMBv1 activity.

An SMB connection involving the `IPC$` share was also observed. Additional SMB activity included `PeekNamedPipe` requests.

The traffic included the NT status response:

`STATUS_INSUFF_SERVER_RESOURCES`

These observations provide network-level evidence relevant to the investigation of WannaCry activity.

## 5. Attack Behavior

The observed SMB activity is significant because WannaCry is known for exploiting vulnerable Windows systems through SMB.

The investigation identified network behavior associated with SMB-based exploitation and possible propagation between systems.

The evidence does not by itself establish every stage of the ransomware infection. Therefore, conclusions are limited to behaviors directly supported by the captured network traffic.

## 6. MITRE ATT&CK Mapping

### T1210 — Exploitation of Remote Services

The SMB traffic observed over TCP/445 is relevant to exploitation of a vulnerable remote service.

### T1046 — Network Service Scanning

Network activity identified during the investigation is relevant to network service discovery and scanning behavior.

## 7. Indicators of Compromise

The IOC extraction process identified indicators from the network analysis evidence.

### IP Addresses

- `192.168.116.149`
- `192.168.116.138`

### Hashes

- `44d88612fea8a8f36de82e1278abb02f`

### URLs

- `https://example.com/malware`

> Note: The URL and hash above were used during IOC-extraction testing and should be treated as test indicators unless independently confirmed as originating from the WannaCry evidence.

## 8. Impact Assessment

The observed activity indicates potential compromise or attempted exploitation of systems through SMB.

The presence of SMBv1 and suspicious SMB requests represents a significant security risk because vulnerable SMB services can provide attackers with a pathway to compromise and propagate between systems.

## 9. Recommended Remediation

The following defensive actions are recommended:

1. Disable SMBv1 where it is not required.
2. Apply current security patches to Windows systems.
3. Restrict unnecessary access to TCP port 445.
4. Segment critical systems from untrusted network segments.
5. Monitor SMB traffic for suspicious activity.
6. Maintain reliable offline backups.
7. Review affected systems for signs of compromise.
8. Continue monitoring for related indicators.

## 10. Conclusion

The investigation identified suspicious SMB activity consistent with behaviors relevant to WannaCry ransomware propagation.

The combination of SMB communication over TCP/445, SMBv1 negotiation, IPC$ activity, and `PeekNamedPipe` requests provided important network evidence for the investigation.

The analysis demonstrates how packet-level evidence can be used to identify suspicious behavior, map activity to MITRE ATT&CK techniques, and extract indicators that can support further detection and response.
