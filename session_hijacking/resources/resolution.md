## Session Hijacking (Cookie Theft)

### Vulnerability:

HTTP by itself is a stateless protocol. Therefore the server is unable to determine which requests are performed by which client, and which clients are authenticated or unauthenticated.

The use of HTTP cookies within the headers, allows a web server to identify each individual client and can therefore determine which clients hold valid authentication, from those that do not. These are known as session cookies.

When one visits a website, the remote server may leave an HTTP cookie on one's computer, where they are often used to authenticate identity upon returning to the website.

The cookie is often used like a ticket to identify a particular event or transaction; in this case to identify whether a user is an admin.

By using HTTP Cookies to store the 'I_am_admin' cookie in the browser on the client side, the born_to_sec website is vulnerable to the cookie theft. An attacker can impersonate an admin user by modifying the cookie value. 

### Avoidance:
Methods of mitigating cookie theft attacks include: 

- Making secondary checks against the identity of the user. For instance, a web server could check with each request made that the IP address of the user matched the one last used during that session. This does not prevent attacks by somebody who shares the same IP address, however, and could be frustrating for users whose IP address is liable to change during a browsing session.
- Changing the value of the cookie with each and every request. This dramatically reduces the window in which an attacker can operate and makes it easy to identify whether an attack has taken place.
- Setting an additional HttpOnly flag in the Set-Cookie HTTP response header. Using the HttpOnly flag when generating a cookie helps mitigate the risk of client side script accessing the protected cookie (if the browser supports it).

Some of the operations that can be done using cookies can also be done using other mechanisms, including:

- JSON Web Tokens
A JSON Web Token (JWT) is a self-contained packet of information that can be used to store user identity and authenticity information. This allows them to be used in place of session cookies. Unlike cookies, which are automatically attached to each HTTP request by the browser, JWTs must be explicitly attached to each HTTP request by the web application.

- HTTP authentication
The HTTP protocol includes the basic access authentication and the digest access authentication protocols, which allow access to a web page only when the user has provided the correct username and password. If the server requires such credentials for granting access to a web page, the browser requests them from the user and, once obtained, the browser stores and sends them in every subsequent page request. This information can be used to track the user.


### Impact:
Several possible security impacts exist once this vulnerability is exploited:

- Services “identify” the user from the cookies and offer a personalized version of the website, thus, exposing the user’s personal information and account functionality to the adversary.
- Using the stolen cookie, in some cases an adversary can infer sensitive data about the user. For example, depending on the attacker’s goal, they could employ a precompiled dictionary of sensitive keywords for finding sensitive web activity.
- The stolen cookie information can be leveraged to bypass 2FA techniques as the cookie is in the end still a single factor.


### Resources:
- https://en.wikipedia.org/wiki/Session_hijacking
- https://embracethered.com/blog/posts/passthecookie/
- https://resources.infosecinstitute.com/risk-associated-cookies/
- https://owasp.org/www-community/HttpOnly