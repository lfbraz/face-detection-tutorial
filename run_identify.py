from src.face import Face

# STEPS TO IDENTIFY A PERSON

# Initiate the object
face = Face()

PERSON_GROUP_ID = 'pessoas'
FACES_IMAGE_PATH_TO_BE_IDENTIFIED = ['images/obama/obama_4.jpg',
                                     'images/luiza/IMG_20160213_110652816.jpg',
                                     'images/luiza/IMG_20160226_092750.jpg',
                                     ]

# Identify each the person
for path in FACES_IMAGE_PATH_TO_BE_IDENTIFIED:
    face.identiy_face(person_group_id=PERSON_GROUP_ID, face_image_path=path, is_url=False)
