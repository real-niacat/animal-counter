# animal-counter
a simple python program written for the jetson nano that counts the amount of animals in an image/camera, and warns you if it's more than 2

# how to run:
first, you need an installation of python 3
then, for it to run, you need jetson_inference and jetson_utils packages, which you can get by building [jetson inference](https://github.com/dusty-nv/jetson-inference) locally
additionally, it needs argparse to run, which you can simply install via `pip install argparse`

Now that you have the necessary packages, you can run it simply with either `python detect_animals.py camera` or `python detect_animals.py image [image_path]`
Reading the console, you will see the amount of animals counted by the program, and it will have an alternate alert message if there are 2 or more
