# Import the packages for picam
from picam import PICam
from picam.picam_types import PicamReadoutControlMode
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Initialize the picam object
cam = PICam()

# Loading the library
cam.loadLibrary()

try:
    # Initialize to a DemoCamera
    cam.getAvailableCameras(demo = True)

    # Connect to DemoCamera
    cam.connect(camID=None)

    # Print parameters
    # cam.printAvailableParameters()

    # Set parameters
    # PicamReadoutControlMode converts option name into correct numerical value
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