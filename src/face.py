import config.settings as conf
import os
import sys
import time
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType


class Face():
    '''
    Interact with Azure Face API:
        - Detect faces in an image
        - Find similar faces
        - Create and train a person group
        - Identify a face
        - Verify faces
    '''

    def __init__(self):
        '''
        Init class
        '''
        self.face_client = self.auth()

    def auth(self):
        '''
        Authenticate the client
        Instantiate a client with your endpoint and key.
        Create a CognitiveServicesCredentials object with your key
        and use it with your endpoint to create a FaceClient object.

        Returns
            FaceClient
        '''
        # Create an authenticated FaceClient.
        return FaceClient(conf.ENDPOINT,
                          CognitiveServicesCredentials(conf.KEY))

    def get_detected_face_in_image(self, face_image_path, is_url=True):
        '''
        Detects a face in a image (could be remote [URL] or local image).

        It prints the detected face's ID to the console and also stores it in program memory.

        Then, it detects the faces in an image with multiple people and prints their IDs to the console as well.

        Parameters
            face_image_path: string
                URL or path of the image
            is_url: boolean
                True/False indicating when to use remote images (URL)
        '''

        # print('Detecting faces in the {} image'.format(face_image_path))

        # Detect a face in an image that contains a single face
        single_image_name = os.path.basename(face_image_path)

        if(is_url):
            detected_faces = self.face_client.face.detect_with_url(url=face_image_path)
        else:
            detected_faces = self.face_client.face.detect_with_stream(image=open(face_image_path, 'rb'),
                                                                      return_face_id=True)

        if not detected_faces:
            print('No face detected from image {}'.format(single_image_name))
            return None

        # Save this ID for use in Find Similar
        return detected_faces[0].face_id

    def create_person_group(self, person_group_id):
        '''
        Create person group to a specific person

        Returns
            message: string
            Indicate when the group was created or already existed
        '''
        try:
            self.face_client.person_group.create(person_group_id=person_group_id,
                                                 name=person_group_id)
            print('Person group {} was created'.format(person_group_id))
        except Exception as e:
            print(e)

    def add_person_group_level(self, person_group_id, name):
        '''
        Add a person group level to an existing person_group_id
        Example: person_group_id = people, name=Woman
        person_group_id = people, name=Man
        person_group_id = people, name=Child

        Returns
            message: string
            Indicate when the group was created or already existed
        '''
        return self.face_client.person_group_person.create(person_group_id, name).person_id

    def assign_person_image_to_person_group(self, person_group_id, person_id, face_image_path):
        '''
        Assign a person's image to a person group
        '''
        try:
            self.face_client.person_group_person.add_face_from_stream(person_group_id,
                                                                      person_id,
                                                                      open(face_image_path, 'rb'))
        except Exception as e:
            print('Error {} in the image file {}'.format(e, face_image_path))

    def train_person_group(self, person_group_id):
        '''
        Train PersonGroup
        '''

        print()
        print('Training the person group...')

        # Train the person group
        self.face_client.person_group.train(person_group_id)

        while (True):
            training_status = self.face_client.person_group.get_training_status(person_group_id)
            print("Training status: {}.".format(training_status.status))
            print()

            if (training_status.status is TrainingStatusType.succeeded):
                break
            elif (training_status.status is TrainingStatusType.failed):
                sys.exit('Training the person group has failed.')
            time.sleep(5)

    def identify_face(self, person_group_id, face_image_path, is_url=True):
        '''
        Given a face_id and person_group_id try to identify the person associated with the face_id
        '''
        face_id = []
        results = {}

        if(self.get_detected_face_in_image(face_image_path, is_url)):
            face_id.append(self.get_detected_face_in_image(face_image_path, is_url))
            # Identify faces
            results = self.face_client.face.identify(face_id, person_group_id)

        print(results)

        # print('Identifying faces in {}'.format(os.path.basename(image.name)))
        if not results or not results[0].candidates:
            print('Person in the image file {} '
                  'was not found'.format(face_image_path))
        else:
            print('Person for face ID {} '
                  'in the image file {} '
                  'is identified to the person "{}" '
                  'with a confidence of {}.'.format(face_id[0],
                                                    face_image_path,
                                                    self.face_client.person_group_person.get(person_group_id,
                                                                                             results[0].candidates[0].person_id).name,
                                                    results[0].candidates[0].confidence))

    def delete_person_group(self, person_group_id):
        '''
        Delete a person group
        '''
        try:
            # Delete the main person group.
            self.face_client.person_group.delete(person_group_id=person_group_id)
            print("Deleted the person group ""{}"" from the source location.".format(person_group_id))
            print()
        except Exception as e:
            print("Error {} when try to delete the person_group_id {}".format(e, person_group_id))
