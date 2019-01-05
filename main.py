from file_utils import walk
# editted on branch

#walk.apply_from("hello", lambda x: x + " paul")

#walk.list_from('.\\file_utils', ['__pycache__'])

print("***** list_from")
walk.list_from(root='.', skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS)

print('\n ***** list_dirs_from')
walk.list_dirs_from(skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS)

print('\n ***** list_paths_from')
walk.list_paths_from(skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS)

print('\n ***** list_from_with_sizes')
walk.list_from_with_sizes(skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS)

print('\n ***** get_files_from_with_sizes')
print(walk.get_files_from_with_sizes(skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS))

print('\n ***** get_dirs_from_with_sizes')
print(walk.get_dirs_from_with_sizes())

print('\n ***** get_largest_files')
print(walk.get_largest_files(skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS))

print('\n ***** get_largest_files top 2 only')
print(walk.get_largest_files(skip_dirs=walk.PYTHON_PROJECT_SKIP_DIRS, how_many=2))

print('\n ***** get_largest_files top 5 only including venv')
print(walk.get_largest_files(how_many=5))

print('\n ***** get_largest_dirs top 5 only including venv')
print(walk.get_largest_dirs(how_many=5))
