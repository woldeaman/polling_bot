"""Definition of crawler for poll."""
# -*- coding: utf-8 -*-
import urllib


#################
# LINKS TO POLL #
############################################################################################
php_base = 'https://l-blog.de/wp-admin/admin-ajax.php'  # php script runs voting
options = '?action=totalpoll&totalpoll%5BpollId%5D=3478&totalpoll%5Baction%5D=vote&'  # base options
marlenes_vote = 'totalpoll%5Bchoices%5D%5B735e6363-7b6b-4424-9d5f-308c2dd8efbe%5D%5B%5D=2c6dbff5-eda8-4d8e-bbea-65207fa95368'
last_place_vote = 'totalpoll%5Bchoices%5D%5B735e6363-7b6b-4424-9d5f-308c2dd8efbe%5D%5B%5D=ae42c431-1968-4f55-a7f3-0bf9bfc19024'
############################################################################################


#################
# RUN THE VOTES #
############################################################################################
vote_url = php_base+options+marlenes_vote  # set specific vote
votes = 50  # set number of votes to commit

for i in range(votes):  # run the loop
    with urllib.request.urlopen(vote_url) as f:
        print(f.read().decode('utf-8'))
############################################################################################
