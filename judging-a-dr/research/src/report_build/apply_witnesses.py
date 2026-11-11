import re, sys
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool')
import fmccube as fc
def solved_by(state_seq, sol_seq):
    return fc.apply(fc.apply(fc.solved(), fc.parse(state_seq)), fc.parse(sol_seq)) == fc.solved()
PAIRS = [("R L' B2 D2 R L'", "L R' D2 B2 L R'"), ("F' B R2 D2 F B'", "B F' D2 R2 B' F"), ("R D2 F2 B2 R' L F2 R'", "R F2 L' R B2 F2 D2 R'"),
         ("F L2 F B' R2 L2 D2 F'", "F D2 L2 R2 B F' L2 F'"), ("L' F2 R L' F2 B2 D2 L", "L' D2 B2 F2 L R' F2 L"),
         ("L2 B2 D B2 L2 R2 F2 U'", "U F2 R2 L2 B2 D' B2 L2"), ("B2 L2 D L2 B2 F2 R2 U'", "U R2 F2 B2 L2 D' L2 B2"),
         ("U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2", "U B2 L2 F2 D F2 D"), ("U L2 R2 U R2 B2 U L2", "L2 U' B2 R2 U' R2 L2 U'"),
         ("U' L2 D' B2 U' B2 U L2 D", "D' L2 U' B2 U B2 D L2 U"), ("D F2 U' B2 F2 D'", "D F2 B2 U F2 D'"), ("U L2 R2 U L2 R2 U'", "U R2 L2 U' R2 L2 U'"),
         ("D F2 R2 F2 D", "D' F2 R2 F2 D'")]
for a, b in PAIRS: assert solved_by(a, b), (a, b)
print('all quoted state/solution pairs check out on the facelet simulator')

class Doc:
    def __init__(self, path): self.path = path; self.L = open(path).read().split('\n')
    def find(self, prefix):
        hits = [i for i, l in enumerate(self.L) if l.startswith(prefix)]
        assert len(hits) == 1, (self.path, prefix[:50], len(hits)); return hits[0]
    def replace_line(self, prefix, new): self.L[self.find(prefix)] = new
    def append(self, prefix, add): i = self.find(prefix); self.L[i] = self.L[i] + add
    def sub(self, prefix, a, b):
        i = self.find(prefix); assert self.L[i].count(a) == 1, (prefix[:40], a[:40], self.L[i].count(a)); self.L[i] = self.L[i].replace(a, b)
    def insert_after(self, prefix, text): i = self.find(prefix); self.L[i+1:i+1] = text.split('\n')
    def save(self): open(self.path, 'w').write('\n'.join(self.L))

setup_table = open('/data/fmc/judging-a-dr/report/data/setup_bound_examples.md').read().strip('\n')
F = Doc('new_front.md')
F.replace_line('- **Bounds graded.**', "- **Bounds measured.** Levi's 1qt formula, trangium's 2q bound taken to any qt, HTR length, corner length with parity. Which hold for every finish, how often a finish with extra quarter turns gets under the others, and how far below optimal they all sit.")
F.append('- **Optimal leave slice of every DR state.**', " (`U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'` needs 18 for the leave slice and 18 for the full finish.)")
F.insert_after('- *L + longest HTR predicts within ~1 move*', """
A pair that shows what the first hunch is up against. Both are 2c4 4e, with the same corner case on normal and on inverse, 7 to HTR on both sides, and the same corner length (7):

    D F2 U' F2 D B2 D'                                 // optimal 7
    D' R2 B2 U' F2 D B2 U B2 F2 U' F2 U' L2 D' U'      // optimal 16""")
