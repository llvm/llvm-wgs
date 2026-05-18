### 2023, Jan 25

Agenda

  * Next meeting Feb 8th
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246189758&usg=AOvVaw2VvRzrJoiLZGzuhUB50M10) 
  * New kernel launch API: [https://reviews.llvm.org/D141232](https://www.google.com/url?q=https://reviews.llvm.org/D141232&sa=D&source=editors&ust=1778600246189884&usg=AOvVaw3oxWwXr8g3jUY3yUgO8CYF)
  * Dynamic shared memory per kernel: [https://reviews.llvm.org/D141233](https://www.google.com/url?q=https://reviews.llvm.org/D141233&sa=D&source=editors&ust=1778600246190010&usg=AOvVaw21ydLWkiQ4MLLPGNGiXRwI) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246190118&usg=AOvVaw2ev5tE_wGI3akQt0EOoLQ6) 
  * Num threads: [https://github.com/llvm/llvm-project/blob/feee22db52259d19a8624318517ef5688abfc67c/openmp/libomptarget/DeviceRTL/src/State.cpp#L356](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/feee22db52259d19a8624318517ef5688abfc67c/openmp/libomptarget/DeviceRTL/src/State.cpp%23L356&sa=D&source=editors&ust=1778600246190371&usg=AOvVaw2IwOK-iEc0sOMtd-Lij_6T) 
  * Only build GPU tests if a GPU is found on the system: [https://reviews.llvm.org/D142018](https://www.google.com/url?q=https://reviews.llvm.org/D142018&sa=D&source=editors&ust=1778600246190518&usg=AOvVaw3ZlYbqTgRcGwQQ-NZnL_Vz)
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246191010&usg=AOvVaw2noNZAHfC8uJ7PBud5cFSW)


  52. Allocate "all" device memory
  53. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  54. Replay -> load image + user allocated memory, launch with argos and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246191382&usg=AOvVaw2IEu8qrUBNL5G1b8jJpds1)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246191471&usg=AOvVaw3vJzXeFNPhcBEs6XpD0Ve6)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246191687&usg=AOvVaw1T-iHblha1O-SA-f5vgOO9)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246191942&usg=AOvVaw2OZA5hVXl_C6vWrIuSEU2S) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246192090&usg=AOvVaw1X9H6rrb8II5Ry5Wscmafk)


  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246192207&usg=AOvVaw1cOFntuE3gcf8wYc36Laq_)


  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246192344&usg=AOvVaw11DCeMmzROMC5JpcKp9i1W)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246192577&usg=AOvVaw37G6bzBur4wZUGo1jxhCrN) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246192667&usg=AOvVaw1ACVddxGH7Os6LUjI1Z6Xb)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246192803&usg=AOvVaw3Z1SH8LpZlg39XojkHs7bE)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246193548&usg=AOvVaw2Y2jJrx4mbqofdAFAUIXnm)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246193718&usg=AOvVaw17nZpu_TaVmVfdNtxhRO8d)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246193822&usg=AOvVaw1mgYJBlLH4j6yAZb3AoH8R) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246193979&usg=AOvVaw3r03NLgJ_bbndbgRegrn7S) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246194503&usg=AOvVaw0caBPfSAd6QqL5FhjJp13-) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246194680&usg=AOvVaw2MrYX_xayy0SpiwX1fQhE5) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246194923&usg=AOvVaw2IG5qPfSRBXkji-o2BUsVa)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246195121&usg=AOvVaw0L7q10ggnXfn5lvfLVieCV)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246195283&usg=AOvVaw3s8egtO0aAmNtbIfcvWC01): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246195473&usg=AOvVaw3DRnOG0dLoz7oyCQr4aFO8) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
