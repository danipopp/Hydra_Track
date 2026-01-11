import numpy as np

class RadarSensor:
    def __init__(self, noise_std=1.0):
        self.noise_std = noise_std

    def measure(self, true_position):
        noise = np.random.normal(0, self.noise_std, size=2)
        return true_position + noise
