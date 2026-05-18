### 2020, August 12

### Agenda

  1. Roll Call  Put your name in the participants list below (if you want)
  2. administrative things: weekly meetings, google docs, 



Need regular backups of the document

  3. Open :



Plugin :    …

  Jon made AMD plugin runtime. About 6000 lines, only builds if a cmake variable ROCM_DIR is set.  Would like to check in as is.

  Johannes prefers to work on enabling testing (after merge)

  Order plugin  table in chronological order.

Greg wants libomptarget to look in current directory for plugin to avoid using LD_LIBRARY_PATH

Greg also want some early check  for device availability before loading plugin

  4. present clause (Joel)



Done.  target update, target data. For target regions checked on entry and exit.

Need clarification about map and present  clause ordering.

Alexey is working on reordering mapping clauses based on 5.0 requirements.

  5. Status of failures when switching OpenMP version to 50 (Saiyed)


  1. https://reviews.llvm.org/D84844
  2. https://reviews.llvm.org/D85150
  3. https://reviews.llvm.org/D85214



       360 tests need to be updated.. Hopefully it will be done by next week.

       Split test to run in parallel. ([https://reviews.llvm.org/D85695](https://www.google.com/url?q=https://reviews.llvm.org/D85695&sa=D&source=editors&ust=1778600246610329&usg=AOvVaw2Y90P3veFiBgtp5XOZw-5v) & [https://reviews.llvm.org/D85551](https://www.google.com/url?q=https://reviews.llvm.org/D85551&sa=D&source=editors&ust=1778600246610411&usg=AOvVaw0xYVA--OGRTvph_BW8th0f))

  6. target memory manager & pool allocator (Shilei)



            Patches are [https://reviews.llvm.org/D81054](https://www.google.com/url?q=https://reviews.llvm.org/D81054&sa=D&source=editors&ust=1778600246610586&usg=AOvVaw32u-2qHDL8h3KrrbZHQ60Q) and [https://reviews.llvm.org/D85274](https://www.google.com/url?q=https://reviews.llvm.org/D85274&sa=D&source=editors&ust=1778600246610658&usg=AOvVaw0i2EWBI40yLrTpCoMSWnGI)

  7. unshackled task / async support (Shilei)
  8. Heterogeneous LLVM-IR Modules (Johannes)
  9. Support fat static library
  10. Libomptarget dependency handling (Shilei)
  11. OpenMP IRBuilder status, Flang + OpenMP
  12. OpenMP optimization command center (Johannes)
  13. Automatic detection of target pragmas without user command line -fopenmp-targets=
  14. DeviceRTL redesign to support sharing code
  15. OpenMP feature tracking status ( https://clang.llvm.org/docs/OpenMPSupport.html)
  16. LTO for fat binary linking



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=47063](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D47063&sa=D&source=editors&ust=1778600246611456&usg=AOvVaw3IsUdgxQJU4sMJojIIBF36)
  * [https://bugs.llvm.org/show_bug.cgi?id=47122](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D47122&sa=D&source=editors&ust=1778600246611577&usg=AOvVaw2Nb7ihdADoUFdrry6Jtb6P)



### Patches to look at

  * [https://reviews.llvm.org/D80816](https://www.google.com/url?q=https://reviews.llvm.org/D80816&sa=D&source=editors&ust=1778600246611720&usg=AOvVaw2DQYK6NlKpZV9C93JXYEbd) \- clang-offload-bundler (SDL) -  needs approval/review.



### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert (ANL)
  * George Rokos (Intel)
  * Joel Denny, Valentin Clement (ORNL)
  * Kelvin Li (IBM)
  * Shilei Tian (SBU)
  * Lukas Sommer (TU Darmstadt)
  * Roger Ferrer Ibañez (Barcelona Supercomputing Center)
  * Saiyedul Islam, Raghu Maddhipatla, Rich Bleikamp, Greg Rodgers, Jan Sjodin (AMD)
  * Ye Luo(ANL)
  * Michael Kruse (ANL)
  * Andrey Churbanov (Intel)



* * *

## Meeting Template (to be copied into next meeting)

### <Date>

### Agenda

  * 


### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  *   *   *   *   *   *   *   *   *   *   *
