#!/bin/bash

cd `dirname $0`
ansible-playbook playbook.dev.yml --vault-password-file vault.txt
