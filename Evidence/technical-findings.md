# Technical Findings

## 1. Vulnerability Exploited

The WannaCry ransomware outbreak exploited a vulnerability in the Microsoft Server Message Block (SMB) version 1 protocol.

The vulnerability, identified as **CVE-2017-0144**, affected vulnerable versions of Microsoft Windows and allowed remote code execution.

Microsoft addressed the vulnerability through security update **MS17-010**.

## 2. Exploitation Mechanism

WannaCry used the SMBv1 vulnerability to gain unauthorized access to vulnerable systems.

The malware was capable of spreading between systems over a network without requiring the victim to manually execute the malware on every affected machine.

This made the attack particularly dangerous in organizations with large numbers of unpatched Windows systems.

## 3. Propagation

After compromising a vulnerable system, WannaCry attempted to identify other potentially vulnerable systems.

Its propagation behavior contributed significantly to the rapid global spread of the outbreak.

Network environments with exposed or unpatched SMB services were particularly vulnerable.

## 4. Ransomware Behavior

After infection, WannaCry encrypted files on the affected system and displayed a ransom demand.

The malware attempted to make affected files inaccessible and demanded payment in Bitcoin in exchange for purported recovery of the encrypted data.

The incident demonstrated how ransomware can combine data encryption with automated network propagation.

## 5. Network-Level Findings

The attack was strongly associated with exploitation of SMB services, particularly **TCP port 445**.

Potential indicators of malicious activity included:

- Unexpected SMB connections between internal systems
- Large numbers of connection attempts to TCP port 445
- Scanning activity targeting vulnerable Windows hosts
- Unusual lateral movement across the network
- Communication patterns associated with infected hosts

Network monitoring and packet analysis can therefore help identify abnormal SMB activity.

## 6. Endpoint-Level Findings

Potential signs of WannaCry infection included:

- Files becoming inaccessible or encrypted
- Unexpected ransom messages
- Unusual file-system activity
- Suspicious processes executing on Windows hosts
- Attempts to communicate with other systems over SMB
- Unexpected changes to system files

Endpoint monitoring and centralized logging can assist in detecting these behaviors.

## 7. Security Control Failures

The incident highlights several security weaknesses:

1. Failure to apply critical security patches promptly.
2. Continued use of vulnerable SMBv1 services.
3. Insufficient network segmentation.
4. Excessive exposure of SMB services.
5. Inadequate endpoint monitoring.
6. Insufficient backup and recovery controls.

## 8. Defensive Recommendations

Organizations should:

- Apply security updates promptly.
- Disable SMBv1 where it is not required.
- Restrict TCP port 445 using appropriate firewall rules.
- Segment networks to limit lateral movement.
- Monitor unusual SMB activity.
- Deploy endpoint detection and response capabilities.
- Maintain regular offline or otherwise protected backups.
- Test backup restoration procedures.
- Establish an incident response plan.
- Provide security awareness training to users.

## 9. Technical Assessment

The WannaCry incident demonstrates how an unpatched vulnerability can become a major organizational security incident when combined with automated propagation.

The primary defensive lesson is that vulnerability management, network segmentation, endpoint monitoring, and reliable backups must work together.

A single security control may not prevent every attack, but layered defensive controls can significantly reduce the likelihood and impact of a ransomware outbreak.
