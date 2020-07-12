# python_ftp_server_client
This module can act as a ftp server to serve files/dir through ftp protocol and also as a ftp client to download and upload files from the server.


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

