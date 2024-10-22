class PDController:
    def __init__(self, kp, kd):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0.0

    def compute(self, error, dt) -> float:
        derivative = (error - self.previous_error) / dt
        # Calculate PD controller output using provided gains
        output = self.kp * error + self.kd * derivative
        # Update previous error for next iteration
        self.previous_error = error
        return output