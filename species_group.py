from species import Species

class SpeciesGroup:
    
    def __init__(self, group_name:str="", species:list=[]):
        """Initialise new species group with its name and Species."""
        self.group_name = group_name
        self.species = species

    @property
    def group_name (self):
        return self.__group_name

    @group_name.setter
    def group_name (self, group_name):
        if isinstance(group_name, str):
            self.__group_name = group_name.strip()
        else:
            raise TypeError("Group name must be of type str.")

    @property
    def species (self):
        return self.__species

    @species.setter
    def species (self, species:list):
        if isinstance(species, list):
            self.__species = species
        elif isinstance(species, str):
            self.__species = [species]
        else:
            raise TypeError("Species must be of type list or str.")