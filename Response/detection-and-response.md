# Detection and Response Plan — WannaCry

## 1. Purpose

This section presents a defensive detection and response approach for a WannaCry-style ransomware incident.

The objective is to identify suspicious activity early, contain affected systems, remove the threat, and restore normal operations.

---

## 2. Detection Strategy

Security teams should monitor for indicators associated with ransomware activity and abnormal SMB behavior.

### Key Detection Signals

- Unusual SMB traffic over TCP/445
- Large numbers of SMB connection attempts
- Multiple systems communicating with previously unseen internal hosts
- Sudden file-encryption activity
- Unexpected changes to large numbers of files
- Security tools being disabled unexpectedly
- Suspicious executable files appearing on endpoints
- Multiple hosts showing similar ransomware-related behavior

---

## 3. Network Detection

Network monitoring tools such as IDS/IPS, SIEM platforms, and packet-analysis tools can help identify abnormal SMB activity.

### Example Detection Scenario

A workstation begins generating a large number of TCP/445 connection attempts against multiple internal systems.

This behavior should trigger an investigation because widespread SMB connection attempts may indicate automated network propagation.

### Investigation Questions

1. Which host initiated the connections?
2. Which systems were contacted?
3. How many connections were generated?
4. Were the destination systems vulnerable?
5. Did the source host show other suspicious activity?
6. Did additional systems become infected?

---

## 4. Endpoint Detection

Endpoint monitoring should look for:

- Unexpected executable files
- Rapid modification of large numbers of files
- Suspicious processes
- Unusual network connections
- Changes to security controls
- Ransomware-related notifications
- Abnormal system behavior

Endpoint alerts should be correlated with network telemetry to determine whether the activity is isolated or part of a wider incident.

---

## 5. Initial Response

Once ransomware activity is confirmed:

### Step 1 — Identify affected systems

Determine which endpoints and servers are showing signs of compromise.

### Step 2 — Isolate affected systems

Remove confirmed compromised systems from the network to reduce further propagation.

### Step 3 — Protect unaffected systems

Identify vulnerable systems and restrict unnecessary SMB communication while investigation continues.

### Step 4 — Preserve evidence

Collect relevant logs, alerts, network records, and other forensic evidence before making unnecessary changes to affected systems.

---

## 6. Containment

Containment should focus on stopping further spread.

Recommended actions include:

- Restrict unnecessary SMB traffic
- Isolate infected endpoints
- Segment critical systems
- Disable obsolete protocols where appropriate
- Block known malicious indicators
- Protect backup infrastructure
- Monitor for additional compromised hosts

---

## 7. Eradication

After containment, security teams should remove the underlying cause of the compromise.

Key actions include:

- Apply relevant security patches
- Remove malicious files and persistence mechanisms
- Rebuild severely compromised systems where appropriate
- Update endpoint security tools
- Disable unnecessary services
- Review privileged accounts
- Confirm that vulnerable systems have been remediated

---

## 8. Recovery

Recovery should be performed in a controlled manner.

### Recovery Activities

1. Restore systems from trusted backups.
2. Verify that restored systems are clean.
3. Apply security updates before reconnecting systems.
4. Reconnect systems gradually.
5. Monitor restored systems for recurring suspicious activity.
6. Confirm that critical business services are functioning normally.

---

## 9. Post-Incident Review

After recovery, the organization should conduct a lessons-learned review.

### Questions to Consider

- How did the incident begin?
- Which vulnerability was involved?
- Why was the vulnerability still present?
- How quickly was the incident detected?
- How effective was containment?
- Were backups available and usable?
- Which security controls failed?
- What improvements are required?

---

## 10. Preventive Controls

Organizations can reduce ransomware risk through:

- Timely vulnerability and patch management
- Network segmentation
- Endpoint detection and response
- Security information and event management
- Regular vulnerability assessments
- Strong access controls
- Offline or otherwise protected backups
- Employee security awareness
- Incident-response planning
- Continuous network monitoring

---

## 11. Conclusion

A ransomware incident should be treated as both a technical and operational security event.

Effective defense requires more than detecting malware. Organizations must be able to identify suspicious behavior, contain compromised systems, preserve evidence, eradicate the threat, and safely restore operations.

The WannaCry incident demonstrates the importance of proactive patch management, network monitoring, segmentation, and tested recovery procedures.
