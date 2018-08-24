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

def get_urls():
    """
    Downloads the text where the list of urls is found
    and returns a list with the name of the agency and it's url. """

    """Set path for file and used open() fuction to open file and read it. """
    with open(r"/Users/katherinedey/Desktop/job_scrape/water_jobs_test.txt", 'r') as infile:
        data = infile.read()
        print(data)

    """
    # Raise an exception if we failed to get any data from the text
    raise Exception('Error retrieving contents at {}'.format(data)) """

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
    Downloads the page where the list of jobs is found
    and returns a list of strings, one per job
    """
    
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
    get_urls()
    names = get_names()
    print('... done.\n')

    names.sort()
    names.reverse()

    print('\n Job scraping results on these websites:\n')
    for name in names:
        print('{}'.format(name))
print('')

    

