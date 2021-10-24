import requests

url = "https://duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1"

list_of_president_names = [
    "George Washington",
    "John Adams",
    "Thomas Jefferson",
    "James Madison",
    "James Monroe",
    "John Quincy Adams",
    "Andrew Jackson",
    "Martin Van Buren",
    "William Henry Harrison",
    "John Tyler",
    "James K. Polk",
    "Zachary Taylor",
    "Millard Fillmore",
    "Franklin Pierce",
    "James Buchanan",
    "Abraham Lincoln",
    "Andrew Johnson",
    "Ulysses S. Grant",
    "Rutherford B. Hayes",
    "James Garfield",
    "Rutherford B. Hayes",
    "Rutherford B. Hayes",
    "Benjamin Harrison",
    "Grover Cleveland",
    "William McKinley",
    "Theodore Roosevelt",
    "William Howard Taft",
    "Woodrow Wilson",
    "Warren G. Harding",
    "Calvin Coolidge",
    "Herbert Hoover",
    "Franklin D. Roosevelt",
    "Harry S. Truman",
    "Dwight D. Eisenhower",
    "John F. Kennedy",
    "Lyndon B. Johnson",
    "Richard M. Nixon",
    "Gerald R. Ford",
    "James Carter",
    "Ronald Reagan",
    "George H. W. Bush",
    "William J. Clinton",
    "George W. Bush",
    "Barack Obama",
    "Donald J. Trump",
    "Joseph Robinette Biden",
]

response = requests.get(url).json()
presidentLastNamesFromResponse = []
for i in range(len(response["RelatedTopics"])):
    presidentLastNamesFromResponse.append(
        response["RelatedTopics"][i]['FirstURL'].split('/')[-1].replace('_', ' ').split(' ')[-1])


newList = []
for i in list_of_president_names:
    lastName = i.split()[-1]
    newList.append(lastName)

counter = True

for i in newList:
    if i not in presidentLastNamesFromResponse:
        counter = False
print(counter)
