# Module 2 – Networking Basics & Hands-On Lab

This module focused on designing, building, and configuring a basic network using Cisco Packet Tracer. It was split into two parts:

---

## 🛠️ Part 1 – Simple Ethernet LAN Build

**Objective:**  
Set up a small-scale LAN with 2 PCs, a DNS server, and two switches.

**Key Actions:**
- Assigned static IPs to both PCs and the server
- Connected all devices using proper Ethernet cables
- Configured switch names, passwords, and banners using CLI
- Verified connectivity with `ping` commands and displayed switch configuration using `show running-config`

---

## 🌐 Part 2 – Multi-Segment Routed Network with RIPv2

**Objective:**  
Design and configure a two-router network with subnetting, DHCP, and dynamic routing.

**Core Setup:**
- **Routers:** Connected Router0 and Router1 using a /30 subnet
- **Switches:** Each router connected to its own local switch
- **DHCP:** Configured static and dynamic IP ranges across both subnets
- **Servers:** Static IPs assigned to Web, DNS, and DHCP servers
- **RIPv2 Routing:** Enabled routing across the entire network to allow cross-subnet traffic

**IP Scheme Highlights:**
- Subnet A (192.168.1.0/25): Web, DNS, DHCP servers and PCs
- Subnet B (192.168.1.128/25): DHCP server, PCs, printer

**Tests Performed:**
- Ping tests across subnets
- Web access test to the web server
- IP allocation confirmed via DHCP

---

## 🧠 What I Learned

- How to apply subnetting in practical network layouts
- Dynamic routing with RIPv2
- Hands-on CLI config for switches (hostname, banner, passwords)
- Testing and troubleshooting basic and multi-segment networks
