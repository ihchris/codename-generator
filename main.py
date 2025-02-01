import random
from words_list import attributes, objects


# Generator function
def generate_codename(attributes, objects, add_number=False):
    # Randomly pick one attribute and one object
    attribute = random.choice(attributes).upper()
    obj = random.choice(objects).upper()
    
    # Combine them into a phrase
    codename = f"{attribute} {obj}"
    
    # Add a number if requested (e.g., "THREATENING INSPECTOR-42")
    if add_number:
        codename += f"-{random.randint(0, 99):02d}"
    
    return codename

# Example usage
if __name__ == "__main__":
    num_names = int(input("How many code names do you want to generate? "))
    # use_numbers = input("Add random numbers? (y/n): ").strip().lower() == 'y'
    
    print("\nGenerated Code Names:\n")
    for _ in range(num_names):
        # print(generate_codename(attributes, objects, add_number=use_numbers))
        print(generate_codename(attributes, objects))