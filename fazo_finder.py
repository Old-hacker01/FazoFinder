#!/usr/bin/env python3

import os
import requests
import json
import argparse
from datetime import datetime

VERSION = "1.0"
AUTHOR = "Fazo28"
BANNER = f"""
\033[1;35m
  ______      _          ______ _           _            
 |  ____|    | |        |  ____(_)         | |           
 | |__ __ _ __| | ___   | |__   _ _ __   __| | ___ _ __  
 |  __/ _` / _` |/ _ \  |  __| | | '_ \ / _` |/ _ \ '_ \ 
 | | | (_| | (_| |  __/  | |    | | | | | (_| |  __/ | | |
 |_|  \__,_|\__,_|\___|  |_|    |_|_| |_|\__,_|\___|_| |_|
 
 \033[1;37mVersion: {VERSION} | Author: {AUTHOR}
 \033[0m
"""

def print_banner():
    print(BANNER)

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def check_terms_of_service():
    print("\n\033[1;31mIMPORTANT LEGAL NOTICE:\033[0m")
    print("This tool is for educational and authorized security testing only.")
    print("Unauthorized use to gather personal information is illegal.")
    print("By using this tool, you agree to use it only for lawful purposes.\n")
    
    consent = input("Do you agree to these terms? (yes/no): ").lower()
    return consent == 'yes'

def domain_lookup(domain):
    try:
        url = f"https://api.viewdns.info/dnsrecord/?domain={domain}&apikey=demo&output=json"
        response = requests.get(url)
        data = response.json()
        
        print(f"\n\033[1;32mDNS Records for {domain}:\033[0m")
        if 'records' in data['response']:
            for record in data['response']['records']:
                print(f"{record['type']}: {record['address']}")
        else:
            print("No DNS records found.")
    except Exception as e:
        print(f"Error in domain lookup: {e}")

def email_analysis(email):
    print(f"\n\033[1;33mBasic Email Analysis for {email}:\033[0m")
    print("Note: This only checks for breaches using HaveIBeenPwned API")
    
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {"User-Agent": "FazoFinder"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            breaches = json.loads(response.text)
            print(f"\n{email} was found in {len(breaches)} breaches:")
            for breach in breaches:
                print(f"- {breach['Name']} ({breach['BreachDate']})")
        elif response.status_code == 404:
            print("No breaches found for this email.")
        else:
            print("Could not check breaches (API limit or error).")
    except Exception as e:
        print(f"Error checking breaches: {e}")

def username_search(username):
    print(f"\n\033[1;34mBasic Username Search for {username}:\033[0m")
    print("Checking common social media platforms...")
    
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}"
    }
    
    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{site}: \033[1;32mFound\033[0m - {url}")
            else:
                print(f"{site}: \033[1;31mNot Found\033[0m")
        except:
            print(f"{site}: \033[1;31mError checking\033[0m")

def generate_report(query, results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"fazo_report_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"Fazo Finder Report - {timestamp}\n")
        f.write(f"Query: {query}\n\n")
        f.write(results)
    
    print(f"\nReport saved as {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fazo Finder - Ethical OSINT Tool")
    parser.add_argument("-d", "--domain", help="Perform DNS lookup on a domain")
    parser.add_argument("-e", "--email", help="Check if email was involved in breaches")
    parser.add_argument("-u", "--username", help="Search for username across social media")
    parser.add_argument("-o", "--output", help="Save results to a file", action="store_true")
    args = parser.parse_args()
    
    print_banner()
    
    if not check_terms_of_service():
        print("\nYou must agree to the terms to use this tool.")
        return
    
    if not check_internet():
        print("\n\033[1;31mError: No internet connection detected.\033[0m")
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
        generate_report(args.domain or args.email or args.username, results)

if __name__ == "__main__":
    main()
