## Unvalidated select

### Vulnerability:

This is an example of a failure to properly validate data passed to the backend of the application. Input validation is a programming technique that ensures only properly formatted data may enter a software system component.

### Avoidance:

This flaw can be mitigated by validating the user inputs both syntactically and semantically valid (in that order) before using it in any way (including displaying it back to the user).

Syntax validity means that the data is in the form that is expected.

Semantic validity includes only accepting input that is within an acceptable range for the given application functionality and context. For example, a start date must be before an end date when choosing date ranges.

### Impact:

Improper validation can lead to injection of malicious input such as code, scripting, commands, that can be interpreted/executed by different targets to exploit vulnerabilities, such as:

- Browser: XSS, XFS, HTML-Splitting
- Data repositories: SQL Injection, LDAP injection
- Server side file processing: XML, XPATH
- Application/Server/O.S: File uploads, Buffer Overflow

### Resources:

- https://owasp.org/www-pdf-archive/Encoded_Attacks_Threats_Countermeasures_9_30_08.pdf
- https://stackoverflow.com/questions/18008017/are-drop-down-select-fields-vulnerable-to-any-sort-of-injection
- https://owasp.org/www-project-proactive-controls/v3/en/c5-validate-inputs

