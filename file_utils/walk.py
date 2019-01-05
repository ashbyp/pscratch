import os
from functools import partial

PYTHON_PROJECT_SKIP_DIRS = {'__pycache__', 'venv', '.idea', '.git'}


def apply_from(dir_fn, file_fn, root='.', skip_dirs=None):
    if skip_dirs is None:
        skip_dirs = {}
    file_results = []
    dir_results = []
    for dir_name, subdir_list, file_list in os.walk(root):
        result = dir_fn(dir_name)
        if result:
            dir_results.append(result)
        for file_name in file_list:
            result = file_fn(dir_name, file_name)
            if result:
                file_results.append(result)
        _do_skip_dirs(subdir_list, skip_dirs)
    if dir_results and file_results:
        return dir_results, file_results
    elif dir_results:
        return dir_results
    elif file_results:
        return file_results
    else:
        return None


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
                               lambda d: print('Found directory %s : %s' % (d, os.path.getsize(d))),
                               lambda d, f: print('\t%s : %s' % (f, os.path.getsize(os.path.join(d, f)))))

get_files_from_with_sizes = partial(apply_from,
                                    lambda d: None,
                                    lambda d, f: (f, os.path.getsize(os.path.join(d, f))))

get_dirs_from_with_sizes = partial(apply_from,
                                   lambda d: (d, os.path.getsize(d)),
                                   lambda d, f: None)


def get_largest_files(root='.', skip_dirs=None, how_many=10):
    if skip_dirs is None:
        skip_dirs = {}
    results = sorted(get_files_from_with_sizes(root=root, skip_dirs=skip_dirs),
                     reverse=True, key=lambda x: x[1])[:how_many]
    return results or []


def get_largest_dirs(root='.', skip_dirs=None, how_many=10):
    if skip_dirs is None:
        skip_dirs = {}
    results = sorted(get_dirs_from_with_sizes(root=root, skip_dirs=skip_dirs),
                     reverse=True, key=lambda x: x[1])[:how_many]
    return results or []


def _do_skip_dirs(sub_dirs, skip_dirs):
    if skip_dirs and sub_dirs:
        skip_dirs = set(skip_dirs)
        x = 0
        while x < len(sub_dirs):
            if sub_dirs[x] in skip_dirs:
                del sub_dirs[x]
            else:
                x += 1
