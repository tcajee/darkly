# Unrestricted File Upload 

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/?page=upload using the IP address provided.
- Try uploading any file whether or not it is an image. This should fail. 
- Ensure that the `curl` and `grep` utilities are installed on your system.
- Create an empty file called `file.php`, which will serve as the example payload.
- To bypass the front end checks, run the following command using curl, a tool to transfer data from or to a server, from the command line to force the server to accept an arbitrary file as type image/jpeg, remember to change the IP address:
```bash
curl -X POST -F 'Upload=Upload' -F 'uploaded=@file.php;type=image/jpeg' "http://0.0.0.0/?page=upload" | grep "flag"
```
- The flag will be returned as part of the server response, via the grep command.


### Notes on options and utilites used:

```
 -X, --request <command>
    (HTTP) Specifies a custom request method to use when  communicating  with  the
    HTTP  server.  The specified request method will be used instead of the method
    otherwise used (which defaults to GET). Read the HTTP  1.1  specification  for
    details  and  explanations.  Common  additional  HTTP requests include PUT and
    DELETE, but related technologies like WebDAV offers PROPFIND, COPY,  MOVE  and
    more.

 -F, --form <name=content>
    (HTTP SMTP IMAP) For HTTP protocol family, this lets curl emulate a  filled-in
    form  in  which a user has pressed the submit button. This causes curl to POST
    data using the Content-Type multipart/form-data according to RFC 2388.
```