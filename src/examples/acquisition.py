# Import the packages for picam
from picam import PICam
from picam.picam_types import PicamReadoutControlMode, PicamAdcQuality, PicamAdcAnalogGain, PicamTriggerDetermination
from picam.picam_types import PicamTriggerResponse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import time

# Initialize the picam object
cam = PICam()

# Loading the library
cam.loadLibrary()

try:
    # Initialize to a DemoCamera
    cam.getAvailableCameras()

    # Connect to DemoCamera
    cam.connect(camID=None)

    # Print parameters
    # cam.printAvailableParameters()

    # Set camera temperature
    cam.setParameter("SensorTemperatureSetPoint", -70)
    print(f"Camera temperature: {cam.getParameter('SensorTemperatureReading'):.1f} C")

    # Set parameters
    cam.setParameter("ExposureTime", 10) # Exposure time in ms
    cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])

    # ADC parameters
    cam.setParameter("AdcQuality", PicamAdcQuality["ElectronMultiplied"])
    cam.setParameter("AdcAnalogGain", PicamAdcAnalogGain["Low"])
    cam.setParameter("AdcEMGain", 1)

    # sensor cleaning
    cam.setParameter("CleanSectionFinalHeightCount", 1)
    cam.setParameter("CleanSectionFinalHeight", 100)
    cam.setParameter("CleanSerialRegister", False)
    cam.setParameter("CleanCycleCount", 1)
    cam.setParameter("CleanCycleHeight", 100)
    cam.setParameter("CleanUntilTrigger", True)

    # Set trigger
    cam.setParameter("TriggerDetermination", PicamTriggerDetermination["RisingEdge"])
    cam.setParameter("TriggerResponse", PicamTriggerResponse["ReadoutPerTrigger"])

    # Apply settings
    cam.sendConfiguration()

    # get readout speed
    print("Estimated readout time = %f ms" % cam.getParameter("ReadoutTimeCalculation"))

    # Loop to read out camera many times and animate the plot
    # Read out one frame
    data = cam.readNFrames(N = 1, timeout = 100000)[0][0]

    # Define figure and axes
    fig, ax = plt.subplots()
    # Define region of interest
    x0 = 100
    x1 = 400
    y0 = 200
    y1 = 300
    ax.add_patch(Rectangle((x0,y0), x1-x0, y1-y0, fill = False, ec = 'r'))
    im = ax.imshow(data)

    # Loop to see many framse
    N_read = 10
    for i in range(N_read):
        # Read out one frame
        data = cam.readNFrames(N = 1, timeout = 100000)[0][0]

        # print(f"Shape of data: {data.shape}")

        # Plot the array
        im.set_data(data)

        plt.draw()
        plt.pause(0.010)


# Unload library
finally:
    cam.disconnect()
    cam.unloadLibrary()