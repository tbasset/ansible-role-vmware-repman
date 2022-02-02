# Ansible Role VMware Replication Manager for vSphere
This is a Ansible Role for Managing and Operating a VM with a defined lifecycle for a Service.

Stages:
- Build
- prepare
    - snap
    - testing changes (--diff)
- deploy 
  
Requirements:
    None

Role Variables:
    - hostname

Using this Role:
  - git clone https://gitlab.com/rstumpner/ansible-role-vmware-repman

Activate role in a playbook or deployment:

Example:
```YAML
- hosts: all
  roles:
     - ansible-role-vmware-repman
```

Tested:
 - vSphere 7

 
License:
    MIT / BSD

Author Information:
roland@stumpner.at