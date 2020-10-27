# SQL Injection

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/index.php?page=searchimg using the IP address provided.
- Enter valid integers as IDs to test the application output. You should see the input directly returned as the ID value and that query results are sent back with the application responses which consists of 2 columns. This confirms that the query is vulnerable to union attacks that use the same number of columns. (Entering the number 5 gives you a hint as to which row will contain the target flag)
- Get the name of the table using information_schema object using the following query:
```bash
5 UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema = database()
```
- Get the column names using the table name returned in the 'Url' field with the following query:
```bash
5 UNION SELECT column_name, null FROM information_schema.columns WHERE table_schema = database()
```
- Get the flag by checking the values for each column returned in the 'Url' field. Otherwise, if you don't want to manually check each one, the answer to the next step is in the title and comment columns:
```bash
5 UNION SELECT title, comment FROM list_images
```
- Decrypting the result of the last step using an [MD5 decryption utility](https://hashtoolkit.com/decrypt-md5-hash) returns the value `albatroz`, which should be lowercased as instructed.
- Run the lowercased result through an [SHA256 calculator](https://xorbin.com/tools/sha256-hash-calculator) to get the flag.