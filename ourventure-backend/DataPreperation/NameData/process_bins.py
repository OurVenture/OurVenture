import json
import pprint


def add_region_bins(output_values):
    # Used to assign bin values to each key, the following comments are the output of the dict keys from main.py
    '''
    
    dict_keys(['scottish', 'welsh', 'indonesian', 'indian', 'belarusian', 'french', 'icelandic', 'latin', 'danish', 'occitan',
    'russian', 'estonian', 'hawaiian', 'bulgarian', 'catalan', 'manx', 'hungarian', 'portuguese', 'turkish', 'korean', 'serbian',
    'hebrew', 'persian', 'swedish', 'lithuanian', 'georgian', 'hindi', 'dutch', 'norwegian', 'slovak', 'norman', 'japanese', 'vietnamese',
    'czech', 'bosnian', 'greek', 'arabic', 'basque', 'finnish', 'german', 'romanian', 'tagalog', 'irish', 'breton', 'ukrainian', 'iranian',
    'polish', 'spanish', 'telugu', 'slavic', 'albanian', 'kazakh', 'montenegrin', 'bashkir', 'english', 'serbo-croatian', 'croatian', 'yoruba', 
    'latvian', 'azerbaijani', 'macedonian', 'italian', 'cebuano', 'armenian', 'slovene', 'galician']) 66
    
    '''
    # Region bins have a k, v[list] structure, the key is the region type and the v[list] is a list of values that are found in the k region
    # Some of these choices may be controversial, but any decisions that cause arguments are done purely to make  the data easier to work with, 
    # and for no ulterior reasons
    #TODO: implement regression test for if new values are found and added other than the 66 that exist here currently (as pf 06/02/22)
    region_bins = {"french": ["french", "norman", "breton", "occitan"], "iberian": ["spanish", "catalan", "basque", "portuguese", "galician"],
                "british": ["manx", "english", "welsh", "norman", "irish", "scottish"], "celtic": ["welsh", "breton", "irish", "scottish", "manx"],
                "italian": ["italian", "latin"], "benelux": ["dutch", "french", "norman", "german"], "german": ["german"], 
                "west-slavic": ["polish", "slovak", "czech", "romanian", "slavic", "serbian"], 
                "balkan": ["serbo-croatian", "montenegrin", "macedonian", "albanian", "bosnian", "bulgarian", "serbian", "croatian", "slovene"],
                "east-slavic": ["slavic", "ukranian", "belarsian", "russian"], "baltic": ["latvian", "lithuanian", "estonian"], 
                "uralic": ["finnish", "hungarian", "estonian"], "greek": ["greek"], "turkic": ["turkish", "persian", "bashkir", "kazakh"], "turkish": ["turkish"],
                "steppe": ["kazakh", "bashkir"], "scandinavian": ["danish", "icelandic", "manx", "danish", "finnish", "norweigan", "swedish", "estonian"],
                "ancient": ["greek", "latin"], "anatolia": ["greek", "turkish"], "caucasus": ["georgian", "armenian", "azerbaijani"], 
                "russian": ["russian", "belarusian", "kazakh", "ukrainian", "slavic", "bashkir", "georgian"], "east-asian": ["japanese", "korean"],
                "south-asia": ["indian", "hindi", "telugu", "persian"], 
                "south-east-asian": ["vietnamese", "tagalog", "cebuano", "indonesian"], "africa": ["yoruba"], 
                "middle-east": ["arabic", "persian", "iranian", "azerbaijani", "turkish"]}


    # Check the dict keys and the length of the dict keys, should be as long as the top comment
    print(output_values.keys(), len(output_values.keys()))
    # Loop over dict input, get the name of the origin and the list of dicts contained in origin dicts
    for name_type, origin_dicts in output_values.items():
        print("Name type is : " , name_type)
        print(type(origin_dicts))
        # assert (type(origin_dicts) == dict, "Input is dict")
        print("Starting internal loop")
        # Init variable that holds values
        region_bin_tags = []
        for k, v in region_bins.items():
            # Check if the origin is in the region bins, if it exists create list 
            if name_type in v:
                region_bin_tags.append(k)
        # Loop over list of dicts, add "region" key with found regions, useful for SQL/NoSQL operations in future
        for value in origin_dicts:
            value["region"] = region_bin_tags

    
    return output_values