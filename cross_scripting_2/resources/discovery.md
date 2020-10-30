# Advanced XSS

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/index.php
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Inspect the second National Security agency image to discover a hyperlink to `page=media?src=nsa`.
- Execute the Data URI exploit by doing the following:
    1. Define the JavaScript to be executed. A simple example is something like `alert("XSS attack succesful")`.
    2. [Encode](https://www.base64encode.org/) the JavaScript in base-64 to bypass the MIME-type filter.
    3. Change the value of `src` to store the encoded data URI instead of pointing to a static file: 
    `page=media?src=data:text/html;base64,YWxlcnQoIlhTUyBhdHRhY2sgc3VjY2VzZnVsIik=`
- Click on the image to navigate to the page and get the flag.
