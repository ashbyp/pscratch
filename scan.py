from file_utils import walk, misc
from timeit import default_timer as timer

users = ('Marcus', 'ashbyp', 'victoria', 'elisa', 'Public')


def scan_dirs():
    print('=============================================')
    print('Finding largest 10 folders in each users area')
    print('=============================================')

    for user in users:
        print('\nScanning, ', user)
        start = timer()
        results = walk.get_largest_dirs(root='c:/users/%s' % user)
        end = timer()
        print('Scan took %s seconds' % (end - start))
        print('Results: Total size for %s is %s' % (user, misc.convert_size(sum([x[1] for x in results]))))
        print('Top 10 are:')
        for file, size in results:
            print("  %s:\t%s" % (misc.convert_size(size), file))


def scan_files():
    print('=============================================')
    print('Finding largest 20 files in each users area')
    print('=============================================')

    for user in users:
        print('\nScanning, ', user)
        start = timer()
        results = walk.get_largest_files(root='c:/users/%s' % user, how_many=20)
        end = timer()
        print('Scan took %s seconds' % (end - start))
        print('Results: Total size for %s is %s' % (user, misc.convert_size(sum([x[1] for x in results]))))
        print('Top 20 are:')
        for file, size in results:
            print("  %s:\t%s" % (misc.convert_size(size), file))


scan_files()