import csv

def Future_irreg(verb):
    """Creates dictionary with irregular verbs from a csv file, checks if 
    the given verb is in the dictionary. If it is, the stem is returned
    from the dictionary. If the verb is not irregular, the verb is returned
    unchanged. 
    
    Returns:
        stem = stem of irregular verb to be used instead of verb
        verb = unchanged verb"""

    with open("Spanish\Future_indicative\Future_indicative_irregular.csv", "rt") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        irreg_dict = {rows[0]: [rows[1]] for rows in csv_reader}

    ### if verb is in irregular dictionary
    if verb in irreg_dict:
        ### use verb as key to get the stem
        stem = irreg_dict.get(verb)
        ### remove brackets
        stem = ''.join(stem)
        return stem

    else:
    ### if verb is not in irregular dictionary
        return verb
