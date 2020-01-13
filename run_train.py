from src.face import Face

# STEPS TO TRAIN THE COGNITIVE MODEL

# Initiate the object
face = Face()

# Create a person group
PERSON_GROUP_ID = 'pessoas'
face.create_person_group(PERSON_GROUP_ID)

# Create a level related to an existing person group
# In our case will be used to identify the person
PERSON_1 = 'obama'

person_id = face.add_person_group_level(PERSON_GROUP_ID, PERSON_1)
print(person_id)

# Assign a person image to a person group
FACES_IMAGE_PATH = ['images/obama/obama_1.jpg',
                    'images/obama/obama_2.jpg',
                    'images/obama/obama_3.jpg']

for path in FACES_IMAGE_PATH:
    face.assign_person_image_to_person_group(PERSON_GROUP_ID, person_id, path)


PERSON_2 = 'luiza'

person_id = face.add_person_group_level(PERSON_GROUP_ID, PERSON_2)
print(person_id)

# Assign a person image to a person group
FACES_IMAGE_PATH = ['images/luiza/IMG_20160213_110618494.jpg',
                    'images/luiza/IMG_20160213_110651269.jpg',
                    'images/luiza/IMG_20160213_110652816.jpg',
                    'images/luiza/IMG_20160214_124123291.jpg'
                    ]

for path in FACES_IMAGE_PATH:
    face.assign_person_image_to_person_group(PERSON_GROUP_ID, person_id, path)

# Train a person group
face.train_person_group(PERSON_GROUP_ID)
