import numpy as np
from sensors.radar import RadarSensor
from sensors.camera import CameraSensor

def main():
    radar = RadarSensor()
    camera = CameraSensor()

    true_position = np.array([0.0, 0.0])
    velocity = np.array([1.0, 0.5])

    for t in range(10):
        true_position += velocity

        radar_meas = radar.measure(true_position)
        camera_meas = camera.measure(true_position)

        print(f"Time {t}")
        print(f"  True position: {true_position}")
        print(f"  Radar: {radar_meas}")
        print(f"  Camera: {camera_meas}")

if __name__ == "__main__":
    main()
