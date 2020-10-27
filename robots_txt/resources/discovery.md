# Robots.txt 

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/robots.txt using the IP address provided.
- The following directory structure should be provided:
```bash
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
- Navigate to http://0.0.0.0/whatever and download the htpassword which contains the admin details `root:8621ffdbc5698829397d97767ac13db3`.
- Decrypting this value using an [MD5 decryption utility](https://hashtoolkit.com/decrypt-md5-hash) returns the value 'dragon'.
- Navigate to http://0.0.0.0/admin and login using username `root` and password `dragon` to get the flag. 