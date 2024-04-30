import os
import paramiko


def connect_to_sftp(hostname: str, username: str, password: str, port: int) -> paramiko.SFTPClient | None:
    try:
        transport = paramiko.Transport((hostname, port));
        transport.connect(username=username, password = password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        print('Connected to', hostname)
        return sftp
    except Exception as e:
        print(e)


def upload_file(sftp: paramiko.SFTPClient, file: str, remote_dir='') -> None:
    try:
        remote_file = remote_dir + '/' + os.path.basename(file)
        sftp.put(file, remote_file)
        print(f'Uploaded file {remote_file}')
    except Exception as e:
        print(e)