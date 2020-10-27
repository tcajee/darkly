## Diretory Traversal

### Vulnerability:

Directory traversal, also called path traversal, is a vulnerability that allows attackers to break out of a web server’s root directory and access other locations in the server's file system.

A bug in the web server software may allow the web server process to access files outside the web document root. If a web application also uses file names taken from user inputs without proper input validation, this could open up a path traversal vulnerability. 

### Avoidance:

Path traversal attacks rely on two vulnerable elements: the web application code and the web server configuration. By taking care to avoid vulnerabilities in both areas, you can mitigate the majority of such attacks.

To mitigate the vulnerability on the web server side, ensure you are using up-to-date web server software. The web server process should also run with the minimum necessary privileges and only have access to directories that the website or application actually needs. For Linux/UNIX systems, you may want to consider running the web server in a chroot jail to contain any path traversal attacks that do succeed.

Modern applications generally avoid this by using URL mapping to separate the URLs from the underlying files. In fact, if you use a CMS or web development framework, this is often the default approach. A related solution is to store files in a central database, not directly in the web server file system, and define your own resource names used to access them.

### Impact:

Instead of valid file names, an attacker can then enter relative or absolute file paths to access arbitrary files, including application source code, system files, server logs, and other files containing sensitive information. If combined with some kind of file upload vulnerability, directory traversal can even lead to remote code execution.

### Resources:

- https://owasp.org/www-community/attacks/Path_Traversal
- https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.
- https://portswigger.net/web-security/file-path-traversal
- https://www.netsparker.com/blog/web-security/directory-path-traversal-attacks/0i