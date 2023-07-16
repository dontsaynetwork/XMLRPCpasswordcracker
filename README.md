# XMLRPCpasswordcracker
This is a simple Python script which tries to crack a wordpress password using the XMLRPC.php

This script uses the xmlrpc page to tries to bruteforce the login. The script
will try the same password on a list of login that the user will provide. The logins can be found 
by going to http://www.target-blog.com/wp-json/wp/v2/users.

This script would then save the password that were succesful into a text file.

This is an ongoing project that requires more testing and validating.

As usual, this script is for educational purposes while I work more on my Python programming skills
and is not intended for use outside of the educational scope.
