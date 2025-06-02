import requests
import re
import webbrowser
import urllib.parse

'''
My idea was to use request module and then scrap but we can use this method too.

'''




choices = {0:'''Instagram content creators''', 1: '''Facebook content creators''', 2: "Tiktok content creators" }


#You can customize it as per your need.
rchoices = {
    0: 'site:instagram.com intext:"2000 followers" OR intext:"3k followers" OR intext:"4k followers" ("@gmail.com" OR "@yahoo.com")',
    1: 'site:facebook.com intext:"2,000 followers" OR intext:"3,000 followers" ("@gmail.com" OR "@yahoo.com")',
    2: 'site:tiktok.com intext:"2k followers" OR intext:"3k followers" OR intext:"4k followers" ("@gmail.com" OR "@yahoo.com")'
}


# query = int(input(f"PLEASE SELECT YOUR TYPE(eg 0,1,2): \n{choices.values()} "))  #looking dirty


def get_emails():



    for keys, values in choices.items():   #This will assign like (0 is key, insta... is value), (...)

        print(f"{keys} --> {values}")



    query = int(input("PLEASE SELECT YOUR TYPE: "))

    result_ = rchoices.get(query)

    '''
    Main logic starts from here you can even find phone number using regex tooo...

    '''

    encoded = urllib.parse.quote_plus(result_)

    url = f"https://www.google.com/search?q={encoded}"
    r = webbrowser.open(url)



#You can adjust the function calling part using a while or even  for loop
# get_emails()

# get_emails()

get_emails()

'''

JUST COPY THE FULL PAGE CONTENT (CTRL+C) AND THEN PASTE TO A FILE NAMED data.txt.... it will gets all the emails. 

'''

# Read and search for emails
with open("data.txt", "r") as f:
    data = f.read()

    # Regular expression to find emails
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", data)

    if emails:
        print("\tScrapping emails from url...... ")
        print("Found emails:")
        for email in emails:

            print(email)

            
            
            with open("emails.txt", "a") as f:   #NEVER use write mode in this case coz it wll overwrite all emails and only saved last one ig
                scrapped_emails = email
                
                f.write(f"{scrapped_emails}\n")



    else:
        print("No email found.")


if __name__ == "__main__":

    print("\tEND OF THE PROGRAM")
