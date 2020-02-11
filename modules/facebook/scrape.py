import requests


class Scrape:

    def __init__(self):
        self.selectors = {
            'name': '_2nlw _2nlv',
            'work': 'fbProfileEditExperiences',
            'education': 'fbProfileEditExperiences'
        }

    """
    Loop through a range, check if the profile has been indexed
    if it's not, index it, with the pictures, likes, general info
    """
    def scrape(self):
        for profile in range(4,5):
            uri = 'https://facebook.com/profile.php?id=%d' % profile
            with requests.get(uri) as response:
                print(response.content)


