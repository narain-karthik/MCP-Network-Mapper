
# 🕵️‍♂️ MCP - Network-Mapper

The **MCP - Network-Mapper** is an interactive, user-friendly command-line interface designed to simplify the process of performing various **Nmap** scans. It integrates essential network scanning tools, such as **port scanning**, **service detection**, **OS detection**, **vulnerability scanning**, and more, all within an MCP-based system. Ideal for penetration testers, network engineers, and system administrators, this tool aims to streamline and automate network scanning workflows.

---

## ✨ Features

- 🔐 **Basic Port Scan** – Scan open ports on a target machine.
- 🖥️ **Service Detection** – Detect services running on open ports.
- 🖱️ **OS Detection** – Identify the operating system of the target.
- 🧑‍💻 **Run NSE Scripts** – Execute custom Nmap Scripting Engine (NSE) scripts.
- 🌐 **Ping Sweep** – Discover live hosts on a subnet.
- ⚙️ **Custom Nmap Command** – Execute custom Nmap commands with user-defined options.
- 🔓 **Vulnerability Scan** – Run vulnerability scanning using Nmap NSE scripts.
- 🌍 **Traceroute** – Trace the network path packets take to reach the target.
- 🔥 **Firewall Detection** – Identify potential firewalls or packet filtering.
- 💣 **Aggressive Scan** – Run a comprehensive scan (OS, services, scripts, traceroute).
- 🕵️‍♀️ **Stealth Scan** – Perform stealth scans such as Null, FIN, and Xmas scans.
- 📁 **Output to File** – Save scan results to text or XML files.
- 📊 **Live Host Count Summary** – Count live hosts after performing a ping sweep.

---

## 🛠️ Tech Stack

- **Frontend**: Python with `FastMCP` for the interactive MCP interface
- **Backend**: Python, running system commands (`subprocess` module)
- **Security**: Nmap, utilizing command-line tools and system-based network probes
- **Networking**: Nmap Scanning Techniques

---

## ⚙️ Prerequisites
Before you begin, ensure that you have the following installed:
- Python 3.7+
- Nmap (`nmap` command line tool)

You can install Nmap using your system's package manager:
- For **Debian/Ubuntu**: `sudo apt install nmap`
- For **macOS**: `brew install nmap`
- For **Windows**: [Download and install Nmap](https://nmap.org/download.html)
