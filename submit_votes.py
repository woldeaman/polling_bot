"""Definition of crawler for poll."""
# -*- coding: utf-8 -*-
import urllib.request as urreq
import argparse as ap


#################
# LINKS TO POLL #
############################################################################################
php_base = 'https://l-blog.de/wp-admin/admin-ajax.php'  # php script runs voting
options = '?action=totalpoll&totalpoll%5BpollId%5D=3478&totalpoll%5Baction%5D=vote&'  # base options
marlenes_vote = 'totalpoll%5Bchoices%5D%5B735e6363-7b6b-4424-9d5f-308c2dd8efbe%5D%5B%5D=2c6dbff5-eda8-4d8e-bbea-65207fa95368'
last_place_vote = 'totalpoll%5Bchoices%5D%5B735e6363-7b6b-4424-9d5f-308c2dd8efbe%5D%5B%5D=ae42c431-1968-4f55-a7f3-0bf9bfc19024'
############################################################################################


##################
#   DEFINITONS   #
############################################################################################
def parser_input():
    """Parse command line input so everyone can vote."""
    parser = ap.ArgumentParser(description=("""Schick votes für Marlen ab."""),
                               formatter_class=ap.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-nbr', dest='nbr', type=int, help='Anzahl der Votes', default=50)
    args = parser.parse_args()

    return args.nbr
############################################################################################


#################
#   MAIN LOOP   #
############################################################################################
def main():
    vote_url = php_base+options+marlenes_vote  # set specific vote
    votes = parser_input()  # set number of votes to commit

    for i in range(votes):  # run the loop
        with urreq.urlopen(vote_url) as f:
            response = f.read().decode('utf-8')
            if "Vielen Dank" in response:
                print(f"Vote {i+1}/{votes} war erfolgreich!")
            else:
                print(f"Vote {i+1}/{votes} hat nicht funktioniert!")
############################################################################################


#############
#  EXECUTE  #
##########################################################################
if __name__ == "__main__":
    main()
##########################################################################
