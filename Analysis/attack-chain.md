# WannaCry Attack Chain

## Attack Flow

```mermaid
flowchart LR
    A[Unpatched Windows System] --> B[SMB Vulnerability]
    B --> C[CVE-2017-0144 Exploitation]
    C --> D[Initial System Compromise]
    D --> E[Network Discovery / Scanning]
    E --> F[Propagation to Vulnerable Hosts]
    F --> G[File Encryption]
    G --> H[Ransom Demand]
    H --> I[Operational Disruption]

