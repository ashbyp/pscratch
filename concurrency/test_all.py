import pprint
import multiprocessing
from concurrency import async_io
from concurrency import multi_process
from concurrency import no_concurrency
from concurrency import with_threading

results = [
    ('no_concurrency', no_concurrency.run()),
    ('with_threading', with_threading.run()),
    ('async_io', async_io.run()),
    ('multi_process', multi_process.run()),
]

pprint.pprint(results)
