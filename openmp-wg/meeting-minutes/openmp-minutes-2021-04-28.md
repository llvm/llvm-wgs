### 2021, April 28th

### Agenda

  * Offload table ordering
  * Helper thread degradation.
  * [https://reviews.llvm.org/D101173](https://www.google.com/url?q=https://reviews.llvm.org/D101173&sa=D&source=editors&ust=1778600246555204&usg=AOvVaw28NDnOj276N8nSLvDY1cAb)
  * Depending on llvm libraries (not just the headers) (libomptarget only)
  * Getting the OpenMP offloading buildbot green (Michael)


  * http://meinersbur.de:8011/#/builders/142
  * http://meinersbur.de:8011/#/builders/143
  * Permanently failing Tests (3) with x86_64 offloading:
  *   libomptarget :: offloading/bug49334.cpp
  *   libomptarget :: offloading/memory_manager.cpp
  *   libomptarget :: offloading/parallel_offloading_map.cpp
  * https://reviews.llvm.org/D101265 (Use in-project clang as CUDA->IR compiler)


  * Virtual functions: vtable is generated for a constructor definition, and its initializer references all virtual functions that are declared within the class; does it mean that all virtual functions' definitions must be marked "declare target"?  Otherwise, if a device side vtable is ever created, some references may be unresolved.



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=48851](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D48851&sa=D&source=editors&ust=1778600246556244&usg=AOvVaw3O2HZSh6iejBtTMuZVl_3N) (refresher)



### Patches to look at

  * OMPD: [https://reviews.llvm.org/D100181](https://www.google.com/url?q=https://reviews.llvm.org/D100181&sa=D&source=editors&ust=1778600246556413&usg=AOvVaw1xXoNPHc3jAd1R7z9a2D5C) and followups



### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert (ANL)
  * George Rokos (Intel)
  * Joseph Huber (ORNL)
  * Valentin Clement (ORNL)
  * Andrey Churbanov (Intel)
