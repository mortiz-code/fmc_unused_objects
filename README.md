# fmc_clean_objects
## Detects unused objects.


## Use Case Description

Detects unused objects in Secure Firewall Management Center to keep the configuration clean.

## Installation

Clone the repository:

```sh
git clone https://github.com/mortiz-code/fmc_clean_objects.git
cd fmc_clean_objects
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

***NOTE**: You may require to install the "python3-venv" package in your Linux.*

- Complete .env_expample file and rename it to .env

Enable REST API calls.
- https://www.cisco.com/c/en/us/td/docs/security/firepower/730/api/REST/secure_firewall_management_center_rest_api_quick_start_guide_730/About_The_Firepower_Management_Center_REST_API.html#task_khz_fh1_ccb



Example usage:

    (venv) ┌──(mat㉿kali)-[~/github/devnet/fmc_clean_objects] (main)
    └─$ /home/mat/github/devnet/fmc_clean_objects/venv/bin/python /home/mat/github/devnet/fmc_clean_objects/main.py
    ------------------------- Searching for unused objects in fmc01.bvs.local --------------------------
    Type Host : BE-ThousandEyes-Agent ->  Not used.
    Type Host : BE_gw_Fibertel1 ->  Not used.
    Type Host : BE_gw_Fibertel2 ->  Not used.
    Type FQDN : Cisco_vManage ->  Not used.
    Type Host : HOST_169.254.2.2 ->  Not used.
    Type Host : HOST_172.31.33.1 ->  Not used.
    Type Network : IPv4-Benchmark-Tests ->  Not used.
    Type Network : IPv4-Link-Local ->  Not used.
    Type Network : IPv4-Multicast ->  Not used.
    Type Network : IPv4-Private-10.0.0.0-8 ->  Not used.
    Type Network : IPv4-Private-172.16.0.0-12 ->  Not used.
    Type Network : IPv4-Private-192.168.0.0-16 ->  Not used.
    Type Network : IPv6-IPv4-Mapped ->  Not used.
    Type Network : IPv6-Link-Local ->  Not used.
    Type Network : IPv6-Private-Unique-Local-Addresses ->  Not used.
    Type Network : IPv6-to-IPv4-Relay-Anycast ->  Not used.
    Type Host : MGT_FTD-VDC ->  Not used.
    Type Host : SAR-DC-ZBX01 ->  Not used.
    Type FQDN : vmanage-1 ->  Not used.
    Type Network : WebexCalling_5 ->  Not used.
    Type Network : WebexCallings_1 ->  Not used.
    Type Network : WebexCallings_10 ->  Not used.
    Type Network : WebexCallings_11 ->  Not used.
    Type Network : WebexCallings_12 ->  Not used.
    Type Network : WebexCallings_13 ->  Not used.
    Type Network : WebexCallings_14 ->  Not used.
    Type Network : WebexCallings_2 ->  Not used.
    Type Network : WebexCallings_3 ->  Not used.
    Type Network : WebexCallings_4 ->  Not used.
    Type Network : WebexCallings_6 ->  Not used.
    Type Network : WebexCallings_7 ->  Not used.
    Type Network : WebexCallings_8 ->  Not used.
    Type Network : WebexCallings_9 ->  Not used.
    Type Host : BE-ThousandEyes-Agent ->  Not used.
    Type Host : BE_gw_Fibertel1 ->  Not used.
    Type Host : BE_gw_Fibertel2 ->  Not used.
    Type Host : HOST_169.254.2.2 ->  Not used.
    Type Host : HOST_172.31.33.1 ->  Not used.
    Type Host : MGT_FTD-VDC ->  Not used.
    Type Host : SAR-DC-ZBX01 ->  Not used.
    Type Network : IPv4-Benchmark-Tests ->  Not used.
    Type Network : IPv4-Link-Local ->  Not used.
    Type Network : IPv4-Multicast ->  Not used.
    Type Network : IPv4-Private-10.0.0.0-8 ->  Not used.
    Type Network : IPv4-Private-172.16.0.0-12 ->  Not used.
    Type Network : IPv4-Private-192.168.0.0-16 ->  Not used.
    Type Network : IPv6-IPv4-Mapped ->  Not used.
    Type Network : IPv6-Link-Local ->  Not used.
    Type Network : IPv6-Private-Unique-Local-Addresses ->  Not used.
    Type Network : IPv6-to-IPv4-Relay-Anycast ->  Not used.
    Type Network : WebexCalling_5 ->  Not used.
    Type Network : WebexCallings_1 ->  Not used.
    Type Network : WebexCallings_10 ->  Not used.
    Type Network : WebexCallings_11 ->  Not used.
    Type Network : WebexCallings_12 ->  Not used.
    Type Network : WebexCallings_13 ->  Not used.
    Type Network : WebexCallings_14 ->  Not used.
    Type Network : WebexCallings_2 ->  Not used.
    Type Network : WebexCallings_3 ->  Not used.
    Type Network : WebexCallings_4 ->  Not used.
    Type Network : WebexCallings_6 ->  Not used.
    Type Network : WebexCallings_7 ->  Not used.
    Type Network : WebexCallings_8 ->  Not used.
    Type Network : WebexCallings_9 ->  Not used.
    Type FQDN : Cisco_vManage ->  Not used.
    Type FQDN : vmanage-1 ->  Not used.
    Type NetworkGroup : DNAC ->  Not used.
    Type NetworkGroup : PERMITED-HOST-VDC ->  Not used.
    Type ProtocolPortObject : AOL ->  Not used.
    Type ProtocolPortObject : Bittorrent ->  Not used.
    Type ProtocolPortObject : FTP ->  Not used.
    Type ProtocolPortObject : HTTP-8080 ->  Not used.
    Type ProtocolPortObject : IMAP ->  Not used.
    Type ProtocolPortObject : LDAP ->  Not used.
    Type ProtocolPortObject : MC-SSH ->  Not used.
    Type ProtocolPortObject : MC-UDP8601 ->  Not used.
    Type ProtocolPortObject : MC-UDP8602 ->  Not used.
    Type ProtocolPortObject : Media-TCP10022 ->  Not used.
    Type ProtocolPortObject : Media-TCP18255 ->  Not used.
    Type ProtocolPortObject : Media-UDP8606 ->  Not used.
    Type ProtocolPortObject : MediaConnect-TCP1935 ->  Not used.
    Type ProtocolPortObject : MediaConnect-UDP ->  Not used.
    Type ProtocolPortObject : NFSD-TCP ->  Not used.
    Type ProtocolPortObject : NFSD-UDP ->  Not used.
    Type ProtocolPortObject : NTP-TCP ->  Not used.
    Type ProtocolPortObject : POP-2 ->  Not used.
    Type ProtocolPortObject : POP-3 ->  Not used.
    Type ProtocolPortObject : RADIUS ->  Not used.
    Type ProtocolPortObject : RIP ->  Not used.
    Type ProtocolPortObject : SIP ->  Not used.
    Type ProtocolPortObject : SMTPS ->  Not used.
    Type ProtocolPortObject : SNMP ->  Not used.
    Type ProtocolPortObject : tcp-8888 ->  Not used.
    Type ProtocolPortObject : TCP_high_ports ->  Not used.
    Type ProtocolPortObject : TELNET ->  Not used.
    Type ProtocolPortObject : TFTP ->  Not used.
    Type ProtocolPortObject : Yahoo_Messenger_Messages ->  Not used.
    Type ProtocolPortObject : YahooMessenger_Voice_Chat_TCP ->  Not used.
    Type ProtocolPortObject : YahooMessenger_Voice_Chat_UDP ->  Not used.
    Type ProtocolPortObject : AOL ->  Not used.
    Type ProtocolPortObject : Bittorrent ->  Not used.
    Type ProtocolPortObject : FTP ->  Not used.
    Type ProtocolPortObject : HTTP-8080 ->  Not used.
    Type ProtocolPortObject : IMAP ->  Not used.
    Type ProtocolPortObject : LDAP ->  Not used.
    Type ProtocolPortObject : MC-SSH ->  Not used.
    Type ProtocolPortObject : MC-UDP8601 ->  Not used.
    Type ProtocolPortObject : MC-UDP8602 ->  Not used.
    Type ProtocolPortObject : Media-TCP10022 ->  Not used.
    Type ProtocolPortObject : Media-TCP18255 ->  Not used.
    Type ProtocolPortObject : Media-UDP8606 ->  Not used.
    Type ProtocolPortObject : MediaConnect-TCP1935 ->  Not used.
    Type ProtocolPortObject : MediaConnect-UDP ->  Not used.
    Type ProtocolPortObject : NFSD-TCP ->  Not used.
    Type ProtocolPortObject : NFSD-UDP ->  Not used.
    Type ProtocolPortObject : NTP-TCP ->  Not used.
    Type ProtocolPortObject : POP-2 ->  Not used.
    Type ProtocolPortObject : POP-3 ->  Not used.
    Type ProtocolPortObject : RADIUS ->  Not used.
    Type ProtocolPortObject : RIP ->  Not used.
    Type ProtocolPortObject : SIP ->  Not used.
    Type ProtocolPortObject : SMTPS ->  Not used.
    Type ProtocolPortObject : SNMP ->  Not used.
    Type ProtocolPortObject : tcp-8888 ->  Not used.
    Type ProtocolPortObject : TCP_high_ports ->  Not used.
    Type ProtocolPortObject : TELNET ->  Not used.
    Type ProtocolPortObject : TFTP ->  Not used.
    Type ProtocolPortObject : Yahoo_Messenger_Messages ->  Not used.
    Type ProtocolPortObject : YahooMessenger_Voice_Chat_TCP ->  Not used.
    Type ProtocolPortObject : YahooMessenger_Voice_Chat_UDP ->  Not used.
    Type PortObjectGroup : Camaras ->  Not used.
    ------------------------------- Number of unused objects: 131 of 429 -------------------------------
    ---------------------------------- Execution time: 0:06:08.550838 ----------------------------------

## DevNet Sandbox

The Sandbox which can implement this script is at: https://devnetsandbox.cisco.com/RM/Diagram/Index/1228cb22-b2ba-48d3-a70a-86a53f4eecc0?diagramType=Topology


## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Author(s)

This project was written and is maintained by the following individuals:

* Matias Ortiz <matias.ortiz@bvstv.com>