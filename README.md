# Face detection using Azure Cognitive Services **(Face API)**
This implementation is for learning purposes. The class face.py could be used to train Cognitive models using Face API.
Could be used in scenarios like person identification, fraud detection, and much more.
Use your creativity to expand the use ~~to have fun~~ to fix a lot of real world problems and feel free to clone this repo and adapt this code for your requirements :)

## [Activate environment](https://pipenv.readthedocs.io/en/latest/)
`pipenv shell`

## Flake8 config
Use the bellow code to adjust the max line length limit
flake8 --max-line-length=140

If you use VSCode you can add this config to settings.json adding the code:

```
"python.linting.flake8Args": [
        "--max-line-length=140",
    ]
```

## Set environment variables
### You can find API Key in Quick start section of your API on Azure Portal
`export FACE_SUBSCRIPTION_KEY=<KEY_1>`
### You can find API endpoint in Quick start section of your API on Azure Portal
`export FACE_ENDPOINT=<FACE_ENDPOINT>`


## How to train the model
Run `run_train.py` and change the variables `PERSON_GROUP_ID` and
the parameters `person_name` and `faces_image_path` for the method `__assign_person_image_to_person_group__`

**PERSON_GROUP_ID**: is the name for the person group to be created (eg. People, Animals, etc)

**person_name** is: the name of the person (Eg. Barack Obama)

**faces_image_path**: is the path of the images to be used for training (Eg. obama_1.jpg, obama_2.jpg). You should download all the images associated
with the person and put all of them inside the folder used in the path

## How to identify a person associated with an image
Run `run_identify.py` and change `PERSON_GROUP_ID` and `FACES_IMAGE_PATH_TO_BE_IDENTIFIED`. It is important to use a PERSON_GROUP_ID
that was already trained before (see **[How to train the model](https://github.com/lfbraz/face-detection-tutorial#how-to-train-the-model)** section).

**PERSON_GROUP_ID**: is the name for the person group already used for the training stage
**FACES_IMAGE_PATH_TO_BE_IDENTIFIED**: is the path of the images to be identified. You can also use the `is_url` flag
of the method `identity_face` to be able to identify images directly from the web.

## Clean up resources
To clean up resources you can delete the Resource Group or the API using Azure Portal.
If you don't want to lose the resources you can also run the file `run_cleanup.py`
this method only delete the `person_group_id`.