F.append('The baseline, and still the biggest single piece of information.', """ One of each 18:

    F2 L2 U B2 F2 R2 B2 F2 R2 U F2 R2 D U F2 R2 D' U'      // 0c0 8e
    F2 D' F2 D' F2 R2 U2 R2 U' B2 R2 B2 L2 U B2 U2 R2 U'   // 0c3 4e
    U2 L2 D B2 U' B2 U' L2 D B2 R2 U R2 U R2 U2 R2 U'      // 2c5 0e
    R2 F2 L2 D' F2 D' B2 F2 R2 U2 F2 D' B2 U2 L2 U' R2 U'  // 2c5 4e

Appendix G has a longest one for every subset.""")
F.replace_line('The shortest possible HTR by corner qt is', "The shortest possible HTR by corner qt is 1 / 3 / 5 / 7 / 9 moves for 1 to 5 qt. These five states have exactly that on both sides: `D`, `D B2 D'`, `D' B2 D' B2 D'`, `D B2 D' B2 D B2 D'`, `U' L2 U R2 U' L2 U R2 D`. Joba took 1 / 2 / 4 / 6 / 8 as a safe lower bound ([[T6639]]); the exact floor is one higher from 2qt up, on either side.")
F.append('Both sides together: best is the first case on both sides', " The fastest any double-stacked 2c4 finishes is 11: `U2 L2 D' F2 U' R2 U F2 D L2 U2`.")
F.append('**2c5.** Three cases:', " The fastest any double-stacked 2c5 finishes is 13: `U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2`.")
F.append("**Zagros's rule, \"4c3", " The rule does throw away real finds: `U' L2 D' B2 U' B2 U L2 D` is a 4c3 4e that is 9 to HTR on both sides and finishes in 9 (`D' L2 U' B2 U B2 D L2 U`).")
F.sub('Knowing the two HTR lengths does not give you a better', "in every subset some state finishes in exactly max(normal, inverse).", "in every subset some state finishes in exactly max(normal, inverse). The 4c3 4e just above is one, and Appendix G has one for every subset.")
F.replace_line("| Levi's formula, HTR normal + HTR inverse − 1 (4a1 4e)", "| Levi's 1qt formula, HTR normal + HTR inverse − 1 (4a1 4e) | never for a finish with one quarter turn. A finish with three is shorter for 11.7% of 4a1 4e | 10.85 | 12.27 |")
F.replace_line('| setup + HTR, any qt (below)', '| setup + HTR, any qt (below) | never for a finish with the minimum number of quarter turns. A finish with more is shorter for 2.6% at 1–2qt and 0.002% above | see below | |')
F.replace_line("**Levi's formula.** (HTR normal) + (HTR inverse) − 1", "**Levi's formula.** (HTR normal) + (HTR inverse) − 1 bounds the finishes with one quarter turn, which is what Levi's doc uses it for. A 1qt state can also be solved with three quarter turns, and the number worth having is how often that is shorter. Over all 286,654,464 states of 4a1 4e, the optimal is below the formula for 11.7% (by 1 in 8.4%, by 2 in 2.7%, by 3+ in 0.6%), equal for 18.0%, above for 70.3%. If the formula says ≤ 12, a 3qt finish beats it 2.5% of the time. Example:")
F.replace_line('One more thing about 4a1 4e', """One more thing about 4a1 4e that I haven't seen written down: for 72 of its 432 cases (one in six) the shortest HTR is not a 1qt HTR at all. The shortest 1qt path is 8, 9 or 10 moves and a 3qt HTR does it in 7 or 8. So "shortest HTR" and "shortest way to the trigger" are different numbers there, and the formula wants the second. One where it happens on both sides:

    U L2 R2 U R2 B2 U L2          // 4a1 4e
    U L2 F2 L2 U B2 U             // shortest HTR on normal: 7, three quarter turns
    R2 F2 U2 R2 F2 U2 L2 D        // shortest HTR with one quarter turn: 8
    L2 U' B2 R2 U' R2 L2 U'       // optimal finish: 8

(The inverse is the same: 7 with three quarter turns, 8 with one.)""")
F.sub('| | Fails | Exact |', '| | Fails |', '| | Beaten by extra qts |')
F.replace_line('It fails for 23.8% of 4a1 4e', "A finish with extra quarter turns gets under it for 23.8% of 4a1 4e (more than the 11.7% for Levi's formula because this one uses the real setup, see above), 2.2% of 4a2 4e, 1.3% of 4a2 0e, 0.9% of 4b2 4e, and for 0.002% of everything at 3qt and up. So from 3qt it's as good as a true bound. One state for every subset where it happens (there are 13):\n\n" + setup_table + "\n\nDaichi's objection ([[T11457]]) holds everywhere: it adds two moves to the HTR bound at 2qt, half a move at 3–4qt, nothing at 5qt (a qt that lowers the count is always available right away), and it sits three or more under optimal for most DRs.")
F.save()

