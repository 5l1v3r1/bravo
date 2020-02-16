import requests, sys
from bs4 import BeautifulSoup
from modules.core.face import Face
from modules.core.images import Images


class Scrape:

    """
    Scrape constructor, contains scraping selectors
    """
    def __init__(self):
        self.face = Face()
        self.images = Images()
        self.selectors = {
            'name': '_2nlw _2nlv',
            'profile_picture': '_11kf img',
            'images': {
                'parent': '_2a2q _1m6c',
                'child': '_xcx'
            },
            'sections': {
                'parent': '_4qm1',
                'child': 'clearfix _h71',
                'title': '_2lzr _50f5 _50f7',
                'description': '_173e _50f8 _2ieq'
            },
        }

    """
    Loop through a range, check if the profile has been indexed
    if it's not, index it, with the pictures, likes, general info
    Store the face encoding in the database
    """
    def scrape(self):
        for profile in range(4, 5):
            uri = 'https://facebook.com/profile.php?id=%d' % profile
            with requests.get(uri) as response:
                soup = BeautifulSoup(response.content, features="html.parser")
                profile_picture = self.profile_photo(soup)
                featured_images = self.featured_photos(soup)
                # work = self.sections(soup)

                # Save the image to a temp folder
                temp_image = self.images.save(profile_picture)
                image = self.images.read(temp_image)

                # Detect the face from the image and save it
                decected_faces = self.face.detect_face(image)
                save = self.face.save(decected_faces)
                print(save)

    """
    Get the profiles profile photo
    """
    def profile_photo(self, soup):
        picture = soup.find('img', class_=self.selectors['profile_picture'])

        return picture['src']

    """
    Get the feature profile photos
    """
    def featured_photos(self, soup):
        images = soup.find_all('img', class_=self.selectors['images'])

        return images

    """
    Sections contains, work, education, quotes
    """
    def sections(self, soup):
        sections = soup.find_all('div', class_=self.selectors['sections']['parent'])
        general_information = []
        for section in sections:
            print(section)

            general_information.append({
                section.div.span.text: {

                }
            })

            for part in section.ul.contents:
                print(part.div.contents)
                # print(part.div.contents.find_next_siblings('div')[1])

            # print(section)
            sys.exit(1)


