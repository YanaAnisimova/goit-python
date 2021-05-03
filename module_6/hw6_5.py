def get_ingredients(path, position_name):
    
    with open(path, 'r') as file:
        for line in file:
            if line.startswith(position_name+':'):
                ingredients = line.removeprefix(position_name+':')
                
                return ingredients.split(',')