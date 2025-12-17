def initialize_array(size, value=0.0):
    return [value] * size

def time_step(current_time, dt):
    return current_time + dt

def validate_parameters(param_dict):
    for key, value in param_dict.items():
        if value is None or (isinstance(value, (int, float)) and value < 0):
            raise ValueError(f"Invalid parameter: {key} must be a non-negative value.")