from src.face import Face
from os import listdir
from os.path import isfile, join


def __assign_person_image_to_person_group__(person_group_id, person_name, faces_image_path):
    person_id = face.add_person_group_level(person_group_id, person_name)
    print('{} added to the person_group {}'.format(person_name, person_group_id))

    image_files = [f for f in listdir(faces_image_path) if isfile(join(faces_image_path, f))]

    for path in image_files:
        face.assign_person_image_to_person_group(person_group_id, person_id, path)


def __train_model__(face, person_group_id):
    # Train a person group
    face.train_person_group(PERSON_GROUP_ID)


# STEPS TO TRAIN THE COGNITIVE MODEL
if __name__ == "__main__":
    PERSON_GROUP_ID = 'pessoas'

    # Initiate the object
    face = Face()

    # Create a person group
    face.create_person_group(PERSON_GROUP_ID)

    # Assign persons to the person group
    __assign_person_image_to_person_group__(PERSON_GROUP_ID, 'BARACK OBAMA', 'images/train/obama')
    __assign_person_image_to_person_group__(PERSON_GROUP_ID, 'LEWIS HAMILTON', 'images/train/hamilton')
    __assign_person_image_to_person_group__(PERSON_GROUP_ID, 'LUIZ BRAZ', 'images/train/luiz')

    # Train the model
    __train_model__(PERSON_GROUP_ID)
