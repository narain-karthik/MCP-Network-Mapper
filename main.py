from mcp.server.fastmcp import FastMCP
from typing import Optional
import subprocess

# Create MCP server
mcp = FastMCP("NmapTools")

# Tool: Interactive Option Menu
@mcp.tool()
def nmap_menu() -> str:
    """Choose an Nmap feature by number."""
    return (
        "Choose an Nmap operation by number:\n"
        "1. Basic Port Scan\n"
        "2. Service Detection\n"
        "3. OS Detection\n"
        "4. Run NSE Script\n"
        "5. Ping Sweep\n"
        "6. Custom Nmap Command\n"
        "7. Vulnerability Scan\n"
        "8. Traceroute\n"
        "9. Firewall Detection\n"
        "10. Aggressive Scan\n"
        "11. Stealth Scan (Null/FIN/Xmas)\n"
        "12. Save Scan Output to File\n"
        "13. Live Host Count Summary\n"
        "Please use the respective tool with the required parameters."
    )

# Tool: Basic Port Scan
@mcp.tool()
def basic_port_scan(target: str, ports: Optional[str] = None) -> str:
    """Scan open ports on a target. Ports can be provided as range (e.g., "20-80") or list (e.g., "22,80")."""
    command = ["nmap", "-sS"]
    if ports:
        command.extend(["-p", ports])
    command.append(target)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Service Detection
@mcp.tool()
def detect_services(target: str) -> str:
    """Detect services running on the target."""
    command = ["nmap", "-sV", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: OS Detection
@mcp.tool()
def detect_os(target: str) -> str:
    """Attempt to detect the target's operating system."""
    command = ["nmap", "-O", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Run NSE Scripts
@mcp.tool()
def run_nse_script(target: str, script: str) -> str:
    """Run a specific Nmap Scripting Engine (NSE) script."""
    command = ["nmap", "--script", script, target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Ping Sweep
@mcp.tool()
def ping_sweep(subnet: str) -> str:
    """Perform ping sweep on a subnet to find live hosts."""
    command = ["nmap", "-sn", subnet]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Custom Nmap Command
@mcp.tool()
def custom_scan(target: str, options: str) -> str:
    """Run a custom Nmap command (user-defined options)."""
    command = ["nmap"] + options.split() + [target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Vulnerability Scan
@mcp.tool()
def vulnerability_scan(target: str) -> str:
    """Run vulnerability scan scripts on the target."""
    command = ["nmap", "--script", "vuln", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Traceroute
@mcp.tool()
def traceroute(target: str) -> str:
    """Perform a traceroute to the target."""
    command = ["nmap", "--traceroute", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Firewall Detection
@mcp.tool()
def firewall_detection(target: str) -> str:
    """Attempt to identify firewall or packet filtering."""
    command = ["nmap", "-sA", "--reason", "--packet-trace", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Aggressive Scan
@mcp.tool()
def aggressive_scan(target: str) -> str:
    """Perform a full aggressive scan (OS, services, scripts, traceroute)."""
    command = ["nmap", "-A", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Stealth Scan Modes
@mcp.tool()
def stealth_scan(target: str, mode: str = "sF") -> str:
    """Run a stealth scan: Null (sN), FIN (sF), Xmas (sX)."""
    if mode not in ("sN", "sF", "sX"):
        return "Invalid mode. Use 'sN', 'sF', or 'sX'."
    command = ["nmap", f"-{mode}", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

# Tool: Output to File
@mcp.tool()
def scan_to_file(target: str, options: str, filename: str) -> str:
    """Run Nmap scan and save output to a file."""
    command = ["nmap"] + options.split() + ["-oN", filename, target]
    result = subprocess.run(command, capture_output=True, text=True)
    return f"Scan complete. Output saved to {filename}" if result.returncode == 0 else result.stderr

# Tool: Live Host Count Summary
@mcp.tool()
def live_host_count(subnet: str) -> str:
    """Count number of live hosts in a subnet."""
    command = ["nmap", "-sn", subnet]
    result = subprocess.run(command, capture_output=True, text=True)
    live_hosts = result.stdout.count("Nmap scan report for")
    return f"Live hosts found: {live_hosts}\n\n{result.stdout}"

# Resource: Welcome message
@mcp.resource("nmap://welcome")
def welcome_message() -> str:
    return (
        "Welcome to NmapTools MCP Server.\n"
        "Use the menu tool to choose a scan option or call tools directly."
    )

if __name__ == "__main__":
    mcp.run()
