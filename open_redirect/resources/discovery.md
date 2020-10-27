# Open Redirect

##  To discover the flag:

- Run the VM to serve the website, and navigate to the landing page of the IP address provided.
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Inspect the Social links in the page footer and change the value of the site query paramater in any of href attributes. For example: href="index.php?page=redirect&site=CHANGEME".
- Click the newly edited link to be redirected and get the flag.