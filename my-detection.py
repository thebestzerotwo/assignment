#from jetson_inference import detectNet
from jetson_utils import loadImage, saveImage
import jetson_inference
import jetson_utils

net = jetson_inference.detectNet(model="ssd-mobilenet-v2", threshold=0.5)
img = loadImage("/home/nvidia/jetson-inference/data/images/fruit_14.jpg")
detections = net.Detect(img)
print(f"total targets: {len(detections)}")
for det in detections:
    print("-- ClassID:", det.ClassID)
    print("-- Confidence:", det.Confidence)
    print("-- Left:", det.Left)
    print("-- Top:", det.Top)
    print("-- Right:", det.Right)
    print("-- Bottom:", det.Bottom)
    print("-- Width:", det.Width)
    print("-- Height:", det.Height)
    print("-- Area:", det.Area)
    print(f"-- Center: ({det.Center[0]:.3f},{det.Center[1]:.3f})")
saveImage("/home/nvidia/Desktop/output_1.jpg",img)

img = loadImage("/home/nvidia/jetson-inference/data/images/fruit_5.jpg")
detections = net.Detect(img)
print(f"total targets: {len(detections)}")
for det in detections:
    print("-- ClassID:", det.ClassID)
    print("-- Confidence:", det.Confidence)
    print("-- Left:", det.Left)
    print("-- Top:", det.Top)
    print("-- Right:", det.Right)
    print("-- Bottom:", det.Bottom)
    print("-- Width:", det.Width)
    print("-- Height:", det.Height)
    print("-- Area:", det.Area)
    print(f"-- Center: ({det.Center[0]:.3f},{det.Center[1]:.3f})")
saveImage("/home/nvidia/Desktop/output_2.jpg",img)
