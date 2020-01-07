from src.face import Face

face = Face()
# face.detect_faces_in_image('https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg')
face.detect_faces_in_image(face_image_path='IMG_20160214_124123291.jpg',
                           is_url=False)
