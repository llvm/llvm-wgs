### 2023, May 31

Agenda

New 

  *  Implementing the device runtime in a separate project


  * Some complains about the project / runtimes handling


  * Remove keep alive functionality in OpenMP [https://reviews.llvm.org/D151324](https://www.google.com/url?q=https://reviews.llvm.org/D151324&sa=D&source=editors&ust=1778600246081539&usg=AOvVaw0MJkyJrYdiOWH6DUCAp_Aa)


  * Used to be required to keep RTL functions alive
  * We unconditionally link the library late now which should prevent this from happening


  * Libm for the GPU


  * Easiest solution is to use the `libc` infrastructure and remap calls to the existing device libs
  * E.g. -Xclang -mlink-builtin-bitcode -Xclang libdevice.10.bc
  * Can we redistribute NVIDIA's libdevice?


  * Artem from Google is asking for this and an MLIR project, license seems to suggest so


  * Integrating the libc RPC implementation into OpenMP


  * How to do this?
  * Header only library, but exposes libc internals


  * Goals for LLVM 17 release?



Previous

  * OpenMP version change
  * Bump up GCC requirement for libomp?
  * Summary of OpenMP F2F (Deepak) 
  * LibC Status


  * [[libc] Enable multiple threads to use RPC on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D148943&sa=D&source=editors&ust=1778600246082637&usg=AOvVaw3ZA2y8y4RVY57470mA0SF0)
  * [[libc] Support concurrent RPC port access on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D149598&sa=D&source=editors&ust=1778600246082762&usg=AOvVaw2uujAj7yIim9q3yhwbfXkm)
  * [[libc] Enable running libc unit tests on AMDGPU](https://www.google.com/url?q=https://reviews.llvm.org/D149517&sa=D&source=editors&ust=1778600246082870&usg=AOvVaw39Gn37nxxS_xigmuwhFxEX)
  * [[libc] Enable running libc unit tests on NVPTX](https://www.google.com/url?q=https://reviews.llvm.org/D149532&sa=D&source=editors&ust=1778600246082979&usg=AOvVaw29nkK25TSmWMRONz8ZPdMN)
  * Nvidia buildbot: [https://lab.llvm.org/buildbot/#/builders/46](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/46&sa=D&source=editors&ust=1778600246083114&usg=AOvVaw1g1G8yuv_3raRia6hMByWp)
  * AMDGPU buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246083240&usg=AOvVaw3wlWFSkOF7U_PK8yj2CUSJ)
  * Presentation [LibC for GPUs](https://www.google.com/url?q=https://docs.google.com/presentation/d/1jQ5uoWtTv-esba-aUJSRxsCKoeha_VOtYO1u2XkeCqc/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246083365&usg=AOvVaw2FPQ53qQpfqQx3lOxk2cRd)


  * Reverse offloading proof of concept demo
  * [https://github.com/jhuber6/OpenMP-reverse-offloading](https://www.google.com/url?q=https://github.com/jhuber6/OpenMP-reverse-offloading&sa=D&source=editors&ust=1778600246083534&usg=AOvVaw37yG7d8XQaXSsON8tffiHF)Switch current "experimental" AMDGPU OpenMP Runtime buildbot to production and move the current "production" buildbot into staging


  * Experimental buildbot does make check-openmp, check-clang, check-llvm, check-lld, check-libc
  * Production buildbot: [https://lab.llvm.org/buildbot/#/builders/193](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193&sa=D&source=editors&ust=1778600246083864&usg=AOvVaw386t2dKuU1zWlx8t3ZXTrX)
  * Experimental buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246083992&usg=AOvVaw0ENNgdBh7We8lPja2pZK4m) 


  *   * One SPEC HPC C/C++ test is still not working on Frontier, five are running now.
  * AMD signal active waiting[ https://reviews.llvm.org/D148808](https://www.google.com/url?q=https://reviews.llvm.org/D148808&sa=D&source=editors&ust=1778600246084246&usg=AOvVaw00Yvt_OUsRq7KK3ImbQEgB)How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246084391&usg=AOvVaw1-EAF3FswiZ3ed8pzER30q)
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246084526&usg=AOvVaw1GIlVhP4GhyoSDm8WF1VNl)


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246084716&usg=AOvVaw3aK4GmuC8dfDOOe9RYN8mx)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246085041&usg=AOvVaw1miSJQPSS-IGeP8ppJ661N)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246085158&usg=AOvVaw1obuJOMWy_B_W-MXLpyDy2)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246085250&usg=AOvVaw2KVzAAGuVEvYanU0MB64YE)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246085430&usg=AOvVaw1aKqGuLmiDyZ5Rj0igpB1A) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246085550&usg=AOvVaw0XXi5BaXOMHGXVq8W7BYlB) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246085652&usg=AOvVaw1jOmGMEOVGKL7kUlSodaha) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246086195&usg=AOvVaw1R091_ZIxBt7J_u1nvjBhq)


  7. Allocate "all" device memory
  8. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  9. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246086583&usg=AOvVaw0m-O1m91ikjCu2FswQPDrU)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246086673&usg=AOvVaw2oauUKcmV0bbpYBvI9CnVD)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246086900&usg=AOvVaw0FyEow0v61emckIEres2M8)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246087172&usg=AOvVaw2L1GT89pIxLRU1CNjEKBLx) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246087340&usg=AOvVaw3-xjwL2wTfP0xhntJobbPA)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246087573&usg=AOvVaw1SIAOacoVWidmBerPqxmel) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246087666&usg=AOvVaw29JfTVYTnuQM31MN2JEa92)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246087808&usg=AOvVaw0s0kHh-6KK6I2YTr4Ekuj3)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246088488&usg=AOvVaw0pSlS4w-T3eIgetOPJNM8S)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246088661&usg=AOvVaw0tazwNAoBcgzR-d2kMWVKQ)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246088758&usg=AOvVaw157tNj1RX2rUYsRdAX5uAB) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246088908&usg=AOvVaw3GRbjU5BrFtc3ngRBJ0bI-) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246089433&usg=AOvVaw1XUCM9np5TkZ_UpL9_Ayxr) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246089601&usg=AOvVaw2wuLBhs52y1IvXsKgf9jaO) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246089807&usg=AOvVaw0zgT6ieig19ca6l1uJdhrY)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246089987&usg=AOvVaw31qrKINW4HXpPk9ILzDP04)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246090151&usg=AOvVaw1xW9hviI0OIC2v7mslg8tZ): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246090340&usg=AOvVaw0Z_mDz4FTMF43sScIQ4Rk4) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
