import numpy as np
from tqdm import tqdm
import multiprocessing as mp
import time

# packages for dynamic time warping
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean



###############################################################################
# LATENT VECTOR FLAG APPROACH
###############################################################################

def latent_distance(z1, z2):
    return np.linalg.norm(z2-z1)


def find_latent_distances(zs):
    # O(n.log(n)) loops
    dists = {}
    for i in tqdm(range(len(zs)), desc="z dists"):
        for j in range(i+1, len(zs)):
            dists[(i,j)] = latent_distance(zs[i], zs[j])
    return dists


def get_flagged_latents(zs, n=20):
    dists = find_latent_distances(zs)
    ordered_dists = [(k,v) for k, v in sorted(dists.items(), key=lambda item: item[1])]
    return ordered_dists[:min(n, len(ordered_dists))]

###############################################################################
# DYNAMIC TIME WARPING FLAG APPROACH
###############################################################################

def find_dtws(waves, frac=0.1):

    st = time.time()

    dists = {}
    for i in tqdm(range(len(waves)), desc="dtws"):
        for j in range(i+1, len(waves)):
            start = int(64000*0.01) # start 1/100th the way in
            end = start + int(64000*frac) # go until end of fraction
            distance, path = fastdtw(waves[i][start:end], waves[j][start:end], dist=euclidean)
            dists[(i,j)] = distance

    et = time.time()
    print("dtws: {:.2f} (s)".format(et-st))

    return dists


def get_flagged_waves(waves, n=20, frac=0.1):
    dists = find_dtws(waves, frac=frac)
    ordered_dists = [(k,v) for k, v in sorted(dists.items(), key=lambda item: item[1])]
    return ordered_dists[:min(n, len(ordered_dists))]


###############################################################################
# DYNAMIC TIME WARPING FLAG APPROACH
###############################################################################

def fastdtw_apply(i, j, w1, w2):
    distance, _ = fastdtw(w1, w2, dist=euclidean)
    return i, j, distance

def find_dtws_par(waves, frac=0.1):
    # prepare arguments list for fastdtw_apply function
    st = time.time()
    arg_list = []
    for i in range(len(waves)):
        for j in range(i+1, len(waves)):
            start = int(64000*0.005) # start 1/100th the way in
            end = start + int(64000*frac) # go until end of fraction
            arg_list.append((i,j,waves[i][start:end], waves[j][start:end]))

    # use multiprocessing to calculate dtws
    pool = mp.Pool(mp.cpu_count())
    result_objects = [pool.apply_async(fastdtw_apply, args=(i[0], i[1], i[2], i[3])) for i in arg_list]
    results = [r.get() for r in result_objects]
    pool.close()
    pool.join()

    dists = {}
    # get results into dictionary format like before
    for i in results:
        dists[(i[0], i[1])] = i[2]

    et = time.time()
    print("dtws par: {:.2f} (s)".format(et-st))

    return dists

def get_flagged_waves_par(waves, n=20, frac=0.1):
    dists = find_dtws_par(waves, frac=frac)
    ordered_dists = [(k,v) for k, v in sorted(dists.items(), key=lambda item: item[1])]
    return ordered_dists[:min(n, len(ordered_dists))]
