package cs.min2phase;

import java.io.*;

/**
 * For each state (id TAB facelets on stdin): the solution tnoodle-lib's call returns when the 200 ms of extra search
 * are set to 0, i.e. the first phase-1 that works with its shortest phase 2:
 *   SearchWCA.solution(state, 21, 60000, 0, INVERSE_SOLUTION, "R", "F")
 * The search order has no timing in it, so this is the same on every machine.
 * usage: java cs.min2phase.FirstSol < states.tsv > first.tsv
 */
public class FirstSol {
    public static void main(String[] a) throws Exception {
        Search.init();
        SearchWCA s = new SearchWCA();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String[] p = line.split("\t");
            String sol = s.solution(p[1], 21, 60000, 0, Search.INVERSE_SOLUTION, "R", "F").trim();
            System.out.println(p[0] + "\t" + sol);
        }
    }
}
