import numpy as np

def create_and_save_npy(n, value, filename):
    array = np.full((n, 1), value)
    np.save(filename, array)
    print(f"Array with {n} elements, all set to {value}, saved to {filename}")

def append_to_npy_file(existing_filename, new_values):
    existing_array = np.load(existing_filename)
    new_values_array = np.array(new_values).reshape(-1, 1)
    updated_array = np.vstack((existing_array, new_values_array))
    np.save(existing_filename, updated_array)
    print(f"Appended {len(new_values)} values to {existing_filename}")

# Create the initial file
n = 92  # Number of elements
value = 1  # Value to set for each element
filename = 'y.npy'  # Filename to save the array

create_and_save_npy(n, value, filename)

# Append new values to the file
new_values = [0] * 270  # New values to append
append_to_npy_file(filename, new_values)
