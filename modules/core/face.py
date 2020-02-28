import cv2
import face_recognition
from dlib.image_dataset_metadata import image
from face_recognition.api import face_detector


class Face:

    """
    Face constructor
    """
    def __init__(self):
        pass

    """
    Detect faces in image
    """
    def detect_face(self, file):
        detected_faces = face_detector(file, 1)

        return detected_faces

    """
    Crop and save the face
    """
    def save(self, faces, image_file, path):
        # Detected faces are returned as an object with the coordinates
        for i, face_rect in enumerate(faces):
            crop = image_file[face_rect.top():face_rect.bottom(), face_rect.left():face_rect.right()]
            cv2.imwrite("faces/detected/%s_%s.jpg" % (path, i), crop)


