

MADNESS is a multi-tool made by Evos Madness (The Head of TWC), for hackers.

It features a DDos tool by the name of FlameGRAVE, that can knock down any network
with ease, as long as the user has activated a VPN. To avoid slowness of their own network, and for anonymity purposes.

As it also contains an SMS Bombing tool by the name of MadSpam. That uses various APIs to ensure a more
high chance of messages being sent to the target number successfully.
note: Target number example: +XXXxxxxxxxx
X = country code
x = target number
`if u put no country code the tool may show that its working but it wont have the specified number to send
the message to, so put a country code.`

Then the third tool helps hackers and network analysts determine information and specifications
about networks, just by entering the Target IP address.

Finally, the 4th tool is a brute force mechanism called RedRipper that is capable of doing admin panel brute forces (MUST ACTIVATE A VPN FOR SAFETY) and capable of cracking SSH and Telnet ( and other IP associated services as long as u got
an open port), (CRUCIAL NOTE: YOU CANNOT BRUTE FORCE SSH WITHOUT INSTALLING SSHPASS, AND U MUST GET A DEDICATED
SSH BRUTEFORCE WORDLIST OTHER THAN THE STOCK WORDLISTS, OR U MUST KNOW THE USERNAME AND ENTER IT IN THE SSH USERNAME FIELD INSTEAD OF THE WORDLIST IF U GOT NO SSH WORDLIST BUT KNOW THE SSH USERNAME [since ssh doesnt validate the username before letting you enter the password, it doesn't validate any input it just goes on with what u enter in the fields and tells u login failed if an input is wrong, that's how it works]).

- Make sure u enter the correct fail string and input login fields while using the Administration Panel brute force option in RedRipper, or else it will give a false positive that it found the right password but it did not.

IMPORTANT : Please use the provided tools ethically and safely. And take permission from the target before
using FLameGRAVE or MadSpam. I am not responsible for any criminal actions done by users of this multi-tool with malicious intent.

Here are instructions on how to begin the MADNESS.
Packages required to run the program:

 `apt update && apt upgrade`
 `pkg install python2`
 `pkg install git`
 `pip2 install requests`
 `pip2 install colorama`
 `pkg install sshpass`
 `pkg install ssh`
 `pkg install openssh`

 no annoying cryptography and compiler installations, since these packages tend to get quirky on termux.

 Beginning the MADNESS:

`git clone https://github.com/therealmadness/MADNESS`
 `cd MADNESS`
 `python2 MADNESS.py`

 Enjoy.

This tool may get updates in the future.
