#!/usr/bin/env python3
"""Every switch rule of the notes (section B), as a function of the switched state's features (F = feat.npz arrays).
Each entry: (id, DRM, source tag, rule as written in the notes, function returning the 'switch' mask, target k).
A rule's reading is on the state after the switch, i.e. the features predicted from the normal side by tracing."""
import numpy as np

def arm_in(F, codes):
    m = np.zeros(F['d'].shape, bool)
    for c in codes:
        a, b = int(c[0]), int(c[1]); mm = (F['carm'] == a) & (F['earm'] == b)
        if len(c) == 3: mm &= F['corner_case'] == 'abcd'.index(c[2])
        m |= mm
    return m
def cc(F, letter, suffix=None):
    m = F['corner_case'] == 'abcd'.index(letter)
    if suffix is not None: m &= F['case_suffix'] == suffix
    return m
P = lambda F: F['pairs']
def dfbr(F):
    """wen's "D F2 B2 R case": the cases solved by one U/D turn, F2 B2, and an R/L quarter turn."""
    import features as fx
    m = np.zeros(F['d'].shape, bool)
    for x in ('U', "U'", 'U2', 'D', "D'", 'D2'):
        for y in ('R', "R'", 'L', "L'"):
            for hh in ('F2 B2', 'B2 F2'): m[fx.state_solved_by(f'{x} {hh} {y}')] = True
    assert (F['pairs'][m] == 0).all() and (F['d'][m] == 4).all() and m.sum() == 12
    return m
def armp(F, d, k=6):
    """ARM codes of the DRM whose exact p(sub-7) exceeds a threshold (for 'ARM above 10%')."""
    return None

RULES = []
def R(i, drm, src, text, f, k=6): RULES.append((i, drm, src, text, f, k))

# ---------------- 4c4e
R('44-yura-good', (4, 4), 'D7871-D7872 Yura Riabov / D7116 Lewis Isom', 'switch ARM 00, 10, 21, 32, 42 ("good")', lambda F: arm_in(F, ['00', '10', '21', '32', '42']))
R('44-yura-decent', (4, 4), 'D7871-D7872 Yura Riabov', 'switch good + decent (31, 11)', lambda F: arm_in(F, ['00', '10', '21', '32', '42', '31', '11']))
R('44-yura-nottrash', (4, 4), 'D7086 / D7871 Yura Riabov', 'switch unless ARM 02, 12, 30, 40 ("never worth switching")', lambda F: ~arm_in(F, ['02', '12', '30', '40']))
R('44-wen-reject', (4, 4), 'D7282-D7283 wen', 'switch unless ARM 01, 02, 12', lambda F: ~arm_in(F, ['01', '02', '12']))
R('44-armthenpairs', (4, 4), 'D11021-D11023 Yura Riabov', 'switch if the ARM is above 10% and 2+ pairs (22 is 9.97%, and under 10% on Yura Riabov\'s own list, T4380)', lambda F: arm_in(F, ['00', '10', '11', '20', '21', '31', '32', '42']) & (P(F) >= 2))
R('44-caycala-5', (4, 4), 'D11016 caycala (image)', 'RZP in 5: 3-4 pairs; 2 pairs with ARM 10 11 20 21 31 32 42a; 1 pair with 21; 0 pairs with 42',
  lambda F: (P(F) >= 3) | ((P(F) == 2) & arm_in(F, ['10', '11', '20', '21', '31', '32', '42a'])) | ((P(F) == 1) & arm_in(F, ['21'])) | ((P(F) == 0) & arm_in(F, ['42'])))
