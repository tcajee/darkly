## Cross-Site Scripting (XSS)

### Vulnerability:

Data URI, defined by [RFC 2397](https://tools.ietf.org/html/rfc2397), is a way of embedding small files inline in HTML documents. Instead of linking to a file stored locally on the server, the file is provided within the URL itself as a base64-encoded string of data preceded by a mime-type.

Data URI’s are considered as self-content entities because the data pointing to an external source can instead be stored in Data URI’s, decreasing the fetch time.

Data URI’s are considered to be hostile as they can be used to execute JavaScript stored in them. Values stored in data URI’s can also be encoded using base-64 encoding in order to bypass the filter. 

### Avoidance:

When handling Data URI’s, check if the payload is encoded in base64. If encoded, decode it and check if it contains any malicious scripts before executing the payload.

### Resources:

- https://www.paladion.net/blogs/bypass-xss-filters-using-data-uris
- https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
- https://tools.ietf.org/html/rfc2397