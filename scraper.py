from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def get_urls(file_name):
    """ Extract list of name url pairs from given file. """

    # take in a file name, create an array? that can hold a name and url
    # take file name in from parameter
    # create an array that can hold pairs of data
    # append pairs of data to that array
    # return array? 
    urls = []
    #Set path for file and use open() fuction to open file and read it using 'r' as read option
    # Note: research firs r, remove if necessary 
    with open(file_name, 'r') as infile:
        # Raise an exception if we failed to get any data from the text file 
        if infile.readline().strip() != 'Water District Jobs':
            raise Exception('This is the wrong file')
        for line in infile: 
            if len(line) > 0:
             line[:4] != 'http'
             url.append = line
             print (line)
            else:
                print (line)

    
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_names():

    """ 
    Uses district names and urls to then
    download the page where the list of jobs is found
    and returns the name of the township, the url and a list of jobs, if any.
    """
    """
    Get a district name and print it. 
    Get the matching url and print it. 
    Find all the jobs at that url and print them.
    If there is a problem scraping, print an error message. 
    Repeat until all the district websites are scraped
    """
    # pass a url from the list of district to get_names function.
    get_urls()

    url = 'http://www.btcsd.org/Employment_Opportunities/Employment.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('center'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


if __name__ == '__main__':

    print('')
    print('Getting the list of jobs....')
    names = get_names()
    print('... done.\n')

    names.sort()
    names.reverse()

    print('\nJob scraping results on these websites:\n')
    for name in names:
        print('{}'.format(name))
print('')



    

