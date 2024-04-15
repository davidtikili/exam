import math

# calculate the error
def calculate_error(set_point, measured_temp):
    return set_point - measured_temp

# calculate the incremental heating control signal (∆𝒖)
def calculate_delta_u(Kp, Ki, Kd, error1, error2, error3):
    delta_u = Kp * (error1 - error2) + (Ki * error1)  + Kd * (error1 - 2 * (error2) + error3)
    return delta_u

# calculate the heating control signal 𝒖 at each time step
def calculate_control_signal(prev_control_signal, delta_u):
    control_signal = prev_control_signal + delta_u
    return control_signal

# simulate the temperature system
def simulate_temperature(tau, zeta, t):
    # temp = 100 * (1 - math.exp(-zeta * t / tau) * (math.cos(math.sqrt(1 - zeta**2) / tau * t) + zeta / math.sqrt(1 - zeta**2) * math.sin(math.sqrt(1 - zeta**2) / tau * t)))
    temp =  100 * (1 - ((math.exp((-zeta * t)/tau))*((math.cos(((math.sqrt(1-zeta**2))/tau)*t))+ ((zeta/(math.sqrt(1-zeta**2)))*(math.sin(((math.sqrt(1-zeta**2))/tau)*t))))))
    return temp

# Main function to find the heating control signal 𝒖 for the specified time range
def main():
    # Constants
    Kp = 8
    Ki = 5
    Kd = 1.6
    tau = 5
    zeta = 0.55
    set_point = 100
    
    # Initial conditions
    measured_temp = 81.5
   
    prev_control_signal = 800
    
    # Simulation
    print("Time(Sec) Meas.Temp(°C)  Error    ∆𝒖       𝒖")
    for t in range(41):
        measured_temp = simulate_temperature(tau, zeta, t)
        sec_temp = simulate_temperature(tau,zeta, t-1)
        third_temp = simulate_temperature(tau, zeta, t-2)
        error1 = calculate_error(set_point, measured_temp)
        error2 = calculate_error(set_point, sec_temp)
        error3 = calculate_error(set_point, third_temp)
        delta_u = calculate_delta_u(Kp, Ki, Kd, error1, error2, error3)
        control_signal = calculate_control_signal(prev_control_signal, delta_u)
        
        print(f"{t:8d}\t{measured_temp:.2f}\t{error1:.2f}\t{delta_u:.2f}\t{control_signal:.2f}")
        
        # Update previous error and control signal for next iteration
        
        prev_control_signal = control_signal

# Run the simulation
main()

