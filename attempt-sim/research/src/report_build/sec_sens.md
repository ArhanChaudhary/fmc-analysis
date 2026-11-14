## 11. What depends on the costs

Since every cost is a guess, here's the stress test. I took the plans behind the conclusions and reran each one against the tuned plan with one cost or limit moved at a time: every cost of section 4 halved and doubled (writing the solution together with the time you keep for it, since you know your own writing speed), and the reading error, how often a route gives its finish, and how many DRs and EOs you see, moved down and up. That's {{V:sens_runs}} runs of 2,000 held-out scrambles each, same scrambles every time. *Better* or *worse* means more than two standard errors, *level* means less. Each row is a plan:

{{T:sens}}

If a plan keeps its verdict in most runs and nothing flips it to the other side, I'd call that conclusion solid. The last column names the moved costs that do flip it.

What holds up:

- **Solid:** the stuff about how much you look at. Finishing only a couple of DRs, 1 RZP state per short EO, 2 or 8 routes per DR, never switching and writing EOs until minute 16 are worse in pretty much every run. 8 RZP states per short EO and the quick route plus a written 22 are better or level in every run, never worse. The baseline loses to the tuned plan in every single run.
- **Flat whatever the costs:** the time split between 3-12 minutes of EOs and 25-40 minutes of DR search, the adaptive rules and the backups stay level or close to it everywhere.
- **Depends on you:**
  - The read cut-off. With a much noisier read of RZP states, a cut-off of 9 beats 10, so the cut-off is really about how far you trust your read.
  - The time you keep for writing. If your step times vary a lot more than the model's, 10 minutes beats 7.
  - Depth first is level or a bit worse, never better.

The same runs read the other way: how much does the tuned plan's own result move when one cost moves? That's basically the order to tune the costs in, biggest effect first. Each row is one cost or limit moved:

{{T:sens_ref}}
