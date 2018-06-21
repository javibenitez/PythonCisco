## Cisco Adaptive Security Appliance - Path Traversal (CVE-2018-0296)

A security vulnerability in Cisco ASA that would allow an attacker to view sensitive system information without authentication by using directory traversal techniques.

## Vulnerable Products
This vulnerability affects Cisco ASA Software and Cisco Firepower Threat Defense (FTD) Software that is running on the following Cisco products:

    3000 Series Industrial Security Appliance (ISA)
    ASA 1000V Cloud Firewall
    ASA 5500 Series Adaptive Security Appliances
    ASA 5500-X Series Next-Generation Firewalls
    ASA Services Module for Cisco Catalyst 6500 Series Switches and Cisco 7600 Series Routers
    Adaptive Security Virtual Appliance (ASAv)
    Firepower 2100 Series Security Appliance
    Firepower 4100 Series Security Appliance
    Firepower 9300 ASA Security Module
    FTD Virtual (FTDv)

## Script usage
- Installation: `git clone https://github.com/yassineaboukir/CVE-2018-0296.git`
- Usage: `python cisco_asa.py <URL>`

If the web server is vulnerable, the script will dump in a text file both the current directory as well as `+CSCOE+`.

## Bug Bounty Recon
You can use Shodan, Censys or any other OSINT tools to enumerate vulnerable servers but I will not be disclosing the query to use. Figure it out!

## References:
- https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180606-asaftd
