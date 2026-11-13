| DRM | Cell (read on the switched side) | Verdict | States | Share of the DRM | Sub-7 rate, exact |
|---|---|---|---|---|---|
| 4c4e | both bad U/D edges paired | switch | 10,920 | 15.5% | 59.9% |
|  | one paired, edge ARM 1 (the two bad edges in different slices) | check | 22,944 | 32.5% | 20.0% |
|  | one paired, edge ARM 0 or 2 (both bad edges in one slice) | discard | 15,696 | 22.2% | 9.8% |
|  | no bad edge paired | discard | 21,000 | 29.8% | 4.3% |
| 4c2e | pairs + side pairs/2 is 1.5 or more | switch | 2,992 | 22.3% | 57.0% |
|  | pairs + side pairs/2 is exactly 1 | check | 3,304 | 24.6% | 15.7% |
|  | pairs + side pairs/2 is 0 or 0.5 | discard | 7,144 | 53.2% | 4.0% |
| 3c2e | always | switch | 3,584 | >99.9% | 61.6% |
| 7c8e | 5 or 6 pairs | switch | 3,840 | 16.3% | 59.0% |
|  | 4 pairs | check | 7,920 | 33.7% | 15.9% |
|  | 3 pairs or fewer | discard | 11,760 | 50.0% | 2.9% |
| 8c8e | corner ARM 0, 4 or 8 | check | 2,660 | 44.2% | 20.5% |
|  | corner ARM 2, 3, 5 or 6 | discard | 3,360 | 55.8% | 9.8% |
| 2c2e | a bad U/D edge with a pair | switch | 416 | 23.2% | 59.6% |
|  | no pair, but JZP | check | 144 | 8.0% | 38.9% |
|  | no pair, not JZP | discard | 1,232 | 68.8% | 9.7% |
| 4c6e | JZP | switch | 576 | 0.61% | 61.1% |
|  | 4 pairs | check | 1,136 | 1.2% | 47.9% |
|  | anything else | discard | 92,368 | 98.2% | 3.7% |
| 3c4e | 2 pairs | check | 2,016 | 10.7% | 33.7% |
|  | 0 or 1 pair | discard | 16,800 | 89.3% | 7.1% |
| 3c6e | always | discard | 25,088 | >99.9% | 4.8% |
| 5c4e | 3 pairs | check | 5,760 | 6.1% | 27.6% |
|  | 2 pairs or fewer | discard | 88,320 | 93.9% | 5.9% |
| 5c6e | 4 pairs | check | 3,840 | 3.1% | 37.9% |
|  | 3 pairs or fewer | discard | 121,600 | 96.9% | 5.1% |
| 6c6e | JZP, or 5 or 6 pairs | check | 1,744 | 1.3% | 39.0% |
|  | anything else | discard | 136,240 | 98.7% | 5.2% |