R('44-caycala-5-strict', (4, 4), 'D11016 caycala (image)', 'as above, bracketed ARMs (10) (11) (20) (31) left out', lambda F: (P(F) >= 3) | ((P(F) == 2) & arm_in(F, ['21', '32', '42a'])) | ((P(F) == 1) & arm_in(F, ['21'])) | ((P(F) == 0) & arm_in(F, ['42'])))
R('44-caycala-6', (4, 4), 'D11016 caycala (image)', 'RZP in 6: 3-4 pairs, or 0 pairs with 42', lambda F: (P(F) >= 3) | ((P(F) == 0) & arm_in(F, ['42'])))
R('44-2pairs', (4, 4), 'T610 Jay / T3225 rodneykinney / D14265 / T9325 tseitsei89', 'switch 2+ pairs', lambda F: P(F) >= 2)
R('44-3pairs', (4, 4), 'T8108 rodneykinney / D11016 caycala (the always-switch tier of both rules)', 'switch 3+ pairs', lambda F: P(F) >= 3)
R('44-3anypairs', (4, 4), 'doc 69 rodneykinney (Domino Setup Theory: 12 - 2pt - 2ps <= 6); T610 Jay', 'switch 3+ pairs of any kind (top + side)', lambda F: P(F) + F['side'] >= 3)
R('44-rodney-case', (4, 4), 'T8108 rodneykinney', '3-4 pairs; 2 pairs unless 4b-0; 1 pair if 4d-2; 0 pairs never', lambda F: (P(F) >= 3) | ((P(F) == 2) & ~cc(F, 'b', 0)) | ((P(F) == 1) & cc(F, 'd')))
R('44-rodney-case+0p', (4, 4), 'T8108 + T8123 rodneykinney', 'as above, plus 0 pairs if 4a-0 or 4d-2 with no fake pairs',
  lambda F: (P(F) >= 3) | ((P(F) == 2) & ~cc(F, 'b', 0)) | ((P(F) == 1) & cc(F, 'd')) | ((P(F) == 0) & (cc(F, 'a', 0) | cc(F, 'd')) & (F['fake'] == 0)))
R('44-tetrad', (4, 4), 'D12095 rodneykinney', 'tetrad (4d) needs 1+ pair, 4b+JZP (4b-0) 3+, everything else 2+', lambda F: np.where(cc(F, 'd'), P(F) >= 1, np.where(cc(F, 'b', 0), P(F) >= 3, P(F) >= 2)))
R('44-complex', (4, 4), 'D13425 compLex', '2 pairs unless 4b; 1 pair only if 4d; 3+ pairs always', lambda F: (P(F) >= 3) | ((P(F) == 2) & ~cc(F, 'b')) | ((P(F) == 1) & cc(F, 'd')))
R('44-tseitsei', (4, 4), 'T9321 tseitsei89', '>1 pairs, or 1 pair and d corners', lambda F: (P(F) >= 2) | ((P(F) == 1) & cc(F, 'd')))
# (doc 275 / 319 rodneykinney: the 4c4e corner-case subsets are "Recommendations for normal scramble"; for NISS the doc keeps 2+ pairs.  Not graded as a switch rule.)
R('44-jay', (4, 4), 'D12085 Jay', '2+ pairs; fewer only if JZP / anti-JZP, or 1 pair and tetrad (4d)', lambda F: (P(F) >= 2) | (F['jzp'] == 1) | (F['anti_ar'] == 1) | ((P(F) == 1) & cc(F, 'd')))
R('44-wen', (4, 4), 'D14327-D14328 wen (D14333)', '2+ pairs; 1 pair if 4d or one U/D turn from 4d; 0 pairs if anti-AR or the D F2 B2 R case (one U/D turn, F2 B2, an R/L quarter turn)', lambda F: (P(F) >= 2) | ((P(F) == 1) & (cc(F, 'd') | (F['a_one_from_d'] == 1))) | ((P(F) == 0) & ((F['anti_ar'] == 1) | dfbr(F))))
R('44-fanti', (4, 4), 'doc 583 Fanti', '2+ p; 1p + ARM 21; 0p + JZP or ARM 42', lambda F: (P(F) >= 2) | ((P(F) == 1) & arm_in(F, ['21'])) | ((P(F) == 0) & ((F['jzp'] == 1) | arm_in(F, ['42']))))
R('44-daichi-4', (4, 4), 'D18953 Daichi (4-move RZP)', '2-4p; 1p except 20d, 22d; 0p except 02, 30, 40, 01b, 41b, 20d, 2c + all U',
  lambda F: (P(F) >= 2) | ((P(F) == 1) & ~arm_in(F, ['20d', '22d'])) | ((P(F) == 0) & ~arm_in(F, ['02', '30', '40', '01b', '41b', '20d']) & ~((F['carm'] == 2) & (F['corners_one_layer'] == 1))), k=7)
