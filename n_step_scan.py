# Dominique Kellam
# CSC 400
# Project: N-Step Scan
# November 21, 2023

import random

def generate_requests(num_requests, max_track):
    return [random.randint(0, max_track) for _ in range(num_requests)]

def n_step_look(requests, n):
    total_movement = 0
    current_position = 0
    direction = 1  # Start moving towards higher block numbers
    processed_groups = []

    for i in range(0, len(requests), n):
        # Create a group of up to N requests
        group = requests[i:i+n]

        # Sort group based on current direction
        group.sort(reverse=direction < 0)

        # Process the group
        for request in group:
            total_movement += abs(current_position - request)
            current_position = request

        processed_groups.append((group, 'High to Low' if direction < 0 else 'Low to High'))
        direction *= -1  # Change direction

    return processed_groups, total_movement

def main():
    num_requests = 1000
    max_track = 199
    requests = generate_requests(num_requests, max_track)
    
    # Print the generated disk requests
    print("Generated Disk Requests:")
    print(requests)

    n = int(input("\nEnter the value of N: "))

    processed_groups, total_movement = n_step_look(requests, n)
    for i, (group, direction) in enumerate(processed_groups):
        print(f"Group {i+1}: {group}, Direction: {direction}")
    print("\nTotal tracks traversed:", total_movement)

if __name__ == "__main__":
    main()