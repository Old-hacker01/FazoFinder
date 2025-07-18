#!/usr/bin/env python3

import os
import requests
import json
import argparse
from datetime import datetime
import socket
import whois
from bs4 import BeautifulSoup

VERSION = "2.0"
AUTHOR = "Old-hacker01"
BANNER = f"""
\033[1;35m
  ______      _          ______ _           _            
 |  ____|    | |        |  ____(_)         | |           
 | |__ __ _ __| | ___   | |__   _ _ __   __| | ___ _ __  
 |  __/ _` / _` |/ _ \  |  __| | | '_ \ / _` |/ _ \ '_ \ 
 | | | (_| | (_| |  __/  | |    | | | | | (_| |  __/ | | |
 |_|  \__,_|\__,_|\___|  |_|    |_|_| |_|\__,_|\___|_| |_|
 
 \033[1;37mVersion: {VERSION} | Author: Old-hacker01
 \033[0m
"""

SOCIAL_LINKS = {
    "GitHub": "https://github.com/Old-hacker01",
    "Telegram": "https://t.me/mr_nobody",
    "WhatsApp": "https://wa.me/+255788795305",
    "Twitter": "https://twitter.com/Fazo28_Tz"
}

def print_banner():
    print(BANNER)
    print("\033[1;36mSocial Links:\033[0m")
    for platform, url in SOCIAL_LINKS.items():
        print(f"{platform}: {url}")

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def check_terms():
    print("\n\033[1;31mLEGAL DISCLAIMER:\033[0m")
    print("This tool is for authorized security testing only.")
    print("Unauthorized use is illegal and strictly prohibited.")
    consent = input("Do you agree to use this tool ethically? (yes/no): ").lower()
    return consent == 'yes'

def domain_lookup(domain):
    try:
        # WHOIS lookup
        w = whois.whois(domain)
        print(f"\n\033[1;32mWHOIS Info for {domain}:\033[0m")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        
        # DNS lookup
        print(f"\n\033[1;32mDNS Records for {domain}:\033[0m")
        print(f"IP Address: {socket.gethostbyname(domain)}")
    except Exception as e:
        print(f"Error: {e}")

def email_analysis(email):
    try:
        print(f"\n\033[1;33mChecking breaches for {email}:\033[0m")
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {"User-Agent": "FazoFinder"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            breaches = json.loads(response.text)
            print(f"\n{email} found in {len(breaches)} breaches:")
            for breach in breaches:
                print(f"- {breach['Name']} ({breach['BreachDate']})")
        else:
            print("No breaches found or API limit reached")
    except Exception as e:
        print(f"Error: {e}")

def username_search(username):
    platforms = {
        "GitHub": f"https://github.com/Old-hacker01",
        "Twitter": f"https://twitter.com/Fazo28_Tz",
        "Instagram": f"https://instagram.com/Fazo.28",
        "Reddit": f"https://reddit.com/user/fazo28"
    }
    
    print(f"\n\033[1;34mSearching for {username}:\033[0m")
    for platform, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            print(f"{platform}: {'Found' if r.status_code == 200 else 'Not Found'}")
        except:
            print(f"{platform}: Error")

def generate_report(data, filename="fazo_report.txt"):
    with open(filename, 'w') as f:
        f.write(f"Fazo Finder Report\n{'='*20}\n")
        f.write(data)
    print(f"\nReport saved as {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fazo Finder - Advanced OSINT Tool")
    parser.add_argument("-d", "--domain", help="Domain to investigate")
    parser.add_argument("-e", "--email", help="Email to check for breaches")
    parser.add_argument("-u", "--username", help="Username to search")
    parser.add_argument("-o", "--output", help="Save report", action="store_true")
    args = parser.parse_args()
    
    print_banner()
    if not check_terms() or not check_internet():
        return
    
    results = ""
    
    if args.domain:
        domain_lookup(args.domain)
    elif args.email:
        email_analysis(args.email)
    elif args.username:
        username_search(args.username)
    else:
        parser.print_help()
    
    if args.output and results:
        generate_report(results)

if __name__ == "__main__":
    main()
