import urllib


class Images:

    # Read image from url
    def get_image(self, uri):
        image = urllib.urlopen(uri).read()

        return image
