import numpy as np

class CameraSensor:
    def __init__(self, noise_std=0.5, detection_prob=0.9):
        self.noise_std = noise_std
        self.detection_prob = detection_prob

    def measure(self, true_position):
        if np.random.rand() > self.detection_prob:
            return None
        noise = np.random.normal(0, self.noise_std, size=2)
        return true_position + noise
