# Session Hijacking (Cookie Theft)

##  To discover the flag:

- Run the VM to serve the website, and navigate to the landing page of the IP address provided.
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Select the 'Network' DevTools tab, then select the GET request for the landing page (File will be '/' or 'index.php') 
- Select the 'Headers' tab below the list of network request, and inspect the response headers where you should see a Set-Cookie header.   
- Select the 'Application' or 'Storage' DevTools tab and open the 'Cookies' dropdown to list site cookies.
- Copy the 'I_am_admin' cookie value `68934a3e9455fa72420237eb05902327`.
- Decrypting this value using an [MD5 decryption utility](https://hashtoolkit.com/decrypt-md5-hash) returns the value 'false'.
- [Encrypt a new MD5 hash](https://hashtoolkit.com/generate-hash/) using the value 'true' and replace the original value with the new hashed value `b326b5062b2f0e69046810717534cb09`.
- Refresh the page to get the flag.

