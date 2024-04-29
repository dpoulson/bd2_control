#!/bin/bash

IUSER=`whoami`
IGROUP=`id -gn ${USER}`
PWD=`pwd`

echo "Setting up service with ${USER}:${GROUP} in ${PWD}"

sed -e "s/GROUP/${IGROUP}/" -e "s/USER/${IUSER}/" -e "s#PWD#${PWD}#" bd2_control.service.tmpl > bd2_control.service
sudo mv bd2_control.service /lib/systemd/system
sudo systemctl enable bd2_control
sudo systemctl start bd2_control


