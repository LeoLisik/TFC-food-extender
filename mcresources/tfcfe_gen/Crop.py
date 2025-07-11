from mcresources import ResourceManager
from tfcfe_gen.Utils import *


class Crop:
    def __init__(self, rm: ResourceManager, name: str, mod_id: str, age: int = 6):
        self.rm = rm
        self.name = name
        self.mod_id = mod_id
        self.age = age

    def generate_default_crop(self):
        self.rm.blockstate("crop/" + self.name, variants={
            f'age={i}': {'model': f'{self.mod_id}:block/crop/{self.name}_age_{i}'} for i in range(self.age)
        })
        for i in range(self.age):
            self.rm.block_model(f'crop/{self.name}_age_{i}',
                                parent='block/crop',
                                textures={
                                    'crop': f'{self.mod_id}:block/crop/{self.name}_{i}'
                                })
            generate_png(f'/assets/{self.mod_id}/textures/block/crop', f'{self.name}_{i}')
        self.rm.lang({
            f"block.{self.mod_id}.crop.{self.name}": f"{' '.join(word.capitalize() for word in self.name.split('_'))}"
        })
        return self

    def generate_dead_crop(self):
        self.rm.blockstate("dead_crop/" + self.name, variants={
            'mature=true': {'model': f'{self.mod_id}:block/dead_crop/{self.name}'},
            'mature=false': {'model': f'{self.mod_id}:block/dead_crop/{self.name}_young'}
        })
        self.rm.block_model(f'dead_crop/{self.name}', parent='block/crop', textures={
            'crop': f'{self.mod_id}:block/crop/{self.name}_dead'
        })
        generate_png(f'/assets/{self.mod_id}/textures/block/crop', f'{self.name}_dead')
        self.rm.block_model(f'dead_crop/{self.name}_young', parent='block/crop', textures={
            'crop': f'{self.mod_id}:block/crop/{self.name}_dead_young'
        })
        generate_png(f'/assets/{self.mod_id}/textures/block/crop', f'{self.name}_dead_young')
        self.rm.lang({
            f"block.{self.mod_id}.dead_crop.{self.name}": f"Dead {' '.join(word.capitalize() for word in self.name.split('_'))}"
        })
        return self

    def generate_wild_crop(self):
        self.rm.blockstate("wild_crop/" + self.name, variants={
            'mature=true': {'model': f'{self.mod_id}:block/wild_crop/{self.name}'},
            'mature=false': {'model': f'{self.mod_id}:block/dead_crop/{self.name}'}
        })
        self.rm.block_model(f'wild_crop/{self.name}', parent=f'{self.mod_id}:block/wild_crop/crop', textures={
            'crop': f'{self.mod_id}:block/crop/{self.name}_wild'
        })
        generate_png(f'/assets/{self.mod_id}/textures/block/crop', f'{self.name}_wild')
        self.rm.item_model(f'wild_crop/{self.name}', parent=f'{self.mod_id}:block/wild_crop/{self.name}', no_textures=True)
        self.rm.lang({
            f"block.{self.mod_id}.wild_crop.{self.name}": f"Wild {' '.join(word.capitalize() for word in self.name.split('_'))}"
        })
        return self

    def generate_seed_item(self):
        self.rm.item_model(f'seeds/{self.name}', parent='item/generated', *{
            f'{self.mod_id}:item/seeds/{self.name}'
        })
        generate_png(f'/assets/{self.mod_id}/textures/item/seeds', f'{self.name}')
        self.rm.lang({
            f"item.{self.mod_id}.seeds.{self.name}": f"{' '.join(word.capitalize() for word in self.name.split('_'))} Seeds"
        })
        return self

    def generate_food_item(self, name: str = None,
                           hunger: int = 4, saturation: int = 0, decay_modifier: int = 2):
        if name is None:
            name = self.name
        self.rm.item_model(f'food/{name}', parent='item/generated', *{
            f'{self.mod_id}:item/food/{name}'
        })
        generate_png(f'/assets/{self.mod_id}/textures/item/food', f'{name}')
        self.rm.data((f'tfc/food_items', name), {
            "ingredient": {
                "item": f"{self.mod_id}:food/{name}"
            },
            "hunger": hunger,
            "saturation": saturation,
            "decay_modifier": decay_modifier
        })
        self.rm.lang({
            f"item.{self.mod_id}.food.{name}": ' '.join(word.capitalize() for word in name.split('_'))
        })
        return self

    def generate_loot_table(self, drop_path: str = None):
        if drop_path is None:
            drop_path = f'{self.mod_id}:food/{self.name}'
        self.rm.block_loot(f'crop/{self.name}', {
            "rolls": 1,
            "entries": [
                {
                    "type": "minecraft:item",
                    "name": f"{drop_path}",
                    "conditions": [
                        {
                            "condition": "minecraft:block_state_property",
                            "block": f"{self.mod_id}:crop/{self.name}",
                            "properties": {
                                "age": f"{self.age - 1}"
                            }
                        }
                    ],
                    "functions": [
                        {
                            "function": "minecraft:set_count",
                            "count": {
                                "type": "tfc:crop_yield_uniform",
                                "min": 0,
                                "max": {
                                    "type": "minecraft:uniform",
                                    "min": 6,
                                    "max": 10
                                }
                            }
                        }
                    ]
                }
            ],
            "conditions": [
                {
                    "condition": "minecraft:survives_explosion"
                }
            ]
        },
                      {
                          "rolls": 1,
                          "entries": [
                              {
                                  "type": "minecraft:item",
                                  "name": f"{self.mod_id}:seeds/{self.name}"
                              }
                          ],
                          "conditions": [
                              {
                                  "condition": "minecraft:survives_explosion"
                              }
                          ]
                      })
        return self

    def generate_climate_range(self,
                               min_hydration: int = 25, max_hydration: int = 100,
                               hydration_wiggle_range: int = 0,
                               min_temperature: int = -4, max_temperature: int = 35,
                               temperature_wiggle_range: int = 5):
        self.rm.data((f'tfc/climate_ranges/crop', self.name), {
            "min_hydration": min_hydration,
            "max_hydration": max_hydration,
            "hydration_wiggle_range": hydration_wiggle_range,
            "min_temperature": min_temperature,
            "max_temperature": max_temperature,
            "temperature_wiggle_range": temperature_wiggle_range
        })
        return self

    # TODO: Vanilla craft
    def generate_seed_craft(self, ingredients, result_count=1, shaped=True, pattern=None, group=None, conditions=None):
        generate_vanilla_craft(self.rm, self.mod_id, "seeds", self.name, ingredients, result_count, shaped, pattern, group, conditions)
        return self

    def generate_bloodmagic_altar_seed_craft(self, input_item, syphon, consumption_rate, drain_rate, upgrade_level):
        generate_bloodmagic_altar_craft(self.rm, self.name, input_item, {"item": f"{self.mod_id}:seeds/{self.name}"}, syphon, consumption_rate, drain_rate, upgrade_level)
        return self
