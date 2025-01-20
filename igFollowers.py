from bs4 import BeautifulSoup

def get_people_from_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    people = set()  # Set to store people's names

    # Assuming names are in <li> elements, modify the code based on your HTML structure
    for link in soup.find_all('a',href=True):  # Adjust the tag if necessary
        person_name = link.get_text(strip=True)
        if person_name:     
            people.add(person_name)
    
    return people

def find_people_you_follow_not_following_you(followers, following):
    # Find people you follow that do not follow you
    not_following_back = [person for person in following if person not in followers]
    return not_following_back

# TODO: Path locations
# followers_file =  # for example: '/Users/username/Desktop/followers.html'  
# following_file = # for example: '/Users/username/Desktop/following.html'  

# Extract people from both files
followers = get_people_from_html(followers_file)
following = get_people_from_html(following_file)

# Find people you follow but who do not follow you
result = find_people_you_follow_not_following_you(followers, following)

print("People you follow but do not follow you:")
for person in result:
    print(person)
