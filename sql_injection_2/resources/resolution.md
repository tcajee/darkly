## SQL Injection

### Vulnerability:

When an application is vulnerable to SQL injection and the results of the query are returned within the application's responses, the UNION keyword can be used to retrieve data from other tables within the database. This results in an SQL injection UNION attack. 

The UNION keyword lets you execute one or more additional SELECT queries and append the results to the original query.

### Avoidance:

The only proven method to prevent against SQL injection attacks while still maintaining full application functionality is to use parameterized queries (also known as prepared statements). When utilising this method of querying the database, any value supplied by the client will be handled as a string value rather than part of the SQL query.

Additionally, when utilising parameterized queries, the database engine will automatically check to make sure the string being used matches that of the column. For example, the database engine will check that the user supplied input is an integer if the database column is configured to contain integers.

### Impact:

SQL injection attacks allow attackers to spoof identity, tamper with existing data, cause repudiation issues such as voiding transactions or changing balances, allow the complete disclosure of all data on the system, destroy the data or make it otherwise unavailable, and become administrators of the database server.

In general, SQL Injection is considered a 'high impact' vulnerability.

### Resources:

- https://owasp.org/www-community/attacks/SQL_Injection
- https://portswigger.net/web-security/sql-injection/union-attacks
- https://dev.mysql.com/doc/refman/8.0/en/information-schema.html
- https://www.softwaretestinghelp.com/sql-injection-how-to-test-application-for-sql-injection-attacks/