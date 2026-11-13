**A separate check, with its own list of 8-movers, its own random skeletons and its own search: one 8-move comm on 20-move skeletons, every second spot and both ends against every spot, on the skeletons whose best is an 8-3 or better. One row per kind of skeleton. A walk is one of the two ways of starting the count, and a miss is a walk that finds nothing as good as the best.**

| Skeletons | How many | Opposite-face pairs: one neighbouring pair of moves in | Walks | Walks that find an insertion as good as the best | Misses | Misses next to an opposite-face pair | Misses the same walk finds once a pair is written the other way round |
|---|---:|---:|---:|---:|---:|---|---|
| a 3c, pairs written in the fixed order | {= EV('3c_fixed', 'skeletons') =} | {= PAIR1IN('3c_fixed') =} | {= EV('3c_fixed', 'good_walks') =} | {= EVP('3c_fixed') =} | {= EV('3c_fixed', 'good_missed') =} | {= EVALL('3c_fixed', 'missed_next_to_pair') =} | {= EVALL('3c_fixed', 'missed_found_once_a_pair_is_swapped') =} |
| a 3c, a pair written either way round | {= EV('3c_free', 'skeletons') =} | {= PAIR1IN('3c_free') =} | {= EV('3c_free', 'good_walks') =} | {= EVP('3c_free') =} | {= EV('3c_free', 'good_missed') =} | {= EVALL('3c_free', 'missed_next_to_pair') =} | {= EVALL('3c_free', 'missed_found_once_a_pair_is_swapped') =} |
| the first comm of a 5c, pairs written in the fixed order | {= EV('5c_fixed', 'skeletons') =} | {= PAIR1IN('5c_fixed') =} | {= EV('5c_fixed', 'good_walks') =} | {= EVP('5c_fixed') =} | {= EV('5c_fixed', 'good_missed') =} | {= EVALL('5c_fixed', 'missed_next_to_pair') =} | {= EVALL('5c_fixed', 'missed_found_once_a_pair_is_swapped') =} |

{= EVTEXT() =}
