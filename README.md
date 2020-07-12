# python_ftp_server_client
This module can act as a ftp server to serve files/dir through ftp protocol and also as a ftp client to download and upload files from the server.

### FTP Server:

The server app runs in background and logs the connection and requests in Server/logs/server.log file.
```
INFO:pyftpdlib:127.0.0.1:52240-[admin] USER 'admin' logged in.
INFO:pyftpdlib:127.0.0.1:52240-[admin] CWD D:\Codebase\python_ftp_server_client\Server\storage 250
INFO:pyftpdlib:127.0.0.1:52240-[admin] RETR D:\Codebase\python_ftp_server_client\Server\storage\server3.txt completed=1 bytes=24 seconds=0.0
INFO:pyftpdlib:127.0.0.1:52240-[admin] STOR D:\Codebase\python_ftp_server_client\Server\storage\clientfile.txt completed=1 bytes=46 seconds=0.0
INFO:pyftpdlib:127.0.0.1:52240-[admin] FTP session closed (disconnect).
```


### FTP Client CLI:
The Client CLI can be used to connect to the FTP server and to transfer files/dir from or to the server.

```
py .\StartFTPClient.py
Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: L
-rw-rw-rw-   1 owner    group          24 Jul 12 14:52 server3.txt
drwxrwxrwx   1 owner    group           0 Jul 11 19:47 user1

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: CL
clientfile.txt

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: D
Enter filename to download: server3.txt
Download Complete!

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: D
Enter filename to download: unknown
Download Failed...Try again!

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: U
Enter filename to upload: clientfile.txt
Download Complete!

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: U
Enter filename to upload: clientunknown
Download Failed...Try again!

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: L
-rw-rw-rw-   1 owner    group          46 Jul 12 16:13 clientfile.txt
-rw-rw-rw-   1 owner    group          24 Jul 12 14:52 server3.txt

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: CL
clientfile.txt
server3.txt

Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: S
Process Complete!

```

