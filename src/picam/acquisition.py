# Import the packages for picam
from picam import *
from picam_types import *
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Initialize the picam object
cam = picam()

# Loading the library
cam.loadLibrary()

try:
    # Initialize to a DemoCamera
    cam.getAvailableCameras()

    # Connect to DemoCamera
    cam.connect(camID=None)

    # Print parameters
    # cam.printAvailableParameters()

    # Set parameters
    cam.setParameter("ExposureTime", 10) # Exposure time in ms
    cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])

    # Apply settings
    cam.sendConfiguration()

    # Read out one frame
    data = cam.readNFrames()[0]

    print(f"Shape of data: {data.shape}")

    # Define region of interest
    x0 = 100
    x1 = 400
    y0 = 200
    y1 = 300

    # Plot the array
    fig, ax = plt.subplots()
    ax.imshow(data[0,:,:])

    # Show region of intereset on plot
    ax.add_patch(Rectangle((x0,y0), x1-x0, y1-y0, fill = False, ec = 'r'))

    plt.show()


# Unload library
finally:
    cam.unloadLibrary()