package cs.min2phase;

import java.security.SecureRandom;
import java.io.*;
import java.util.concurrent.*;

/**
 * TNoodle 333fm scramble generation, as tnoodle-lib ThreeByThreeCubeFewestMovesPuzzle + ThreeByThreeCubePuzzle do it:
 *   state = Tools.randomCube(r); sol = SearchWCA.solution(state, 21, 60000, timeMin, INVERSE_SOLUTION, "R", "F");
 *   scramble = "R' U' F " + sol + " R' U' F".
 * Subclass only records the structure (urfIdx, phase-1 / phase-2 / premove parts) of the solution it returns;
 * the search itself is untouched.
 * usage: java cs.min2phase.GenFMC N threads seed out.tsv [timeMinMs]   (TNoodle's value, and the default: 200)
 */
public class GenFMC extends SearchWCA {
    String rec;

    @Override
    protected String solutionToString() {
        String s = super.solutionToString();
        int urf = (urfIdx + 3) % 6;   // INVERSE_SOLUTION, as solutionToString
        StringBuilder p1 = new StringBuilder(), p2 = new StringBuilder(), pre = new StringBuilder();
        // move[] holds phase-1 then phase-2 moves of the last solution (in the urf frame), preMoves[] the premoves
        int d2 = 0;
        // sol counts merged moves; recover depth2 from the raw arrays: phase 2 moves are move[depth1..depth1+depth2)
        rec = urfIdx + "\t" + depth1 + "\t" + preMoveLen + "\t" + sol;
        StringBuilder raw = new StringBuilder();
        for (int i = 0; i < 31 && i < move.length; i++) raw.append(move[i]).append(',');
        StringBuilder rp = new StringBuilder();
        for (int i = 0; i < preMoveLen; i++) rp.append(preMoves[i]).append(',');
        StringBuilder ms = new StringBuilder();
        for (int i = 0; i < sol; i++) ms.append(moveSol[i]).append(',');
        rec += "\t" + raw + "\t" + rp + "\t" + ms;
        return s;
    }

    public static void main(String[] a) throws Exception {
        int n = Integer.parseInt(a[0]), th = Integer.parseInt(a[1]);
        long seed = Long.parseLong(a[2]);
        final long timeMin = a.length > 4 ? Long.parseLong(a[4]) : 200;
        PrintWriter out = new PrintWriter(new FileWriter(a[3]));
        out.println("k\tscramble\tmiddle\tfacelets\turfIdx\tdepth1\tpreMoveLen\tsol\tmove_raw\tpremoves_raw\tmovesol_raw\tms");
        Search.init();
        // warm-up (JIT), discarded
        { GenFMC g = new GenFMC(); for (int i = 0; i < 20; i++) g.solution(Tools.randomCube(new java.util.Random(i)), 21, 60000, timeMin, INVERSE_SOLUTION, "R", "F"); }
        ExecutorService ex = Executors.newFixedThreadPool(th);
        ThreadLocal<GenFMC> tl = ThreadLocal.withInitial(GenFMC::new);
        ThreadLocal<SecureRandom> tr = ThreadLocal.withInitial(SecureRandom::new);
        java.util.List<Future<String>> fs = new java.util.ArrayList<>();
        for (int k = 0; k < n; k++) {
            final int kk = k;
            fs.add(ex.submit(() -> {
                GenFMC g = tl.get();
                String st = Tools.randomCube(tr.get());
                long t0 = System.nanoTime();
                String s = g.solution(st, 21, 60000, timeMin, INVERSE_SOLUTION, "R", "F").trim();
                long ms = (System.nanoTime() - t0) / 1000000;
                return kk + "\tR' U' F " + s + " R' U' F\t" + s + "\t" + st + "\t" + g.rec + "\t" + ms;
            }));
        }
        int done = 0;
        for (Future<String> f : fs) { out.println(f.get()); if (++done % 1000 == 0) out.flush(); }
        ex.shutdown();
        out.close();
    }
}
