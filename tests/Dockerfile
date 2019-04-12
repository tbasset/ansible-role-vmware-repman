FROM ubuntu:xenial
MAINTAINER Roland Stumpner <roland.stumpner@fh-ooe.at>

# Copy the TERENA CA to Container:
#COPY DigiCertCA.crt /usr/local/share/ca-certificates/

RUN apt update && \
    apt install --no-install-recommends -y python-minimal software-properties-common git vim iputils-ping mtr dnsutils rsync tree python-pip && \
    apt-add-repository ppa:ansible/ansible && \
    apt update && \
    apt install -y ansible \
    python-markupsafe python-ecdsa libyaml-0-2 \
    python-jinja2 python-yaml python-paramiko python-httplib2 \
    python-crypto sshpass && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
echo '[local]\nlocalhost\n' > /etc/ansible/hosts && \
pip install pysphere && \
pip install pyvmomi && \
# pip install pysphere && \
update-ca-certificates && \
git config --global http.sslVerify false

# Write DNS File
# echo 'search\rmgmt.fhooe.at\nnameserver 10.140.50.12\noptions\rndots:0' > ~/resolv.conf

# ENV ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD=True

#COPY DigiCertCA.crt /usr/local/share/ca-certificates/
# Set git repo SSL Settings
# Set git repo Creds
# Fetch the git Repo:
# CMD ["ansible-playbook","-i","/opt/ansible-playbooks/fhooe-ansible-networkconfig/fhooe-network-inventory","/opt/ansible-playbooks/fhooe-ansible-networkconfig/fhooe.yml","--limit","wel-network-rz"]

# Copy Ansible Vault File
#COPY vault-password /opt/

# Execute the Ansible Playbook:
CMD ["git","config","--global","http.sslVerify","false"]
#CMD ["ansible-playbook","-i","/opt/ansible-playbooks/fhooe-ansible-networkconfig/fhooe-network-inventory","/opt/ansible-playbooks/fhooe-ansible-networkconfig/fhooe.yml","--limit","wel-network-staging,wel-network-ca-access,zen-network"]
