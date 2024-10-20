class PDController:
    def __init__(self, kp, kd):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0.0

    def compute(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        derivative = (error - self.previous_error) / dt
        output = self.kp * error + self.kd * derivative
        self.previous_error = error
        return output