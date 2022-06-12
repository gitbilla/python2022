#!/root/PYTHON-Scripts/bin/python3
ip = input("Enter IP Remote Server :")

import paramiko
def connect_SSH():
    ssh = paramiko.SSHClient()
    username = 'root'
    port = 22
    #ip = '192.168.0.15'
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username)
    stdin, stdout, stderr = ssh.exec_command('/root/sample.sh') # run remote command
    outlines = stdout.readlines()
    resp=''.join(outlines)
    print(resp)
connect_SSH()
