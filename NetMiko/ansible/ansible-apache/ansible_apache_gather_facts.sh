# show ipv4 address
echo"----"
echo "IPV4 ADDRESS"
ip addr | grep "inet "
echo "----"
# show ansible config file 
echo "ANSIBLE CONFIG FILE"
cat ansible.cfg
echo "----"
# check ansible version
echo "ANSIBLE VERSION"
ansible --version
echo "----"
# show ansible inventory file(hosts)
echo "ANSIBLE INVENTORY"
cat hosts
echo "----"
# verify status of apache no local server 
echo "VERIFY IF APACHE2 IS ACTIVE"
sudo systemctl status APACHE2
echo "----"