### 2022, Dec 07

Agenda

  * OpenMP-opt slack:


  * [https://join.slack.com/t/openmp-opt/shared_invite/zt-1ktv8h0wx-6Ks4PjL3qnx8dhC9Nx4fgg](https://www.google.com/url?q=https://join.slack.com/t/openmp-opt/shared_invite/zt-1ktv8h0wx-6Ks4PjL3qnx8dhC9Nx4fgg&sa=D&source=editors&ust=1778600246227771&usg=AOvVaw1wpidc0Qbq2l7C9i7S-v4a) 


  * Pinned memory:


  * ½ [https://reviews.llvm.org/D138933](https://www.google.com/url?q=https://reviews.llvm.org/D138933&sa=D&source=editors&ust=1778600246227914&usg=AOvVaw1AZCjJYeTGTx5X5KEDOSKg)
  * 2/2 [https://reviews.llvm.org/D139208](https://www.google.com/url?q=https://reviews.llvm.org/D139208&sa=D&source=editors&ust=1778600246228034&usg=AOvVaw3E97gRn9sjbpsv2QT_gDDE) 


  * NextGen AMD Plugin


  * Jan-Patrick is testing it
  * Latest status: [https://github.com/kevinsala/llvm-project/tree/develop](https://www.google.com/url?q=https://github.com/kevinsala/llvm-project/tree/develop&sa=D&source=editors&ust=1778600246228267&usg=AOvVaw0iX6fQK4P16JiEQ4lGarQr) 


  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)
  * 

  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246228765&usg=AOvVaw2EN_ZB85maoR8nDdpO3ApB)) 


  70. Allocate "all" device memory
  71. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  72. Replay -> load image + user allocated memory, launch with argos and parameters


  * New meeting time for Jan 23, when2meet?
  *   * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246229218&usg=AOvVaw1PpAzamfZG2gHG45_xVbGa)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246229300&usg=AOvVaw3fH8nD5r2a3b8BLdX-F0NT)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246229513&usg=AOvVaw1r40qUc3r0e2KVMuSYQzVU)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246229764&usg=AOvVaw2VWxLXWbiXbKxvJWBQpLIo) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246229916&usg=AOvVaw3uKMxj9lYz7m-acn4LJBBb)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246230064&usg=AOvVaw3ipBKOsVeinR8UnlwAMfBr)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246230308&usg=AOvVaw2RoEnnsuORlRQ9wHUcAJ6t) 


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246230418&usg=AOvVaw38P6qT-QPXxcY3iULmoWj8)
  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246230507&usg=AOvVaw3-YuIoZuEdEPyJRf1z3GhK)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246230650&usg=AOvVaw1p_aWAyBA3M9zpREAVp4B1)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246231313&usg=AOvVaw3Xr06JWEaQQgiRL3kKNRlm)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246231491&usg=AOvVaw0aruo_-1Cra0fMKeRBcV89)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246231589&usg=AOvVaw0-fRCDhziBTATDFGnE9rKD) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246231739&usg=AOvVaw2W0auO3GqH19E228o0bdQP) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246232258&usg=AOvVaw3egLHUR3IMy8iCoey8LuXe) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246232429&usg=AOvVaw0Onjz8PPegr3TzZHTx8urM) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246232626&usg=AOvVaw1_ylbmDzQENAmFxso0N7n3)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246232805&usg=AOvVaw3eP0fse6c1BDD6CZ3ppUJH)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246232952&usg=AOvVaw2VU7UQm9xbLSiDq05Pa9fj): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246233135&usg=AOvVaw3NttawyDjUfCW0uCAZQHOr) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
