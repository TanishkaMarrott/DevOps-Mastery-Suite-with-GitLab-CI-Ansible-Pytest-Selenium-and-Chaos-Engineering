#!/bin/bash

echo \"Starting deployment process...\"
ansible-playbook -i ansible/inventory/production ansible/playbooks/site.yml
