import requests, shutil, cv2


class Images:

    """
    Read an image from its temp folder
    """
    def read(self, path):
        return cv2.imread(path)

    """
    Save the image to a temp directory from a URL
    """
    def save(self, uri):
        with requests.get(uri, stream=True) as response:
            if response.status_code != 200:
                return

            with open(self.path(uri), 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)

                return self.path(uri)

    """
    Get the name of the file from a URL
    """
    def name(self, uri):
        path = uri.split('_')

        return '%s_%s' % (path[1], path[2])

    """
    Create and get the temp path from the name
    """
    def path(self, uri):
        return 'faces/tmp/%s.jpg' % self.name(uri)
