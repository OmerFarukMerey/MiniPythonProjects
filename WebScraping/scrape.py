import pprint
import requests                                                             # Allows us to download HTML initially
from bs4 import BeautifulSoup                                               # Allows us to use HTML and grab different data

def main():
    res = requests.get('https://news.ycombinator.com/')                     # Change the parameter of this function to search in other pages
    soup = BeautifulSoup(res.text, 'html.parser')

    title_link_list = soup.select('.titlelink')                             # Here we grabbed the links
    subtext_list = soup.select('.subtext')                                  # Here we grabbed the link scores

    def eliminate_points_part(points_str):                                  # Eliminates the string part and returns only the integer part of the text
        return points_str.replace(" points", "")

    def sort_stories_by_points(hn_list):                                    # Reverse sort so that we see from the highest to lowest
        return sorted(hn_list, key=lambda k:k['points'], reverse=True)

    def create_custom_hn(links, scores):                                    # Creates the Hacker News List and returns the sorted version of it.
        hn = []
        for index, item in enumerate(links):                                    
            title = item.getText()                                          # Title Name of the News
            href = item.get('href', None)                                   # Link of the News
            votes = scores[index].select('.score')                          # Points/Upvotes of the News
            
            if len(votes):                                                  # If the votes have attribute '.score' aka class                                              
                points = eliminate_points_part(votes[0].getText())          # Grab the points with the help of our method
                hn.append(                                                  #   
                    {                                                       #
                        'title' : title,                                    #
                        'link' : href,                                      # Filling the Hacker News List with News Dictionaries          
                        'votes' : points                                    #
                    }                                                       #
                )                                                           #
            
        return sort_stories_by_points(hn)                                   

    hn_list = create_custom_hn(title_link_list, subtext_list)               # Call of the function
    pprint.pprint(hn_list)                                                  # Pretty Print of our Hacker News List
    
if __name__ == '__main__':
    main()    