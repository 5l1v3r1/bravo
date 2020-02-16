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
    def save(self, faces):

        print(faces)
        # Detected faces are returned as an object with the coordinates
        for i, face in enumerate(faces):
            crop = image[face.top():face.bottom(), face.left():face.right()]
            cv2.imwrite("./.faces/aligned_face_{}_{}_crop.jpg".format('file_name'.replace('/', '_'), i), crop)

