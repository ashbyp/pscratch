import os
from functools import partial
from . import misc

PYTHON_PROJECT_SKIP_DIRS = {'__pycache__', 'venv', '.idea', '.git'}


def apply_from(dir_fn, file_fn, root='.', skip_dirs=None):
    skip_dirs = set(skip_dirs) if skip_dirs else {}
    results = []
    for dir_name, subdir_list, file_list in os.walk(root):
        result = dir_fn(dir_name)
        if result:
            results.append(result)
        for file_name in file_list:
            result = file_fn(dir_name, file_name)
            if result:
                results.append(result)
        _do_skip_dirs(subdir_list, skip_dirs)
    return results or None


list_from = partial(apply_from,
                    lambda d: print('Found directory %s' % d),
                    lambda d, f: print('\t%s' % f))

list_dirs_from = partial(apply_from,
                         lambda d: print('Found directory %s' % d),
                         lambda d, f: None)

list_paths_from = partial(apply_from,
                          lambda d: print('Found directory %s' % d),
                          lambda d, f: print('\t%s' % os.path.join(d, f)))

list_from_with_sizes = partial(apply_from,
                               lambda d: print('Found directory %s : %s' % (d, misc.get_size(d))),
                               lambda d, f: print('\t%s : %s' % (f, misc.get_size(os.path.join(d, f)))))

get_files_from_with_sizes = partial(apply_from,
                                    lambda d: None,
                                    lambda d, f: (os.path.join(d, f), misc.get_size(os.path.join(d, f))))

get_dirs_from_with_sizes = partial(apply_from,
                                   lambda d: (d, misc.get_size(d)),
                                   lambda d, f: None)


def get_largest_files(root='.', skip_dirs=None, how_many=10):
    results = sorted(get_files_from_with_sizes(root=root, skip_dirs=skip_dirs),
                     reverse=True, key=lambda x: x[1])[:how_many]
    return results or []


def get_largest_dirs(root='.', skip_dirs=None, how_many=10):
    results = sorted(get_dirs_from_with_sizes(root=root, skip_dirs=skip_dirs),
                     reverse=True, key=lambda x: x[1])[:how_many]
    return results or []


def _do_skip_dirs(sub_dirs, skip_dirs):
    if skip_dirs and sub_dirs:
        x = 0
        while x < len(sub_dirs):
            if sub_dirs[x] in skip_dirs:
                del sub_dirs[x]
            else:
                x += 1
