import os
from mcresources import ResourceManager


def generate_png(path, file, resource_dir='src/main/resources'):
    dir = resource_dir + path
    os.makedirs(dir, exist_ok=True)
    open(f'{dir}/{file}.png', 'a+')


def generate_vanilla_craft(rm: ResourceManager, mod_id, path, name, ingredients, result_count=1, shaped=True, pattern=None, group=None):
    if shaped:
        if pattern is None:
            raise ValueError("Shaped recipe requires a pattern")
        recipe = {
            "type": "minecraft:crafting_shaped",
            "pattern": pattern,
            "key": {},
            "result": {
                "item": f"{mod_id}:{path}/{name}",
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
                "item": f"{mod_id}:{path}/{name}",
                "count": result_count
            }
        }
        for ingredient in ingredients:
            recipe["ingredients"].append(
                {"tag": ingredient[1:]} if ingredient.startswith("#") else {"item": ingredient}
            )

    if group:
        recipe["group"] = group

    rm.data(f'recipes/{path}/{name}', data_in=recipe)


def generate_bloodmagic_altar_craft(
    rm: ResourceManager,
    name: str,
    input_item: dict,
    output_item: dict,
    syphon: int,
    consumption_rate: int,
    drain_rate: int,
    upgrade_level: int = 0,
    conditions: list = None
):
    recipe = {
        "altarSyphon": syphon,
        "consumptionRate": consumption_rate,
        "drainRate": drain_rate,
        "input": input_item,
        "output": output_item,
        "upgradeLevel": upgrade_level
    }

    if conditions:
        recipe["conditions"] = conditions

    rm.recipe("../../bloodmagic/recipes/altar/" + name, "bloodmagic:altar", recipe)
