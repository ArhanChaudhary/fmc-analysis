package cs.min2phase;

import java.security.SecureRandom;
import java.io.*;
import java.util.concurrent.*;

/**
 * TNoodle 333fm scrambles with the 200 ms of extra search replaced by a fixed amount of search, so that the result
 * does not depend on the machine or its load: tnoodle-lib's SearchWCA, called as ThreeByThreeCubePuzzle calls it
 * (21 moves at most, first move not on R/L, last move not on F/B, solution inverted), stops at the first phase-1
 * solution it reaches after BUDGET of them have been tried since the start (and a solution exists), instead of
 * at the first one after 200 ms.  BUDGET = 0 is the first solution found.  The order of the search is untouched.
 *   java cs.min2phase.GenProbe gen N threads BUDGET out.tsv        k, scramble, facelets of the middle's state
 *   java cs.min2phase.GenProbe solve BUDGET < states.tsv            id, facelets  ->  id, middle
 */
public class GenProbe extends SearchWCA {
    long budget, calls;

    @Override
    protected int initPhase2Pre() {
        if (solution != null && calls >= budget) { isRec = false; return 0; }
        calls++;
        return super.initPhase2Pre();
    }

    String middle(String facelets) {
        calls = 0;
        // 10^9 ms of "extra search": the clock never stops it
        return solution(facelets, 21, 60000, 1000000000L, INVERSE_SOLUTION, "R", "F").trim();
    }

    public static void main(String[] a) throws Exception {
        Search.init();
        if (a[0].equals("solve")) {
            GenProbe g = new GenProbe(); g.budget = Long.parseLong(a[1]);
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            String line;
            while ((line = in.readLine()) != null) { String[] p = line.split("\t"); System.out.println(p[0] + "\t" + g.middle(p[1])); }
            return;
        }
        int n = Integer.parseInt(a[1]), th = Integer.parseInt(a[2]);
        final long budget = Long.parseLong(a[3]);
        PrintWriter out = new PrintWriter(new FileWriter(a[4]));
        ExecutorService ex = Executors.newFixedThreadPool(th);
        final ThreadLocal<GenProbe> tl = new ThreadLocal<GenProbe>() { protected GenProbe initialValue() { GenProbe g = new GenProbe(); g.budget = budget; return g; } };
        final ThreadLocal<SecureRandom> tr = new ThreadLocal<SecureRandom>() { protected SecureRandom initialValue() { return new SecureRandom(); } };
        java.util.List<Future<String>> fs = new java.util.ArrayList<Future<String>>();
        for (int k = 0; k < n; k++) {
            final int kk = k;
            fs.add(ex.submit(new Callable<String>() { public String call() {
                String st = Tools.randomCube(tr.get());
                return kk + "\tR' U' F " + tl.get().middle(st) + " R' U' F\t" + st;
            }}));
        }
        int done = 0;
        for (Future<String> f : fs) { out.println(f.get()); if (++done % 1000 == 0) out.flush(); }
        ex.shutdown(); out.close();
    }
}
