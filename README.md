# WannaCry Ransomware Network Investigation

## Overview

This case study documents a network-based investigation into suspicious activity associated with WannaCry ransomware.

The investigation focuses on SMB traffic, network behavior, indicators of compromise, MITRE ATT&CK mapping, and Python-based IOC extraction.

## Objectives

- Analyze captured network traffic.
- Identify suspicious SMB activity.
- Document relevant network indicators.
- Map observed behavior to MITRE ATT&CK.
- Automate IOC extraction with Python.
- Produce a structured incident report.

## Investigation Highlights

### Network Analysis

The investigation identified:

- SMB traffic over TCP port 445.
- SMBv1 negotiation using `NT LM 0.12`.
- `IPC$` share activity.
- `PeekNamedPipe` requests.
- `STATUS_INSUFF_SERVER_RESOURCES` responses.
- Host `192.168.116.149` as a key observed system.

### MITRE ATT&CK

The investigation mapped relevant behavior to:

- **T1210 — Exploitation of Remote Services**
- **T1046 — Network Service Scanning**

### IOC Automation

A Python script was developed to extract:

- IP addresses
- Hashes
- URLs

The script was tested successfully and then executed against the real network-analysis evidence.

## Tools Used

- Wireshark
- Ubuntu/Linux
- Python 3
- MITRE ATT&CK
- Git/GitHub

## Repository Structure

```text
case-file-001-wannacry/
├── Analysis/
│   ├── incident-report.md
│   ├── mitre-attack-mapping.md
│   └── network-analysis.md
├── Detection/
│   ├── ioc_extractor.py
│   └── test_iocs.txt
├── Evidence/
│   └── network-analysis.md
└── README.md
