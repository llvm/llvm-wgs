### 2021, August 11th

### Agenda

  * 13.0.0 release schedule



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * CMake for Ubuntu Offloading
  * Static library linking?


  * Fixed some issues with amdgpu. Working for nvlink issue: [https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246513460&usg=AOvVaw14x4lo4mnIQ5-w1l_X9o2S)
  * Nvlink doesn't support archive file linking. Solutions:


  * A new Nvlink-wrapper clang tool (code in AOMP)
  * Use llvm-ar to extract cubin files and pass to nvlink. But, llvm-ar doesn't have output_directory option.`


  * AMDGPU math headers
  * Where is an LLVM based toolchain for OpenMP offload on intel GPU? Would like to test stuff using it


  * One piece ? [https://github.com/intel/llvm/blob/openmp/openmp/libomptarget/plugins/opencl/src/rtl.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/openmp/openmp/libomptarget/plugins/opencl/src/rtl.cpp&sa=D&source=editors&ust=1778600246514036&usg=AOvVaw27fdBqwvDs-x0bLpHMNULp)
  * Spirv -> ISA at the last moment: [https://github.com/intel/compute-runtime](https://www.google.com/url?q=https://github.com/intel/compute-runtime&sa=D&source=editors&ust=1778600246514186&usg=AOvVaw3Mq-9__U53Z_cyxeDHKt7T)
  * 

  * Notes for ELF offload images : [https://reviews.llvm.org/D99553](https://www.google.com/url?q=https://reviews.llvm.org/D99553&sa=D&source=editors&ust=1778600246514337&usg=AOvVaw22A1pARKbQkqMXPsW6krnc)


  * Should I expect more comments?
  * D99612  -> D99553  
        |-> D99552  
        |-> D99551


  * LIBOMP_NUM_HIDDEN_HELPER_THREADS


  * What is the behavior if LIBOMP_NUM_HIDDEN_HELPER_THREADS=1
  * Number of helper threads should be +1


  * Alternate Async offload using omp_task_yield  (Ye Luo)  [https://reviews.llvm.org/D107656](https://www.google.com/url?q=https://reviews.llvm.org/D107656&sa=D&source=editors&ust=1778600246514779&usg=AOvVaw2Kum991crnSLlGADQoPZZH)
  * OMPD : [https://reviews.llvm.org/D100366](https://www.google.com/url?q=https://reviews.llvm.org/D100366&sa=D&source=editors&ust=1778600246514883&usg=AOvVaw0g_ap-nGneasDI_MEASGtu), [https://reviews.llvm.org/D100182](https://www.google.com/url?q=https://reviews.llvm.org/D100182&sa=D&source=editors&ust=1778600246514964&usg=AOvVaw0dARU1S0FbHqxuRtUwvXWb), [https://reviews.llvm.org/D100183](https://www.google.com/url?q=https://reviews.llvm.org/D100183&sa=D&source=editors&ust=1778600246515041&usg=AOvVaw0F5y2CK4KlnIXJrFS0IcD4), [https://reviews.llvm.org/D100184](https://www.google.com/url?q=https://reviews.llvm.org/D100184&sa=D&source=editors&ust=1778600246515118&usg=AOvVaw2gS_yBMmM1oKREiJEiaxPF), [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246515190&usg=AOvVaw3T0QRNsEO0cz2ObEQnx3BG)
  * Offloading buildbot(s)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246515558&usg=AOvVaw1sAnXO1sHIgkhMLzuci_cJ) (don't clean source dir)


  * Every regression test over 5s (-j1):


  * https://reviews.llvm.org/D107195 (90s timeouts)
  * 63.08s: libomp :: tasking/omp_taskyield.c
  * 60.10s: libomp :: tasking/omp_task_final.c
  * 50.09s: libomp :: tasking/omp_taskwait.c
  * 50.09s: libomp :: tasking/omp_task.c
  * 50.07s: libomp :: api/omp_get_wtime.c
  * 10.09s: libomp :: tasking/omp_task_if.c
  * 10.06s: libomp :: flush/omp_flush.c
  * 6.37s: libomp :: barrier/omp_barrier.c
  * 5.10s: libomptarget :: nvptx64-nvidia-cuda :: offloading/bug49334.cpp
  * 5.05s: libomp :: tasking/taskdep_if0_2.c
  * Possible solution: change SLEEPTIME in runtime/test/omp_testsuite.h to .02


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246516433&usg=AOvVaw2SdhxUK__WRAnUOaXXnecm); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246516496&usg=AOvVaw2F5tpXiamAxuvvKLeqWzwE) [FLAKY]


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246516748&usg=AOvVaw3vllhYRguSSYh8tLvv5spo) (under review)


  * [llvm.org/PR50738](https://www.google.com/url?q=http://llvm.org/PR50738&sa=D&source=editors&ust=1778600246516830&usg=AOvVaw0eoqXMxrUKKIBfco7r0w-M); [llvm.org/PR51150](https://www.google.com/url?q=http://llvm.org/PR51150&sa=D&source=editors&ust=1778600246516886&usg=AOvVaw1GPS8K7qQlfhg11qgm5Rk2)


  * FAIL: libomptarget :: x86_64-pc-linux-gnu::memory_manager.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::parallel_offloading_map.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::taskloop_offload_nowait.cpp


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246517195&usg=AOvVaw2hNy0Jz50pqwQtFSOkbx6f) [FLAKY]


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp


  * [https://reviews.llvm.org/D107670](https://www.google.com/url?q=https://reviews.llvm.org/D107670&sa=D&source=editors&ust=1778600246517394&usg=AOvVaw20CkWY84es-9Zj3GK4FGmF); [https://reviews.llvm.org/D107706](https://www.google.com/url?q=https://reviews.llvm.org/D107706&sa=D&source=editors&ust=1778600246517466&usg=AOvVaw3Qe99ywK_UGa1H3y99Qhvp); [https://reviews.llvm.org/D107716](https://www.google.com/url?q=https://reviews.llvm.org/D107716&sa=D&source=editors&ust=1778600246517536&usg=AOvVaw2UEAwi_U_8WSpUIAF_swPf) [AMDGPU buildbot]



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246517687&usg=AOvVaw1vTINCX0CYhYbUY6zwWG0d), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246517757&usg=AOvVaw13Xfxl-UZ43pHhbtWscyg3) )
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246517893&usg=AOvVaw3VNUsFJVqNVUwpOeLXi5kt) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply
  * https://bugs.llvm.org/show_bug.cgi?id=51117 


  * pre-merge bot failing with libarcher failures: https://reviews.llvm.org/D105811  [https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246518330&usg=AOvVaw2nHK3vU87EXEmAhYRv2RET)
  * Fixed by D106855


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246518717&usg=AOvVaw0f8yrcnJutEjUqaz1QmUHu)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload archicture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246518938&usg=AOvVaw2B7vsVvWw6W6Imx97VgXID)


  * Rpath, runpath, env vars and fragility of toolchains when more than one are on disk



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49787](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49787&sa=D&source=editors&ust=1778600246519205&usg=AOvVaw2rvnrN8Ol1QzBoIuck4uTY) compiler/runtime API mismatch for async mapping
  * [https://bugs.llvm.org/show_bug.cgi?id=50336](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50336&sa=D&source=editors&ust=1778600246519357&usg=AOvVaw3YtAI95TBkHNswjTGoIMsg) (Should be fixed in [https://reviews.llvm.org/D107668](https://www.google.com/url?q=https://reviews.llvm.org/D107668&sa=D&source=editors&ust=1778600246519444&usg=AOvVaw0MJvw2VtjdCYw_qXO5l_DG))



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Joseph Huber (ORNL)
  * Saiyedul Islam (AMD)
  * George Rokos (Intel)
