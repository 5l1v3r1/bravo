# from modules.facebook.scrape import Scrape
#
#
# class Bravo:
#
#     def __init__(self):
#         pass
#
#     def main(self):
#         Scrape().scrape()
#
#
# Bravo().main()

import face_recognition

face1 = face_recognition.load_image_file("faces/face.jpg")
face2 = face_recognition.load_image_file("faces/face2.jpg")
face3 = face_recognition.load_image_file("faces/face3.jpg")
face4 = face_recognition.load_image_file("faces/face4.jpg")
face5 = face_recognition.load_image_file("faces/face5.jpg")
face6 = face_recognition.load_image_file("faces/zucker2.jpg")
face1_encoding = face_recognition.face_encodings(face1)[0]
face2_encoding = face_recognition.face_encodings(face2)[0]
face3_encoding = face_recognition.face_encodings(face3)[0]
face4_encoding = face_recognition.face_encodings(face4)[0]
face5_encoding = face_recognition.face_encodings(face5)[0]
face6_encoding = face_recognition.face_encodings(face6)[0]

known_image = face_recognition.load_image_file("faces/zuck1.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

for distance in face4_encoding:
    print(distance)

results = face_recognition.compare_faces([
    face1_encoding,
    face2_encoding,
    face3_encoding,
    face4_encoding,
    face5_encoding,
    face6_encoding], known_encoding)

print(results)
# print([
#     face1_encoding,
#     face2_encoding,
#     face3_encoding,
#     face4_encoding] - known_encoding)

# print(results)