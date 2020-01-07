import config.settings as conf
import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import json
import cv2
import numpy

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

    def detect_faces_in_image(self, face_image_path, is_url=True):
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

        print('Detecting faces in the {} image'.format(face_image_path))

        # Detect a face in an image that contains a single face
        single_image_name = os.path.basename(face_image_path)

        if(is_url):
            detected_faces = self.face_client.face.detect_with_url(url=face_image_path)
        else:
            detected_faces = self.face_client.face.detect_with_stream(image=open(face_image_path, 'rb'),
                                                                      return_face_id=True)

        if not detected_faces:
            raise Exception('No face detected from image {}'.format(single_image_name))

        # Display the detected face ID in the first single-face image.
        # Face IDs are used for comparison to faces (their IDs) detected in other images.
        print('Detected face ID from', single_image_name, ':')

        for face in detected_faces:
            print(face.face_id)

        # Save this ID for use in Find Similar
        first_image_face_ID = detected_faces[0].face_id
        print(first_image_face_ID)
