# 

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/.hidden using the IP address provided.
- The flag is contained inside a file deeply nested inside one of the directories listed.
- To help automate the discovery, first create an empty directory called 'flag' using `mdkir`.
- Ensure that `wget`, a free utility for non-interactive download of files from the Web, is installed.
- Download all files using the following command (This can take a while... there are around 17500 files to download):
```bash
wget --mirror -A README -P ./flag -e robots=off http://0.0.0.0/.hidden/
```
- Pipe discovered filenames found using the `find` command as arguments  to `grep` which searches for the alpha numeric pattern and then pipe any results to `cut` to print out the flag part only:
```bash
find ./flag -name README | xargs grep -E '[a-z][0-9]' | cut -d : -f2
```
 
### Notes on options and utilites used:

wget:
```
--mirror: Turn on options suitable for mirroring. This option turns on recursion and time-stamping, sets infinite recursion depth and keeps FTP directory listings.
-A: Recursive Accept. Used to enforce downloading of README files only.

-P: Set directory prefix to prefix.  The directory prefix is the directory where all
    other files and subdirectories will be saved to, i.e. the top of the retrieval
    tree.

-e: execute command robot=off turns off robot exclusion)
```
xargs: used to build and execute command lines from standard input effectively turning its stdin into arguments piped to chained commands.

grep: searches for PATTERNS in each FILE.

cut: prints selected parts of lines from each FILE to standard output.
