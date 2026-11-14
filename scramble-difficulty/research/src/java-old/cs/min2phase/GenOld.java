package cs.min2phase;

import java.security.SecureRandom;
import java.io.*;
import java.util.concurrent.*;

/**
 * TNoodle 333fm scrambles as they were made from March 2016 until the 2019 update of min2phase reached official use:
 * the min2phase of tnoodle before commit 7f6fe84 (no premoves), called as ThreeByThreeCubePuzzle called it:
 *   Search.solution(state, 21, 60000, timeMin, INVERSE_SOLUTION, "R", "F"),   timeMin = 200 ms in TNoodle.
 * usage: java cs.min2phase.GenOld N threads timeMinMs out.tsv
 */
public class GenOld {
    public static void main(String[] a) throws Exception {
        int n = Integer.parseInt(a[0]), th = Integer.parseInt(a[1]);
        final long timeMin = Long.parseLong(a[2]);
        PrintWriter out = new PrintWriter(new FileWriter(a[3]));
        if (!Tools.isInited()) Tools.init();
        { Search g = new Search(); for (int i = 0; i < 20; i++) g.solution(Tools.randomCube(new java.util.Random(i)), 21, 60000, timeMin, Search.INVERSE_SOLUTION, "R", "F"); }
        ExecutorService ex = Executors.newFixedThreadPool(th);
        final ThreadLocal<Search> tl = new ThreadLocal<Search>() { protected Search initialValue() { return new Search(); } };
        final ThreadLocal<SecureRandom> tr = new ThreadLocal<SecureRandom>() { protected SecureRandom initialValue() { return new SecureRandom(); } };
        java.util.List<Future<String>> fs = new java.util.ArrayList<Future<String>>();
        for (int k = 0; k < n; k++) {
            final int kk = k;
            fs.add(ex.submit(new Callable<String>() { public String call() {
                String st = Tools.randomCube(tr.get());
                String s = tl.get().solution(st, 21, 60000, timeMin, Search.INVERSE_SOLUTION, "R", "F").trim();
                return kk + "\tR' U' F " + s + " R' U' F\t" + st;
            }}));
        }
        int done = 0;
        for (Future<String> f : fs) { out.println(f.get()); if (++done % 1000 == 0) out.flush(); }
        ex.shutdown();
        out.close();
    }
}
