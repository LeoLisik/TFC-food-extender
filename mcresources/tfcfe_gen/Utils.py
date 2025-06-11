import os


def generate_png(path, file, resource_dir='src/main/resources'):
    dir = resource_dir + path
    os.makedirs(dir, exist_ok=True)
    open(f'{dir}/{file}.png', 'a+')
