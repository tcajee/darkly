# Brute force 

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/?page=signin using the IP address provided.
- For this flag we will attempt to crack the password with a brute force attack using the `brute_force.py` script.
- Ensure `python` is installed.
- Using a terminal navigate to ./darkly/brute_force/resources, edit the file to replace the IP address, and then run the following command:
```python
python brute_force.py
```
- The flag will appear on the standard output while the script is running.