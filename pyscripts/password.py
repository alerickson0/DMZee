## Purpose: To generate an encrypted password that has many uses. One is generating an encrypted password for a CentOS user in a ks.cfg (kick start) file
## Python versions supported: 3.7.3, 3.6.x

import passlib.hash,getpass

pw=getpass.getpass()
print(passlib.hash.sha256_crypt.hash(pw) if (pw==getpass.getpass("Confirm: ")) else exit())