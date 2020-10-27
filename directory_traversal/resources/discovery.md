# Directory traversal 

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/index.php?page=../ using the IP address provided.
- You see the an alert that saying `wtf`.
- Keep appending additional `../` to the path until you see an alert with `You can DO it !!!  :]`.
- Append `/etc/passwd/` to the path to get the flag.