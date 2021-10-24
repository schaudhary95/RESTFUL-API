import pytest
import requests

url = "https://duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1"

response = requests.get(url).json()

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
    "Joseph Robinette Biden"
]

actualLastName = []
for i in list_of_president_names:
    actualLastName.append(i.split(' ')[-1])

presidentLastNamesFromResponse = []
for i in range(len(response["RelatedTopics"])):
    if response["RelatedTopics"][i]['FirstURL'].split('/')[-1].split('_')[-1] in actualLastName:
        presidentLastNamesFromResponse.append(
            response["RelatedTopics"][i]['FirstURL'].split('/')[-1].replace('_', ' ').split(' ')[-1])


@pytest.mark.parametrize("actualPresidentLastName", ['Adams', 'Biden', 'Buchanan', 'Buren',
                                                     'Bush', 'Bush', 'Carter',
                                                     'Cleveland', 'Clinton', 'Coolidge',
                                                     'Eisenhower', 'Fillmore', 'Ford',
                                                     'Garfield', 'Grant', 'Harding',
                                                     'Harrison', 'Harrison', 'Hayes',
                                                     'Hayes', 'Hayes', 'Hoover', 'Jackson',
                                                     'Jefferson', 'Johnson', 'Johnson',
                                                     'Kennedy', 'Lincoln', 'Madison',
                                                     'McKinley', 'Monroe', 'Nixon',
                                                     'Obama', 'Pierce', 'Polk', 'Reagan',
                                                     'Roosevelt', 'Roosevelt', 'Taft',
                                                     'Taylor', 'Truman', 'Trump', 'Tyler',
                                                     'Washington', 'Wilson'])
def test_EachPresidentInList(actualPresidentLastName):
    assert actualPresidentLastName in presidentLastNamesFromResponse