R('44-caycala-3p', (4, 4), 'D13393 caycala', '3+ pairs unless 3 pairs with all corners on one layer ("all white or all yellow")', lambda F: (P(F) >= 3) & ~((P(F) == 3) & (F['corners_one_layer'] == 1)))
R('44-always-4', (4, 4), 'D18940 Zagros', 'always switch a 4-move 4c4e (target DR <= 7)', lambda F: np.ones(F['d'].shape, bool), k=7)
# ---------------- 4c2e
R('42-noah', (4, 2), 'D7838 Noah Swor / D7116 Lewis Isom', 'ARM 00, 10, 31', lambda F: arm_in(F, ['00', '10', '31']))
R('42-yura', (4, 2), 'D7838-D7842 Noah Swor / Yura Riabov', 'ARM 00, 10, 31, 20, 21, 41', lambda F: arm_in(F, ['00', '10', '31', '20', '21', '41']))
R('42-caycala', (4, 2), 'D12728 caycala', '2 pairs; 1 pair if edge ARM 1 or ARM 1c0e; 0 pairs only JZP', lambda F: (P(F) >= 2) | ((P(F) == 1) & ((F['earm'] == 1) | arm_in(F, ['10']))) | ((P(F) == 0) & (F['jzp'] == 1)))
R('42-jay', (4, 2), 'T8144 Jay', '1 top pair + 1 side pair, or 2 pairs', lambda F: ((P(F) >= 1) & (F['side'] >= 1)) | (P(F) >= 2))
R('42-rodney', (4, 2), 'T9257 / doc 275 rodneykinney', '1+ pair and 1+ side pair', lambda F: (P(F) >= 1) & (F['side'] >= 1))
R('42-tseitsei', (4, 2), 'T9321 tseitsei89', '>1 pair, or 1 pair + side pair', lambda F: (P(F) >= 2) | ((P(F) == 1) & (F['side'] >= 1)))
R('42-rodney-case', (4, 2), 'T8140 rodneykinney (image)', '2 pairs unless 4a; 1 pair unless 4a or 4b-2; 0 never', lambda F: ((P(F) == 2) & ~cc(F, 'a')) | ((P(F) == 1) & ~cc(F, 'a') & ~cc(F, 'b', 2)))
R('42-fanti', (4, 2), 'doc 583 Fanti', 'not 0p; 0p + JZP', lambda F: (P(F) >= 1) | (F['jzp'] == 1))
R('42-15', (4, 2), 'T9468 rodneykinney', '"1.5+ pairs" (pairs + side pairs / 2 >= 1.5)', lambda F: F['pairs_plus_half_side_x2'] >= 3)
# ---------------- 7c8e
R('78-lewis', (7, 8), 'D7116 Lewis Isom', 'ARM 10, 21, 11, 63', lambda F: arm_in(F, ['10', '21', '11', '63']))
R('78-rodney', (7, 8), 'T8142 rodneykinney', '5 or 6 pairs', lambda F: P(F) >= 5)
R('78-tseitsei-a', (7, 8), 'T9314 tseitsei89', '5 pairs; 4 pairs if edge ARM < 2', lambda F: (P(F) >= 5) | ((P(F) == 4) & (F['earm'] < 2)))
R('78-tseitsei-b', (7, 8), 'T9282 tseitsei89', 'pairs < 4 discard; edge ARM < 2 switch; edge ARM 2 or 4 discard; else corner ARM > 3', lambda F: (P(F) >= 4) & ((F['earm'] < 2) | ((F['earm'] == 3) & (F['carm'] > 3))))
R('78-caycala', (7, 8), 'D11016 caycala (chart; the copy in D13502)', 'never edge ARM 4 or 0 except 1c0e; then 6, 5 pairs always; 4 pairs with 21, 31, 43; 3 pairs with 21',
  lambda F: ((P(F) >= 5) | ((P(F) == 4) & arm_in(F, ['21', '31', '43'])) | ((P(F) == 3) & arm_in(F, ['21']))) & ~((F['earm'] == 4) | ((F['earm'] == 0) & ~arm_in(F, ['10']))))
