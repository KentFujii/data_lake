#!/bin/bash

cd `dirname $0`
ansible-playbook stg.playbook.yml --vault-password-file vault.txt
