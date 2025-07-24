# animal-counter
a simple python program written for the jetson nano that counts the amount of animals in an image/camera, and warns you if it's more than 2

## Algorithm

This program takes in an input for image or camera (if image, it also expects the location to the image)

Then it either runs detectnet once on it, and checks the amount of valid animals inside of it, or it runs that code once per frame on the webcam input.
At the end of either step, it'll print the amount of animals it detected, and has a warning message if it's 2 or more.

## Running the project:
first, you need an installation of python 3
then, for it to run, you need jetson_inference and jetson_utils packages, which you can get by building [jetson inference](https://github.com/dusty-nv/jetson-inference) locally.

Additionally, the python script needs argparse to run properly, which you can simply install via `pip install argparse`

Now that you have the necessary packages, you can run it simply with either `python detect_animals.py camera` or `python detect_animals.py image [image_path]`
