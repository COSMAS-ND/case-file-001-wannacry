# Network Analysis

## Overview

Network analysis of the WannaCry incident focuses on the communication and propagation behavior associated with the ransomware.

## SMB Communication

WannaCry exploited vulnerable implementations of the Server Message Block (SMBv1) protocol.

The primary network service associated with this activity was:

**TCP Port 445 — SMB**

Systems exposing vulnerable SMB services were at increased risk.

## Scanning and Propagation

After compromising a system, WannaCry could attempt to identify additional vulnerable hosts.

This behavior could generate unusual network traffic, including:

- Repeated connections to TCP port 445
- Scanning across multiple internal IP addresses
- Large numbers of SMB connection attempts
- Unexpected host-to-host communication
- Rapid lateral movement

## Network Detection

Security teams can monitor for suspicious SMB activity using:

- Firewalls
- Intrusion Detection Systems
- Intrusion Prevention Systems
- Network traffic analysis
- SIEM platforms
- Packet captures

## Example Detection Logic

A security analyst could investigate a host that generates an unusually high number of SMB connection attempts within a short period.

For example:

```text
Internal Host
     |
     |---- TCP/445 ----> Host A
     |---- TCP/445 ----> Host B
     |---- TCP/445 ----> Host C
     |---- TCP/445 ----> Host D
     |---- TCP/445 ----> Host E
