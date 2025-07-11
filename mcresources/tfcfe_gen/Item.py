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
        if shaped:
            if pattern is None:
                raise ValueError("Shaped recipe requires a pattern")
            recipe = {
                "type": "minecraft:crafting_shaped",
                "pattern": pattern,
                "key": {},
                "result": {
                    "item": f"{self.mod_id}:{self.path}/{self.name}",
                    "count": result_count
                }
            }
            for key, ingredient in ingredients.items():
                recipe["key"][key] = (
                    {"tag": ingredient[1:]} if ingredient.startswith("#") else {"item": ingredient}
                )

        if not shaped:
            recipe = {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [],
                "result": {
                    "item": f"{self.mod_id}:{self.path}/{self.name}",
                    "count": result_count
                }
            }
            for ingredient in ingredients:
                recipe["ingredients"].append(
                    {"tag": ingredient[1:]} if ingredient.startswith("#") else {"item": ingredient}
                )

        if group:
            recipe["group"] = group

        self.rm.data(f'recipes/{self.path}/{self.name}.json', data_in=recipe)
        return self

