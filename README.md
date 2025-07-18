# 🔍 Fazo Finder - Advanced OSINT Reconnaissance Toolkit

![Fazo Finder Banner](https://img.shields.io/badge/Fazo_Finder-v2.1-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Termux-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<p align="center">
  <img src="https://i.imgur.com/JK7wLnD.png" alt="Fazo Finder Logo" width="400">
</p>

## 🌟 Key Features

### 🔎 Information Gathering
- **Domain Intelligence**
  - WHOIS lookup
  - DNS records analysis
  - Subdomain enumeration
  - SSL/TLS certificate inspection
  - IP geolocation tracking

- **Email Analysis**
  - Breach detection (HaveIBeenPwned API)
  - Disposable email verification
  - Email pattern recognition
  - Associated account discovery

- **Username Recon**
  - 100+ platform presence check
  - Profile picture extraction
  - Activity timeline analysis
  - Cross-platform connections mapping

### 🛡️ Security Tools
- **Vulnerability Assessment**
  - Website security headers check
  - Open port scanner
  - CMS detection
  - Admin panel finder

- **Dark Web Monitoring**
  - Tor network scanning
  - Pastebin dumps monitoring
  - Data leak alerts
  - Credential exposure checks

### 📊 Reporting
- Multiple export formats (PDF/HTML/JSON)
- Executive summary generation
- Risk scoring system
- Timeline visualization

- Usage
text

python3 fazo_finder.py [options]

Options:
  -d, --domain DOMAIN    Perform DNS lookup on a domain
  -e, --email EMAIL      Check if email was involved in breaches
  -u, --username USER    Search for username across social media
  -o, --output           Save results to a file

Examples

    Check DNS records for a domain:

bash

python3 fazo_finder.py -d example.com
python3 fazo_finder.py -e user@example.com

## 🚀 Installation

### Kali Linux
```bash
git clone https://github.com/Old-hacker01/fazo-finder.git
cd FazoFinder
chmod +x fazo-finder.py
python fazo_finder.py
##Termux(Android)

bash

pkg update && pkg upgrade
pkg install git python python-pip
git clone https://github.com/Old-hacker01/fazo-finder.git
cd FazoFinder
chmod +x fazo_finder.py
python fazo_finder.py

