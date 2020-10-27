# Unprotected Sensitive Information

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/?page=recover using the IP address provided.
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Inspect the page to find a hidden input field element containing a plaintext email address.
- Edit the element and remove the "hidden" type attribute.
- Select and submit the newly visible input field to get the flag.