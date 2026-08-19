# WannaCry Detection Strategy

## Objective

This document outlines security monitoring and detection approaches that could help identify WannaCry-related activity within an organization.

## 1. Network-Based Detection

Monitor for unusual SMB activity, particularly connections involving TCP port 445.

Key indicators include:

- Unexpected SMB connections between internal systems
- Rapid scanning of multiple hosts
- Repeated connection attempts to TCP/445
- Unusual lateral movement patterns
- Sudden increases in SMB traffic

## 2. Endpoint Detection

Monitor Windows endpoints for:

- Unexpected processes executing from unusual locations
- Suspicious file creation or modification
- Abnormal process execution
- Unexpected changes to system files
- Indicators associated with ransomware activity

## 3. Vulnerability Monitoring

Organizations should identify systems running vulnerable versions of Windows and prioritize remediation.

Particular attention should be given to systems where SMBv1 remains enabled.

## 4. SIEM Monitoring

Security teams can create alerts for:

- Large volumes of SMB connections
- Multiple failed or unusual SMB connection attempts
- Sudden endpoint activity across multiple systems
- Suspicious process execution combined with network activity

## 5. Incident Detection Logic

A high-confidence alert could be generated when:

1. An endpoint initiates unusual SMB connections.
2. Multiple internal hosts are contacted within a short period.
3. Suspicious endpoint activity occurs at the same time.
4. Similar activity appears across multiple systems.

This combination can indicate possible ransomware propagation or lateral movement.

## Conclusion

Effective WannaCry detection requires combining network monitoring, endpoint telemetry, vulnerability management, and SIEM correlation rather than relying on a single indicator.
