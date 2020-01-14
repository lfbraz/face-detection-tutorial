from src.face import Face


def __identify_person__(person_group_id, faces_image_path, person_name='', is_url=True):
    # Identify the person
    for path in FACES_IMAGE_PATH_TO_BE_IDENTIFIED:
        print('Trying to identify {}'.format(PERSON_NAME))
        face.identify_face(person_group_id=PERSON_GROUP_ID, face_image_path=path, is_url=is_url)
        print()


# STEPS TO IDENTIFY A PERSON
# Initiate the object
face = Face()

PERSON_GROUP_ID = 'pessoas'

PERSON_NAME = 'OBAMA'  # just used to compare with the prediction
FACES_IMAGE_PATH_TO_BE_IDENTIFIED = [
                                     'https://www.bing.com/th/id/OIP.ejdLBddFrjF3iPOsATlLUQHaLP?w=154&h=211&c=7&o=5&dpr=1.25&pid=1.7',
                                     'https://www.bing.com/th/id/OIP.zYyJds0-XXOihPTEd3PPmAHaKF?w=171&h=211&c=7&o=5&dpr=1.25&pid=1.7',
                                     'https://www.bing.com/th/id/OIP.ORj2a1q5IkftuWwl_2KuaAHaE7?w=246&h=162&c=7&o=5&dpr=1.25&pid=1.7',
                                     'https://www.bing.com/th/id/OIP.EYJH0V48q8x5WE3wxBdESQHaD4?w=300&h=157&c=7&o=5&dpr=1.25&pid=1.7',
                                     'https://www.bing.com/th/id/OIP.MQmLcNYpIfEe7B86HOYLIwHaFj?w=288&h=213&c=7&o=5&dpr=1.25&pid=1.7',
                                     ]

__identify_person__(PERSON_GROUP_ID, FACES_IMAGE_PATH_TO_BE_IDENTIFIED, PERSON_NAME)

PERSON_NAME = 'HAMILTON'  # just used to compare with the prediction
FACES_IMAGE_PATH_TO_BE_IDENTIFIED = [
                                     'https://www.bing.com/th/id/OIP.1c2On2HrHK9kcUmUvaixHgHaFU?w=229&h=160&c=7&o=5&dpr=1.25&pid=1.7',
                                     'https://www.bing.com/th/id/OIP.QXWOYpRUHFWgumq2ZgxGEQHaEZ?w=240&h=160&c=7&o=5&dpr=1.25&pid=1.7',
                                     'https://www.bing.com/th/id/OIP.a4C-ePcNoOpaw4tuL6fqyQHaEo?w=223&h=177&c=7&o=5&dpr=1.25&pid=1.7',
                                    ]
__identify_person__(PERSON_GROUP_ID, FACES_IMAGE_PATH_TO_BE_IDENTIFIED, PERSON_NAME)

PERSON_NAME = 'QUEEN'  # just used to compare with the prediction
FACES_IMAGE_PATH_TO_BE_IDENTIFIED = ['https://www.bing.com/th/id/OIP.32GMUOROblyViQL__qoCxgHaKT?w=203&h=283&c=7&o=5&dpr=1.25&pid=1.7']
__identify_person__(PERSON_GROUP_ID, FACES_IMAGE_PATH_TO_BE_IDENTIFIED, PERSON_NAME)
