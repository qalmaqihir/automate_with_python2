from bs4 import BeautifulSoup
import requests
import lxml


#########################################################
# Getting the webpage successfully                      #
#########################################################
baseurl="" # use the link
# Send get http request
page=requests.get(baseurl)
print(type(page)) # A Response Object

# Checking if we are successfull
print(page.status_code)
# Verify we had a successful get request webpage
if page.status_code==requests.code.ok:
    print("Successfully get requested")
    # get the whole webpage in beautiful soup formate
    print(page.text) # Not BS format
    bs=BeautifulSoup(page.text,'lxml')


#########################################################
# Scrapping the webpage                                 #
#########################################################
# Finds the first instance of smth you specified in the html
#bs.find("Find this tag in the page")
print(bs.find("Find this tag in the page", class_="attribute of the tag").prettify())
bs.find("Find this tag in the page", class_="attribute of the tag").find("find this inside")
#dig more and more down untill you find the element you need. using find and print to see where you got
# find_all will also help
# the elements will be as a python list with all the staff, you can now loop over this to get the output

list_of_all = bs.find("Find this tag in the page", class_="attribute of the tag").find("find this inside").find_all("tag")
print(list_of_all)

# Triming the list will help narrow down more
# Holding our data
my_data={
    "year":[],
    "Team":[],
    "Player":[]
}

# Loop and store the find the data and store it into the dictionary
# Convert the dictionary into a pandas DataFrame and export it as csv with index = False
