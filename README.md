# VM Vending Machine

General 
--------
VM Vending Machine is an open source VM creation tool utilizing Ansible and Packer. This tool is currently utilized to
produce CentOS 7 VirtualBox golden images, but will be expanded to include various Linux and Windows machines. Playbooks
and templates are a work in progress, and will be updated as development continues. In its current state, the Vending
Machine processes Packer files in serial, but the intended outcome is to introduce a parallel solution.

Dependencies 
--------
Vending Machine is intended to be used with the following tools:
- Ansible
- Packer
- VirtualBox