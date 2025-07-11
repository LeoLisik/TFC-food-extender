from mcresources import ResourceManager
from tfcfe_gen.Utils import *


class Item:
    def __init__(self, rm: ResourceManager, path: str, name: str, mod_id: str):
        self.rm = rm
        self.path = path
        self.name = name
        self.mod_id = mod_id

    def generate_base(self):
        full_name = self.path + "/" + self.name
        self.rm.item_model(full_name, {'layer0': f'{self.mod_id}:item/{full_name}'}, parent='item/generated')
        generate_png(f'/assets/{self.mod_id}/textures/item/{self.path}', f'{self.name}')
        self.rm.lang({
            f"item.{self.mod_id}.{self.path}.{self.name}": f"{' '.join(word.capitalize() for word in self.name.split('_')) + ' ' + ' '.join(word.capitalize() for word in self.path.split(('_')))}"
        })
        return self

    def generate_vanilla_craft(self, ingredients, result_count=1, shaped=True, pattern=None, group=None):
        generate_vanilla_craft(self.rm, self.mod_id, self.path, self.name, ingredients, result_count, shaped, pattern, group)
        return self

