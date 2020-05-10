#!/bin/bash

cd `dirname $0`/ansible
ansible-playbook stg.playbook.yml --vault-password-file vault.txt
