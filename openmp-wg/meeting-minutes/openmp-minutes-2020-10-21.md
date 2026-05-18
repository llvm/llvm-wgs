### 2020, October 21

### Agenda

  * Reorganization


  * Jan left AMD and Saiyed will  be  taking over.
  * Presentation at ISC has the current status.
  * Need to merge [https://reviews.llvm.org/D80816](https://www.google.com/url?q=https://reviews.llvm.org/D80816&sa=D&source=editors&ust=1778600246588875&usg=AOvVaw2QF8tfUlpdAL5a6H9OCtu_) 


  * Target mapping names


  * [https://reviews.llvm.org/D89802](https://www.google.com/url?q=https://reviews.llvm.org/D89802&sa=D&source=editors&ust=1778600246589010&usg=AOvVaw1JinHNqPFjXbi7PpyNcnVz)



#pragma omp target map(to:s) map(tofrom:sp->x) map(from:A[0:10])

A[0:10] test.cpp:4:12

s test.cpp:2:21

sp->x test.cpp:3:11

  * Fat archive libraries.
  * Test suites


  * [https://github.com/TApplencourt/OvO/](https://www.google.com/url?q=https://github.com/TApplencourt/OvO/&sa=D&source=editors&ust=1778600246589427&usg=AOvVaw3ERqxxygpGHn_OYd39lI7n)
  * [https://github.com/SOLLVE/sollve_vv](https://www.google.com/url?q=https://github.com/SOLLVE/sollve_vv&sa=D&source=editors&ust=1778600246589524&usg=AOvVaw04z6qDFKu1c5ShVrvX4rpO)
  * [https://github.com/clang-ykt/omptests](https://www.google.com/url?q=https://github.com/clang-ykt/omptests&sa=D&source=editors&ust=1778600246589619&usg=AOvVaw3eUgXEIEkT-6z19OT4Y6xS)


  * libomptarget image registration order
  * Libomptarget refactoring patch (D89654)
  * Fix compiling with debugging using ptxas causing a crash
  * \--cuda-path in regression tests (Michael)


  * https://lists.llvm.org/pipermail/openmp-dev/2020-October/003698.html
  * see: https://github.com/SOLLVE/ci/blob/knowngood_jlse/output.txt (scroll to the end)



### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Joseph Huber (ORNL)
  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert (ANL)
  * George Rokos (Intel)
  * Jon Chesterfield (AMD)
  * Shilei Tian (SBU)
  * Saiyedul Islam (AMD)
  * Andrey Churbanov (Intel)
  * Joel Denny (ORNL)
  * Raghu Maddhipatla(AMD)
  * Kelvin Li (IBM)
  * Michael Kruse (ANL)
  * Jose M Monsalve Diaz (ANL/UD)
  * Valentin Clement (ORNL)
