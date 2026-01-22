# install ssh server 
sudo apt-get install openssh-server

#install sshpass utility - inject the password automatically into the ssh command
sudo apt-get install sshpass

# enable ssh server
sudo systemctl start ssh 