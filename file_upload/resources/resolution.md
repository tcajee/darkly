## Unrestricted File Upload 

### Vulnerability:

The design of many web applications require that users be able to upload files that will either be stored or processed by the receiving web server.

An insecure form-based file upload allows a cyber-criminal the means to abuse and successfully exploit the server directly, and/or any third party that may later access the file. This can occur through uploading a file containing server side-code (such as PHP) that is then executed when requested by the client.

### Avoidance:

Ways to mitigate this vulnerability:

- Whitelist permitted file types and block all others. This should be conducted on the MIME type of the file rather than its extension.
As the file is uploaded, and prior to being handled (written to the disk) by the server, the filename should be stripped of all control, special, or Unicode characters.
- Ensure that the upload is conducted via the HTTP POST method rather than GET or PUT.
- Ensure that the file is written to a directory that does not hold any execute permission and that all files within that directory inherit the same permissions.
- Scan (if possible) with an up-to-date virus scanner before being stored.
- Ensure that the application handles files as per the host operating system. For example, the length of the file name is appropriate, there is adequate space to store the file, protection against overwriting other files etc.

### Impacts:

The impact of this vulnerability is high, supposed code can be executed in the server context or on the client side. 

Specific impacts include:

- Server-side attacks: The web server can be compromised by uploading and executing a web-shell which can run commands, browse system files, browse local resources, attack other servers, or exploit the local vulnerabilities, and so forth.
Client-side attacks: Uploading malicious files can make the website vulnerable to client-side attacks such as XSS or Cross-site Content Hijacking.
- Uploaded files can be abused to exploit other vulnerable sections of an application when a file on the same or a trusted server is needed (can again lead to client-side or server-side attacks)
- Uploaded files might trigger vulnerabilities in broken libraries/applications on the client side (e.g. iPhone MobileSafari LibTIFF Buffer Overflow).
- Uploaded files might trigger vulnerabilities in broken libraries/applications on the server side (e.g. ImageMagick flaw that called ImageTragick!).
- Uploaded files might trigger vulnerabilities in broken real-time monitoring tools (e.g. Symantec antivirus exploit by unpacking a RAR file)
- A malicious file such as a Unix shell script, a windows virus, an Excel file with a dangerous formula, or a reverse shell can be uploaded on the server in order to execute code by an administrator or webmaster later – on the victim’s machine.

### Resources:

- https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload