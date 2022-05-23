import importlib
import pkgutil


def load_plugins():
    plugins = {
        name: importlib.import_module('plugin.'+ name)
        for _, name, _ in pkgutil.iter_modules(['plugin']) if name.startswith('scratch_plugin')
    }
    return plugins


def print_modules():
    for finder, name, ispkg in pkgutil.iter_modules():
        print(name)


if __name__ == '__main__':
    p = load_plugins()
    for k, v in p.items():
        print(f'{k} = {v.register()}')



