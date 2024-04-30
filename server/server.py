import os
import paramiko


def rename_file(file_name):
    try:
        suffix = '.' + file_name.split('.')[-1]
        middle_part = file_name.split('.')[0][0: -11]
        original_date = middle_part[-10:: ]
        my_date = original_date.replace('-', '')
        middle_part = middle_part.replace(original_date, my_date)
        new_file = middle_part + suffix
        print(f'File {file_name} renamed to {new_file}')
        return new_file
    except Exception as e:
        print('Cannot rename file!')
        return file_name


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
        new_file_name = rename_file(os.path.basename(file))
        remote_file = remote_dir + '/' + new_file_name
        sftp.put(file, remote_file)
        print(f'Uploaded file {remote_file}')
    except Exception as e:
        print(e)