OLD1 = """**Levi's formula (4e only)**: shortest *1qt* HTR on normal + on inverse − 1. For one case in six the shortest HTR is a 3qt one, and the formula wants the 1qt length. The optimal is below the formula 11.7% of the time (2.5% when the formula says 12 or less), so read it as "almost always"."""
NEW1 = """**Levi's formula (4e only)**: shortest *1qt* HTR on normal + on inverse − 1. It bounds the finishes with one quarter turn. For one case in six the shortest HTR is a 3qt one, and the formula wants the 1qt length. A 3qt finish is shorter than the formula 11.7% of the time (2.5% when the formula says 12 or less)."""
OLD2 = """**Don't conclude** that the formula is a strict bound on 4e either. When a 4a1 4e is very blocky and the formula still says 10+, look at 3qt finishes."""
NEW2 = """**Don't forget** the 3qt finishes on 4e. When a 4a1 4e is very blocky and the formula still says 10+, look for one: `U2 F2 R2 B2 U D2 B2 R2 B2 R2 F2` has formula 10 and a 3qt finish in 7 (`U B2 L2 F2 D F2 D`).<br>2e and 0e really need three quarter turns: `D F2 U' B2 F2 D'` (4a1 2e) is solved by `D F2 B2 U F2 D'`, and `U L2 R2 U L2 R2 U'` (4a1 0e) by `U R2 L2 U' R2 L2 U'`."""
for p in ('section8.md', 'new_tail.md'):
    T = Doc(p)
    T.sub('| **4a1**', OLD1, NEW1)
    T.sub('| **4a1**', OLD2, NEW2)
    T.sub('| **0c0**', "every 0c0 with bad edges needs two.", "every 0c0 with bad edges needs two. The shortest 0c0 2e is `D F2 R2 F2 D`, solved by `D' F2 R2 F2 D'`.")
    T.sub('| **4c3**', "6.4% of what it drops finishes in 12 and 34% in 13.", "6.4% of what it drops finishes in 12 and 34% in 13. `U' L2 D' B2 U' B2 U L2 D` is 9 to HTR on both sides and finishes in 9.")
    T.sub('| **2c5**', "**Stacked on both sides: never a 12, 0.6% in 13.**", "**Stacked on both sides: never a 12, 0.6% in 13** (the fastest is 13: `U2 F2 U' R2 U F2 D' L2 U B2 U' L2 U2`).")
    T.sub('| **2c4**', "A stack on both sides. 10 to HTR on both sides.", "A stack on both sides (the fastest any of them finishes is 11: `U2 L2 D' F2 U' R2 U F2 D L2 U2`). 10 to HTR on both sides.")
    T.save()
T = Doc('new_tail.md')
T.insert_after('- **Setup lengths** for the setup + HTR bound', "- **Example scrambles**: every scramble quoted as an example of something was found by a search over all DR states, then re-read from its text alone (subset, HTR lengths, leave slice and optimal recomputed from the moves). The ones that stand against something a person wrote were also solved with nissy.")
s = '\n'.join(T.L)
a = "## Docs and sheets referred to\n"
assert s.count(a) == 1
s = s.replace(a, """## Appendix G: a scramble for every subset

For each of the 48 subsets: a state with the longest optimal finish in the subset, and a state that finishes in exactly its longer HTR (so the HTR length is all the bound you get from HTR lengths, in every subset). Do the scramble on a solved cube.

{{WITNESSES}}

---

""" + a)
open('new_tail.md', 'w').write(s)

V = Doc('WRITEUP_first_version.md')
V.insert_after('DR-move values never go above 10, so anything shorter', "\nThe two that get shorter with quarter turns, explicitly. `L2 B2 D B2 L2 R2 F2 U'` is a state of \"R-D − F-V R-V even\", and `U F2 R2 L2 B2 D' B2 L2` solves it in 8. `B2 L2 D L2 B2 F2 R2 U'` is a state of \"F-D − F-V R-V even\", and `U R2 F2 B2 L2 D' L2 B2` solves it in 8. With half turns alone both cases need 9.")
V.save()
a = open('assemble.py').read()
x = ".replace('{{SQUARES}}', data('htr_square_tables.md'))"
assert a.count(x) == 1
a = a.replace(x, x + ".replace('{{WITNESSES}}', data('witnesses_by_subset.md'))")
x = " 'Appendix F: HTR length on both sides, all 48 subsets': 'The square tables.',\n"
assert a.count(x) == 1
a = a.replace(x, x + " 'Appendix G: a scramble for every subset': 'A longest state, and one that finishes in exactly its longer HTR, for each of the 48 subsets.',\n")
open('assemble.py', 'w').write(a)
s = open('start_here.md').read(); assert 'six appendices' in s
open('start_here.md', 'w').write(s.replace('six appendices', 'seven appendices'))
print('sources edited')
