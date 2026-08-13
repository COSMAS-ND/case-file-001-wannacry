# MITRE ATT&CK Mapping — WannaCry

## Overview

This section maps observed WannaCry attack behaviors to relevant MITRE ATT&CK tactics and techniques.

The mapping is based on publicly documented characteristics of the 2017 WannaCry ransomware outbreak.

---

## 1. Initial Access

### T1190 — Exploit Public-Facing Application

WannaCry demonstrated the ability to exploit vulnerable systems through weaknesses in the SMB protocol.

**Relevance:** Exploitation of vulnerable network services can provide an initial foothold into an affected environment.

---

## 2. Execution

### T1059 — Command and Scripting Interpreter

Malware activity may involve command-line execution mechanisms during different stages of infection and system activity.

**Relevance:** Command execution can support malware operations after a system has been compromised.

---

## 3. Lateral Movement

### T1210 — Exploitation of Remote Services

WannaCry propagated between vulnerable Windows systems by exploiting the SMB vulnerability associated with CVE-2017-0144.

**Relevance:** This allowed the malware to spread across vulnerable systems without relying solely on traditional user interaction.

---

## 4. Discovery

### T1046 — Network Service Scanning

The malware demonstrated network-propagation behavior involving the identification of systems that could be reached through vulnerable network services.

**Relevance:** Network discovery can support automated propagation within an environment.

---

## 5. Impact

### T1486 — Data Encrypted for Impact

WannaCry encrypted files on affected systems and displayed a ransom demand.

**Relevance:** Encryption of data directly affected the availability and usability of systems and files.

---

## 6. Impact on Healthcare

The WannaCry outbreak demonstrated how ransomware can disrupt critical healthcare operations when vulnerable systems become unavailable.

Potential consequences include:

- Disruption of clinical workflows
- Loss of access to files and systems
- Operational delays
- Increased incident-response workload
- Financial and reputational impact

---

## Defensive Takeaways

The ATT&CK mapping highlights several important defensive priorities:

1. Maintain timely security patching.
2. Disable obsolete and unnecessary protocols.
3. Segment critical networks.
4. Monitor unusual network activity.
5. Detect suspicious encryption behavior.
6. Maintain tested offline backups.
7. Establish an incident-response process.

---

## Conclusion

The WannaCry incident demonstrates how exploitation of a known vulnerability can lead to rapid malware propagation and significant operational impact.

Mapping the incident to MITRE ATT&CK helps security teams understand attacker behavior and identify opportunities for prevention, detection, and response.
