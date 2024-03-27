#!/bin/bash
sudo rm -rf ./secrets
mkdir secrets
ssh-keygen -t rsa -N "" -C "root@0.0.0.0" -f secrets/id_rsa
chmod 400 secrets/id_rsa
cp secrets/id_rsa.pub secrets/id_rsa_container.pub