R('78-fanti', (7, 8), 'doc 583 Fanti', '5+ p; 4p + 21/31/43; 3p + 21', lambda F: (P(F) >= 5) | ((P(F) == 4) & arm_in(F, ['21', '31', '43'])) | ((P(F) == 3) & arm_in(F, ['21'])))
R('78-tseitsei-c', (7, 8), 'T9321 tseitsei89', 'discard 0% ARMs; then >4 pairs, or 4 pairs and edge ARM < 2', lambda F: ~arm_in(F, ['13', '14', '20', '23', '24', '30', '34', '40', '50', '51', '54', '60', '61', '64']) & ((P(F) >= 5) | ((P(F) == 4) & (F['earm'] < 2))))
# ---------------- 3c2e
R('32-always', (3, 2), 'T9294 rodneykinney / T9321 / D7286 tseitsei89', 'always switch', lambda F: np.ones(F['d'].shape, bool))
R('32-wen', (3, 2), 'D16512 wen', 'a pair, a fake pair or a split pair', lambda F: (P(F) + F['fake'] + F['split_pairs']) >= 1)
R('32-fanti-6', (3, 2), 'doc 583 Fanti (RZP in 6, sub-6 target)', '1p; 0p + ARM 00/21/31', lambda F: (P(F) >= 1) | ((P(F) == 0) & arm_in(F, ['00', '21', '31'])), k=5)
# ---------------- 4c6e
R('46-jzp', (4, 6), 'D6915 Yura Riabov / doc 384', 'only JZP', lambda F: F['jzp'] == 1)
R('46-radek', (4, 6), 'D7471-D7472 Radek B', '4 pairs or JZP', lambda F: (P(F) >= 4) | (F['jzp'] == 1))
R('46-tseitsei', (4, 6), 'T9321 tseitsei89', 'JZP with b corners', lambda F: (F['jzp'] == 1) & cc(F, 'b'))
# ---------------- 8c8e
R('88-lewis', (8, 8), 'D7116 Lewis Isom', 'ARM 00, 84, 01, 31, 63', lambda F: arm_in(F, ['00', '84', '01', '31', '63']))
R('88-tree', (8, 8), 'T9558, T9560 rodneykinney (decision tree), read out by tseitsei89 T9568-T9572', '3 or fewer fake pairs and edge ARM not 2', lambda F: (F['fake'] <= 3) & (F['earm'] != 2))
R('88-tree-6p', (8, 8), 'T9558, T9560 rodneykinney (decision tree), with the branch of T9569', '3 or fewer fake pairs, and edge ARM not 2 or 6+ pairs', lambda F: (F['fake'] <= 3) & ((F['earm'] != 2) | (P(F) >= 6)))
# (T3767 Jay / D16930 Yura Riabov, "R L gives JZP": a premove technique and a fact about one case, not a switch rule; the fact is in claims.py)
# ---------------- 3c4e, 3c6e, 5c, 6c, 2c2e
R('34-rodney', (3, 4), 'doc 275 / doc 319 rodneykinney (NISS: Sometimes)', '2+ pairs', lambda F: P(F) >= 2)
R('34-fanti', (3, 4), 'D15179 Fanti', '2p; 1p + ARM 00/21', lambda F: (P(F) >= 2) | ((P(F) == 1) & arm_in(F, ['00', '21'])))
R('36-jay', (3, 6), 'D6982 Jay', 'ARM 21 only', lambda F: arm_in(F, ['21']))
R('36-fanti', (3, 6), 'D15179 Fanti', '3p JZP-type AR (00) + 2p ARM 21', lambda F: ((P(F) >= 3) & arm_in(F, ['00'])) | ((P(F) == 2) & arm_in(F, ['21'])))
R('22-doc319', (2, 2), 'doc 319 rodneykinney', '1+ pairs', lambda F: P(F) >= 1)
