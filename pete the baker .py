def cakes(recipe, available):
    # Initialize a list to store the ratios of available ingredients to required amounts
    ratios = []
    
    # Check if each ingredient in the recipe is present in the available ingredients
    for ingredient in recipe:
        if ingredient not in available:
            return 0  # If any ingredient is missing, return 0
            
        # Calculate the ratio of available amount to required amount for each ingredient
        ratios.append(available[ingredient] // recipe[ingredient])
    
    # Return the minimum ratio, as that determines the maximum number of cakes that can be made
    return min(ratios)
