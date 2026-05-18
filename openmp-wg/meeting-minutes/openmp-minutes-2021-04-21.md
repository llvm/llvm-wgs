### 2021, April 21th

### Agenda

  * Offload table ordering
  * Helper thread degradation.
  * Supporting present/iterator and release/delete in declare mapper map
  * Depending on llvm libraries (not just the headers)
  * Static library (gpu newsletter referenced an email question about putting omp objects in one, though I can't find said question)
  * Getting the OpenMP offloading buildbot green (Michael)


  * Permanently failing Tests (3) with x86_64 offloading:
  *   libomptarget :: offloading/bug49334.cpp
  *   libomptarget :: offloading/memory_manager.cpp
  *   libomptarget :: offloading/parallel_offloading_map.cpp



### Open Bugs

  * Unfortunate bug: [49777](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49777&sa=D&source=editors&ust=1778600246557614&usg=AOvVaw31akeI1nQYUCOb_NMOrlV9)
  * Segfault which we failed to debug properly so far: [49698](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49698&sa=D&source=editors&ust=1778600246557743&usg=AOvVaw2511_KR-INyfC9ittrvRWa) 



### Patches to look at

  * OMPD: [https://reviews.llvm.org/D100181](https://www.google.com/url?q=https://reviews.llvm.org/D100181&sa=D&source=editors&ust=1778600246557895&usg=AOvVaw3IOJjH7yy0qUgO7gJtW1zI) and followups



### Participants (voluntary/incomplete listing)

  * George Rokos (Intel)
  * Jon Chesterfield (AMD)
  * Joseph Huber (ORNL)
  * Ravi Narayanaswamy (Intel)
