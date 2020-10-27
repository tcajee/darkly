# Unsanitized Select

##  To discover the flag:

- Run the VM to serve the website, and navigate to http://0.0.0.0/?page=survey using the IP address provided.
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Inspect any of the select drop-down elements and the value of any of its children option elements with a numeric value that's not in the original range.
- Select the newly created value to submit the form and get the flag.