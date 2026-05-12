### 2023, May 17

Agenda

New 

  *    LibC Status


  * [[libc] Enable multiple threads to use RPC on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D148943&sa=D&source=editors&ust=1778600246098900&usg=AOvVaw0MKacILqTL4YjiEuUv9VUQ)
  * [[libc] Support concurrent RPC port access on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D149598&sa=D&source=editors&ust=1778600246099012&usg=AOvVaw2C96YWDdGHjirwusEOAQ-7)
  * [[libc] Enable running libc unit tests on AMDGPU](https://www.google.com/url?q=https://reviews.llvm.org/D149517&sa=D&source=editors&ust=1778600246099126&usg=AOvVaw2Gb8eOaHiyCJZTGUonh1NO)
  * [[libc] Enable running libc unit tests on NVPTX](https://www.google.com/url?q=https://reviews.llvm.org/D149532&sa=D&source=editors&ust=1778600246099238&usg=AOvVaw1EGONjGUXzOw07dA06mr5i)
  * Nvidia buildbot: [https://lab.llvm.org/buildbot/#/builders/46](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/46&sa=D&source=editors&ust=1778600246099360&usg=AOvVaw26EiV-jT2zVJDB5ZLwvFJ5)
  * AMDGPU buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246099489&usg=AOvVaw2nRJ_6UD8vAN9kgosvep1t)
  * Presentation [LibC for GPUs](https://www.google.com/url?q=https://docs.google.com/presentation/d/1jQ5uoWtTv-esba-aUJSRxsCKoeha_VOtYO1u2XkeCqc/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246099606&usg=AOvVaw1RXxCa-XQsLNj4IZels9Ya)


  * Reverse offloading proof of concept demo


  * [https://github.com/jhuber6/OpenMP-reverse-offloading](https://www.google.com/url?q=https://github.com/jhuber6/OpenMP-reverse-offloading&sa=D&source=editors&ust=1778600246099778&usg=AOvVaw3l46MO4xZ7x6y3NiMoej09)



Previous

  * Switch current "experimental" AMDGPU OpenMP Runtime buildbot to production and move the current "production" buildbot into staging


  * Experimental buildbot does make check-openmp, check-clang, check-llvm, check-lld, check-libc
  * Production buildbot: [https://lab.llvm.org/buildbot/#/builders/193](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193&sa=D&source=editors&ust=1778600246100183&usg=AOvVaw1_JD0C56RSm_La11L7s_Z_)
  * Experimental buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246100319&usg=AOvVaw3Zifkr0-MMDn9NDXwsXYGg) 


  *   * One SPEC HPC C/C++ test is still not working on Frontier, five are running now.
  * AMD signal active waiting[ https://reviews.llvm.org/D148808](https://www.google.com/url?q=https://reviews.llvm.org/D148808&sa=D&source=editors&ust=1778600246100554&usg=AOvVaw3PjpnN7InwhFgJT-XArDPJ)How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246100697&usg=AOvVaw3-lIvekZ46AJop8s2BcqM0)
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246100830&usg=AOvVaw07-lm9DIQJdKAefC1x2_SB)


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246100992&usg=AOvVaw1KehDBahYMlD6wYFEXgN3b)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246101370&usg=AOvVaw2DPpIinx5Z16dV5uOQcrb-)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246101468&usg=AOvVaw1UY4S7MgcI33aQH_TRBISo)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246101559&usg=AOvVaw36rj2XRCUFNenccyvNd_Sn)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246101743&usg=AOvVaw10l5dGwEhxgLgEz8Oxaw08) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246101865&usg=AOvVaw02095D6AyKnrH5CllcRrbe) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246101969&usg=AOvVaw3nd5aPC-i1Ofs8DlR811aB) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246102474&usg=AOvVaw1E9d0bYtYhnKaJoof9mqv0)


  13. Allocate "all" device memory
  14. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  15. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246102827&usg=AOvVaw0TWv4qTrJlYdgyoMcxw-vX)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246102908&usg=AOvVaw3IUREBt8VF2xMubsTVFEbO)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246103130&usg=AOvVaw0p4fPaubksQi-o5Ku-M_mb)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246103393&usg=AOvVaw1GcupK7EZaH1-uQXxO62e-) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246103558&usg=AOvVaw36WKFE3Fn_1xlsGe6ItyaV)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246103792&usg=AOvVaw31VI7yDHXAzyHHvLnL8Cyn) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246103891&usg=AOvVaw2VHKhdQoxt7x-VIqpjifD0)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246104027&usg=AOvVaw0mIJgDtQ3M1rJKFnB5_4t4)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246104695&usg=AOvVaw2n1ojyBeEKQ-ZSngu4yEEp)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246104889&usg=AOvVaw3zQY0NyvoHM8Kwh32JAahv)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246104987&usg=AOvVaw0vQMCpzPz8vYZY2pnBzS7A) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246105143&usg=AOvVaw3N6U-rg2Ts3ehMDoYJd_zB) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246105659&usg=AOvVaw3Q1adjh9nIhsHSk69Wde3N) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246105819&usg=AOvVaw2vrAZdDbwt7axnTynAus0t) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246106029&usg=AOvVaw1TJMrrP2LcEhYsujFIiK5i)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246106216&usg=AOvVaw0nWJKthCNLA8zZpDENySBP)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246106377&usg=AOvVaw34avg7Y-_5v7cTXY2ACtHh): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246106557&usg=AOvVaw1mEm3KbQF30_YikwoBfUjN) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
