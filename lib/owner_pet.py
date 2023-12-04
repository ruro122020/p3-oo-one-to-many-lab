
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = list()

    def __init__(self, name, pet_type, owner=None):
        self.owner = owner
        self.name = name
        self.pet_type = pet_type
        Pet.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception 
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
       

    def pets(self):
        pets = []
        for pet in Pet.all:
            if pet.owner == self:
                pets.append(pet)
        return pets
        
    def add_pet(self, pet):
        if not (isinstance(pet, Pet)) or not pet:
            raise Exception("Object is not of type Pet")
        else:
            pet.owner = self
            
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
