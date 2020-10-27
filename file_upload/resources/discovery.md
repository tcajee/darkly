# Unrestricted File Upload 

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/?page=upload using the IP address provided.
- Try uploading any file whether or not it is an image. This should fail. 
- Ensure that the `curl` and `grep` utilities are installed on your system.
- Create an empty file called `file.php`, which will serve as the example payload.
- To bypass the front end checks, run the following command from the command line to force the server to accept an arbitrary file as type image/jpeg, remember to change the IP address:
```bash
curl -X POST -F 'Upload=Upload' -F 'uploaded=@file.php;type=image/jpeg' "http://0.0.0.0/?page=upload" | grep "flag"
```
- The flag will be returned as part of the server response, via the grep command.