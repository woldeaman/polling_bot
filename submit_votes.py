"""Definition of crawler for poll."""
# -*- coding: utf-8 -*-
import urllib.request as urreq
import argparse as ap
import numpy as np
import time


#################
# LINKS TO POLL #
############################################################################################
php_base = 'https://l-blog.de/wp-admin/admin-ajax.php'  # php script runs voting
# base options
options = '?action=totalpoll&totalpoll%5BpollId%5D=3478&totalpoll%5Baction%5D=vote&totalpoll%5Bchoices%5D%5B735e6363-7b6b-4424-9d5f-308c2dd8efbe%5D%5B%5D='
# saving ids for all options
all_vote_ids = ["ae42c431-1968-4f55-a7f3-0bf9bfc19024", "ddc6d47d-41a5-41a3-9dc6-2dd20b97dff2", "213b21ad-9fd8-49cd-b7b2-4c8a0bbe1dc6", "21f07488-8ace-4342-a0f0-7e92a016656b",
                "07b13943-faf5-4774-bb2f-01c4c96b9da4", "2c6dbff5-eda8-4d8e-bbea-65207fa95368", "f33385bf-2296-494e-8b66-af64014a0440", "ed4bd68f-3b2a-4c98-a3ad-93cb0e9543c4",
                "b3fc90dc-caa4-405a-b7b3-00c9077ca835"]
############################################################################################


##################
#   DEFINITONS   #
############################################################################################
def parser_input():
    """Parse command line input so everyone can vote."""
    parser = ap.ArgumentParser(description=("""Schick votes für LVB Abstimmung ab."""),
                               formatter_class=ap.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-nbr', dest='nbr', type=int, help='Anzahl der Votes', default=50)
    parser.add_argument('-choice', dest='id', type=int, help='Nummer für die gevoted werden soll', default=6)
    parser.add_argument('-break', dest='brk', type=int, help='Maximaldauer für Pausen (in Sekunden)', default=30)
    args = parser.parse_args()

    return args.nbr, args.id, args.brk
############################################################################################


#################
#   MAIN LOOP   #
############################################################################################
def main():
    vote_nbrs, vote_id, brk_time = parser_input()  # read input
    vote_url = php_base+options+all_vote_ids[vote_id-1]  # set specific vote

    for i in range(vote_nbrs):  # run the loop
        with urreq.urlopen(vote_url) as f:
            response = f.read().decode('utf-8')
            print("Warte auf nächsten Vote...", end='\r')
            time.sleep(np.random.rand()*brk_time)
            if "Vielen Dank" in response:
                print(f"Vote {i+1}/{vote_nbrs} war erfolgreich!", end='\r')
            else:
                print(f"Vote {i+1}/{vote_nbrs} hat nicht funktioniert!")
############################################################################################


#############
#  EXECUTE  #
##########################################################################
if __name__ == "__main__":
    main()
##########################################################################
