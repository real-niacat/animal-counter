import argparse
import jetson_utils
import jetson_inference
# written by human(s?)
# for humans

parser = argparse.ArgumentParser(description="Takes an image or webcam input and detects if there are multiple animals in it.",
                                 usage="Usage: python detect_animals.py [camera|image <image_path>]")

parser.add_argument("inputtype", type=str, default="", nargs="?", help="Webcam or from image file")
parser.add_argument("input", type=str, default="", nargs="?", help="Input destination")


inp = None
setting = None
pka = parser.parse_known_args()[0]
inp = pka.input
setting = pka.inputtype
animals = ["person", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe"]
# these are all of the valid animals in the detectnet labels
# yes. people are animals
if setting == "image" or setting == "camera":
    detect = jetson_inference.detectNet(model="ssd-mobilenet-v2",threshold=0.5)
    #to be fully honest with you it isn't so good at detecting images all the time, but i can't really make the model better on its own
if setting == "image":
    print("Running on " + inp)
    
    
    image = jetson_utils.loadImage(inp)
    
    print("DetectNet loaded!")
    print("Detecting from image...")
    io = detect.Detect(image)
    animalcount = 0
    for i in io:
        desc = detect.GetClassDesc(i.ClassID) #it says desc but it's really just the name
        if desc in animals:
            print(f"found: {animalcount+1}") #i may be stupid
            #BUT
            # i have nothing else to say
            animalcount += 1
        
    if animalcount > 1:
        print(f"There are {animalcount} animals in this image, which is too many.")
elif setting == "camera":
    
    camera = jetson_utils.videoSource("/dev/video0")
    video = jetson_utils.videoOutput("file://detection.mp4")
    while True:
        frame = camera.Capture()
        found = detect.Detect(frame)
        video.Render(frame)

        animalcount = 0
        for i in found:
            desc = detect.GetClassDesc(i.ClassID)
            if desc in animals:
                animalcount += 1
            
        if animalcount > 1:
            print(f"Detected {animalcount} animals, !!!!!!!!")
        else:
            print(f"Detected {animalcount} animals, you're fine.")

        video.SetStatus(f"{animalcount} animals found!")
    
else:
    print("Unrecognized input. Please try again")
    print(parser.usage)