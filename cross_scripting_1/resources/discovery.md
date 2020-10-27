# XSS

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/index.php?page=feedback using the IP address provided.
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Inspect the 'Name' input field, edit the element to add `value="script"`.
- Submit the form to get the flag.`