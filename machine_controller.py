class CacheBin:
    state = None
    states = ['opened', 'closed', 'empty', 'need maintenance', 'in maintenance']

    cache_remain = 0
