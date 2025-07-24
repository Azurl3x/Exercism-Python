"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):

    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    
    """
    grouped efficiency into 4 bands : 
    green -> efficiency of 80% or more,
    orange -> efficiency of less than 80% but at least 60%,
    red -> efficiency below 60%, but still 30% or more,
    black -> less than 30% efficient.

    Calculate the percentage value : 
    
    (generated_power/theoretical_max_power)*100 where generated_power = voltage * current."""

    generated_power = voltage * current

    if (generated_power/theoretical_max_power) * 100 >= 80: 
        say = 'green'
    elif (generated_power/theoretical_max_power) * 100 < 80 and (generated_power/theoretical_max_power) * 100 >= 60:
        say = 'orange'
    elif (generated_power/theoretical_max_power) * 100 < 60 and (generated_power/theoretical_max_power) * 100 >= 30:
        say = 'red'
    else:
        say = 'black'
    return say

def fail_safe(temperature, neutrons_produced_per_second, threshold):

    """
    Creating fail-safe mechanism to avoid overload and meltdown :
    This function determine if reactor is below, at or above the ideal criticality treshold.
    if its less than 90% = low
    if its 0-10% less or greater than treshold = normal
    if not any of aboves ranges = danger
    """

    if temperature * neutrons_produced_per_second < 0.9 * threshold:
        say = 'LOW'
    elif 0.9 * threshold <= temperature * neutrons_produced_per_second <= 1.1 * threshold:
        say = 'NORMAL'
    else: 
        say = 'DANGER'
    return say
