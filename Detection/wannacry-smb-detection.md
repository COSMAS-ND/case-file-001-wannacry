# WannaCry SMB Propagation Detection

## Objective

Detect unusual SMB activity that may indicate automated ransomware propagation across an internal network.

## Detection Scenario

A workstation generates an unusually high number of SMB connection attempts to multiple internal hosts over a short period.

## Relevant Network Indicator

- Protocol: SMB
- Destination Port: TCP/445
- Direction: Internal host to multiple internal hosts

## Example Detection Logic

```text
IF
    source_host generates multiple TCP/445 connections
    AND
    destinations include multiple internal hosts
    AND
    activity occurs within a short time window
THEN
    generate a high-priority security alert
