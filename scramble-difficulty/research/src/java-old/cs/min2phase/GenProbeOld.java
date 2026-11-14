package cs.min2phase;

import java.security.SecureRandom;
import java.io.*;
import java.util.concurrent.*;

/**
 * As GenProbe, for the min2phase TNoodle used from March 2016 until its 2019 update reached official scrambles
 * (sources made by mk_old_probe.sh).
 *   java cs.min2phase.GenProbeOld gen N threads BUDGET out.tsv
 *   java cs.min2phase.GenProbeOld solve BUDGET < states.tsv
 */
public class GenProbeOld {
    static String middle(Search g, long budget, String facelets) {
        g.budget = budget;
        return g.solution(facelets, 21, 60000, 200, Search.INVERSE_SOLUTION, "R", "F").trim();
    }
    public static void main(String[] a) throws Exception {
        if (!Tools.isInited()) Tools.init();
        if (a[0].equals("solve")) {
            Search g = new Search(); long b = Long.parseLong(a[1]);
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            String line;
            while ((line = in.readLine()) != null) { String[] p = line.split("\t"); System.out.println(p[0] + "\t" + middle(g, b, p[1])); }
            return;
        }
        int n = Integer.parseInt(a[1]), th = Integer.parseInt(a[2]);
        final long budget = Long.parseLong(a[3]);
        PrintWriter out = new PrintWriter(new FileWriter(a[4]));
        ExecutorService ex = Executors.newFixedThreadPool(th);
        final ThreadLocal<Search> tl = new ThreadLocal<Search>() { protected Search initialValue() { return new Search(); } };
        final ThreadLocal<SecureRandom> tr = new ThreadLocal<SecureRandom>() { protected SecureRandom initialValue() { return new SecureRandom(); } };
        java.util.List<Future<String>> fs = new java.util.ArrayList<Future<String>>();
        for (int k = 0; k < n; k++) {
            final int kk = k;
            fs.add(ex.submit(new Callable<String>() { public String call() {
                String st = Tools.randomCube(tr.get());
                return kk + "\tR' U' F " + middle(tl.get(), budget, st) + " R' U' F\t" + st;
            }}));
        }
        int done = 0;
        for (Future<String> f : fs) { out.println(f.get()); if (++done % 1000 == 0) out.flush(); }
        ex.shutdown(); out.close();
    }
}
