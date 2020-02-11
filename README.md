# bravo

Scrape facebook for pictures, store likes and general information. Train the facial recognition, and examine the input feed.


### Installation

todo


### Todo


- Scrape Facebook/Instagram/Twitter/Youtube/Vimeo etc (add a service)
- When an image is found, get the face encoding/distance
- Face/Person lookup, return all the information on them, use a % of likeliness.
- Tables:
    - person
        * id
        * name
        * information (json: work, education, likes, religion, politics.. etc)
    - faces:
        * id
        * person_id
        * encoding array (face recog points, when searching use a euclidean distance sqrt((encoding_1 - image_encoding1) + ...))
        * image_id
        * created_at
    - images:
        * id
        * location
        * exif

