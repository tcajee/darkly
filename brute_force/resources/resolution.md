## Brute force 

### Vulnerability:

A brute force attack is a popular cracking method where attackers use trial-and-error to guess login info, encryption keys, or find a hidden web page. Hackers work through all possible combinations hoping to guess correctly.

The attack involves ‘guessing’ username and passwords to gain unauthorized access to a system. Brute force is a simple attack method and has a high success rate.

### Avoidance:

There are a few ways to mitigate this kind of attack, including:

- High encryption rates: to make it harder for brute force attacks to succeed, system administrators should ensure that passwords for their systems are encrypted with the highest encryption rates possible, such as 256-bit encryption. The more bits in the encryption scheme, the harder the password is to crack.

- Salt the hash: administrators should also randomize password hashes by adding a random string of letters and numbers (called salt) to the password itself. This string should be stored in a separate database and retrieved and added to the password before it's hashed. By salting the hash, users with the same password have different hashes.

- Two-factor authentication (2FA): additionally, administrators can require two-step authentication and install an intrusion detection system that detects brute force attacks. This requires users to follow-up a login attempt with a second factor, like a physical USB key or fingerprint biometrics scan.

- Limit number of login re-tries: limiting the number of attempts also reduces susceptibility to brute-force attacks. For example, allowing three attempts to enter the correct password before locking out the user for several minutes can cause significant delays and cause hackers to move on to easier targets.

### Resources:

- https://phoenixnap.com/kb/prevent-brute-force-attacks
- https://www.imperva.com/learn/application-security/brute-force-attack/
- https://www.kaspersky.com/resource-center/definitions/brute-force-attack