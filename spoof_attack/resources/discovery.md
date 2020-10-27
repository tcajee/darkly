# Spoofing

##  To discover the flag:
- Run the VM to serve the website, and navigate to http://0.0.0.0/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c using the IP address provided. 
- Open the browser's DevTools utility to inspect the page (the keyboard shortcut on most browsers is Ctrl+Shift+C).
- Inspect body content the page near the bottom to find the comments:
`You must cumming from : "https://www.nsa.gov/" to go to the next step` and `Let's use this browser : "ft_bornToSec". It will help you a lot.`
- Using these hints we build the following command using `curl`, a tool to transfer data from or to a server, to masquerade as the given browser landing on the page: 
```bash
curl -A 'ft_bornToSec' --referer "https://www.nsa.gov/" "0.0.0.0/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c" | grep "flag"
```
- The flag will be returned in the command output.

### Notes on options and utilites used:

```
-A, --user-agent <name>
    (HTTP) Specify the User-Agent string to send to the  HTTP  server.  

    A user agent is software that acts on behalf of an end user, such as a browser that 'retrieves, renders and facilitates end user interaction with Web content'.

-e, --referer <URL>
    (HTTP) Sends the "Referrer Page" information to the HTTP server.

    A referrer is a website that redirects visitors to your site, that is, the website a person was on before they navigated to your page.
```

