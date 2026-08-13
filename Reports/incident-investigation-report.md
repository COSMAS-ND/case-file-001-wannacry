# WannaCry Ransomware — Incident Investigation Report

## 1. Executive Summary

This investigation examines the 2017 WannaCry ransomware outbreak, with emphasis on vulnerability exploitation, network propagation, operational impact, detection, containment, and defensive controls.

The incident demonstrated how exploitation of an unpatched vulnerability could enable ransomware to spread rapidly across vulnerable Windows systems.

The case provides important lessons for security operations teams regarding vulnerability management, network monitoring, segmentation, endpoint protection, and incident response.

---

## 2. Incident Overview

| Category | Finding |
|---|---|
| Incident | WannaCry Ransomware |
| Year | 2017 |
| Incident Type | Ransomware |
| Primary Impact | Data encryption and operational disruption |
| Key Protocol | SMB |
| Relevant Vulnerability | CVE-2017-0144 |
| Affected Platform | Vulnerable Microsoft Windows systems |
| Primary Security Concern | Rapid network propagation |

---

## 3. Attack Chain

The investigation identifies the following general sequence:

1. A vulnerable Windows system was exposed.
2. The SMB vulnerability was exploited.
3. The ransomware gained access to the affected system.
4. The malware attempted to propagate to other vulnerable systems.
5. Files on affected systems were encrypted.
6. Victims received a ransom demand.
7. Organizations experienced operational disruption.

---

## 4. Key Findings

### Finding 1 — Unpatched Vulnerability

The incident depended heavily on vulnerable Windows systems that had not received the relevant security update.

**Risk:** A known vulnerability created an entry point for compromise and propagation.

### Finding 2 — Network Propagation

WannaCry demonstrated rapid propagation through vulnerable SMB-enabled systems.

**Risk:** A compromised endpoint could become a threat to other vulnerable systems on the same network.

### Finding 3 — Insufficient Network Segmentation

Flat or poorly segmented networks can allow malicious activity to spread more easily between systems.

**Risk:** A localized compromise can develop into a wider organizational incident.

### Finding 4 — Operational Impact

Ransomware can affect the availability of systems and files required for normal business operations.

**Risk:** Organizations may experience service interruptions, financial losses, and reputational damage.

---

## 5. Detection Opportunities

Security teams could identify suspicious activity through:

- Abnormal TCP/445 traffic
- Large numbers of SMB connection attempts
- Unusual communication between internal hosts
- Sudden file-encryption activity
- Suspicious processes
- Endpoint security alerts
- Multiple systems displaying similar symptoms

---

## 6. Containment Recommendations

During an active incident, defenders should:

1. Identify affected systems.
2. Isolate confirmed compromised endpoints.
3. Restrict unnecessary SMB traffic.
4. Identify vulnerable systems.
5. Protect backup infrastructure.
6. Preserve relevant logs and evidence.
7. Monitor for additional affected systems.

---

## 7. Recovery Recommendations

After containment:

- Remediate vulnerable systems.
- Apply appropriate security updates.
- Rebuild compromised systems when necessary.
- Restore from trusted backups.
- Verify systems before reconnecting them.
- Monitor restored systems.
- Conduct a post-incident review.

---

## 8. Security Controls That Could Reduce Risk

### Preventive Controls

- Patch and vulnerability management
- Network segmentation
- Endpoint protection
- Least-privilege access
- Secure configuration management
- Protected backups

### Detective Controls

- SIEM monitoring
- IDS/IPS
- Endpoint detection and response
- Network traffic monitoring
- File integrity monitoring

### Response Controls

- Incident-response procedures
- Endpoint isolation
- Evidence preservation
- Recovery procedures
- Post-incident lessons learned

---

## 9. MITRE ATT&CK Alignment

Relevant ATT&CK techniques identified during the investigation include:

- T1190 — Exploit Public-Facing Application
- T1046 — Network Service Scanning
- T1210 — Exploitation of Remote Services
- T1486 — Data Encrypted for Impact

These mappings provide a structured way to understand attacker behavior and identify corresponding defensive opportunities.

---

## 10. Lessons Learned

The WannaCry incident demonstrates several important cybersecurity principles:

1. Known vulnerabilities must be patched promptly.
2. Legacy protocols can create significant security risk.
3. Network segmentation can limit the impact of a compromise.
4. Security monitoring should identify abnormal behavior, not only known malware.
5. Backups should be protected and regularly tested.
6. Incident-response plans should be established before an incident occurs.

---

## 11. Final Assessment

The WannaCry outbreak demonstrates how a single vulnerable service can contribute to widespread ransomware propagation.

The most important defensive lesson is that effective cybersecurity requires multiple layers of protection.

Patch management, secure network architecture, endpoint monitoring, centralized logging, incident response, and reliable recovery mechanisms must work together to reduce both the likelihood and impact of ransomware incidents.
