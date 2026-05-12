### 2023, june 07

Agenda

New 

  * Libm for the GPU


  * Easiest solution is to use the `libc` infrastructure and remap calls to the existing device libs
  * E.g. -Xclang -mlink-builtin-bitcode -Xclang libdevice.10.bc
  * Can we redistribute NVIDIA's libdevice?


  * Artem from Google is asking for this and an MLIR project, license seems to suggest so


  * The answer is "yes"


  * Exporting the RPC interface from libc


  * [[libc] Begin implementing a library for the RPC server](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246071504&usg=AOvVaw2P3uRyOb1hBr9_g9t6wZtQ)
  * [[libc] Export GPU extensions to `libc` for external use](https://www.google.com/url?q=https://reviews.llvm.org/D152283&sa=D&source=editors&ust=1778600246071618&usg=AOvVaw1QYnJgCL30V78OUnI_f5Jp)


  * Moving the AMDGPU libc build bot to staging


  * [https://lab.llvm.org/staging/#/builders/247](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/247&sa=D&source=editors&ust=1778600246071794&usg=AOvVaw3yj5lTv10pOcmX453e1A8Y)


  * Leftover runtime "state" down to 1 element (for simple kernels)
  * Lightweight Attributor under review -> Attributor compile time reduction under development
  * Flang OpenMP offload is making nice progress (thanks to AMD)



Previous

  *  Implementing the device runtime in a separate project


  * Some complains about the project / runtimes handling


  * Remove keep alive functionality in OpenMP [https://reviews.llvm.org/D151324](https://www.google.com/url?q=https://reviews.llvm.org/D151324&sa=D&source=editors&ust=1778600246072352&usg=AOvVaw2lITgZ4bqixSyDcfhTTFM5)


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
  * OpenMP version change
  * Bump up GCC requirement for libomp?
  * Summary of OpenMP F2F (Deepak) 
  * LibC Status


  * [[libc] Enable multiple threads to use RPC on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D148943&sa=D&source=editors&ust=1778600246073362&usg=AOvVaw2i5zY-IOuxlq3eNqiqXX-R)
  * [[libc] Support concurrent RPC port access on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D149598&sa=D&source=editors&ust=1778600246073481&usg=AOvVaw1cUHxVZCSxqu5lp1ovgf7g)
  * [[libc] Enable running libc unit tests on AMDGPU](https://www.google.com/url?q=https://reviews.llvm.org/D149517&sa=D&source=editors&ust=1778600246073586&usg=AOvVaw2hVWozewekkIp0yz-lCTyt)
  * [[libc] Enable running libc unit tests on NVPTX](https://www.google.com/url?q=https://reviews.llvm.org/D149532&sa=D&source=editors&ust=1778600246073688&usg=AOvVaw1nMtehOgGg7jS4GPYW11PC)
  * Nvidia buildbot: [https://lab.llvm.org/buildbot/#/builders/46](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/46&sa=D&source=editors&ust=1778600246073809&usg=AOvVaw2oVh4jKlqud7Yd_SOkGDAf)
  * AMDGPU buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246073942&usg=AOvVaw2YWQoW1w0jAzvhhTq-95Iy)
  * Presentation [LibC for GPUs](https://www.google.com/url?q=https://docs.google.com/presentation/d/1jQ5uoWtTv-esba-aUJSRxsCKoeha_VOtYO1u2XkeCqc/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246074062&usg=AOvVaw1sbzdtXyUoiAVK3vufY0WV)


  * Reverse offloading proof of concept demo
  * [https://github.com/jhuber6/OpenMP-reverse-offloading](https://www.google.com/url?q=https://github.com/jhuber6/OpenMP-reverse-offloading&sa=D&source=editors&ust=1778600246074271&usg=AOvVaw3GBpvpgHDWbhPD0LvEy6ZH)Switch current "experimental" AMDGPU OpenMP Runtime buildbot to production and move the current "production" buildbot into staging


  * Experimental buildbot does make check-openmp, check-clang, check-llvm, check-lld, check-libc
  * Production buildbot: [https://lab.llvm.org/buildbot/#/builders/193](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193&sa=D&source=editors&ust=1778600246074606&usg=AOvVaw0bE37B_KZGg3k0l79QJpu9)
  * Experimental buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246074734&usg=AOvVaw0bKjtDDxIMcltCRnIKZYvh) 


  *   * One SPEC HPC C/C++ test is still not working on Frontier, five are running now.
  * AMD signal active waiting[ https://reviews.llvm.org/D148808](https://www.google.com/url?q=https://reviews.llvm.org/D148808&sa=D&source=editors&ust=1778600246074991&usg=AOvVaw2uOi0tA3-8n7rGZqUCciUF)How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246075149&usg=AOvVaw2061o7j2tVa7FKqj0T8Myq)
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246075283&usg=AOvVaw1qxWS9qBJm0byeFnotWPNB)


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246075449&usg=AOvVaw1SuT8QVe4MxaOba1Kl1q5u)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246075778&usg=AOvVaw2on6S2_dQvHYRZddRvzDTo)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246075882&usg=AOvVaw1DejZJW60oXlSuKGtAc_LN)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246075974&usg=AOvVaw1ucY_lXKkAW1BGxiHNR47a)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246076151&usg=AOvVaw1frbzRgnbpgjOt8oh6pgOH) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246076281&usg=AOvVaw0bV-mvJiXZ8oeJ4XIeJkMK) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246076384&usg=AOvVaw0gCaokSnX79TmzyT5M_J5Z) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246076877&usg=AOvVaw1KyJpRlf4ySQHxs7lI9QmE)


  4. Allocate "all" device memory
  5. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  6. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246077256&usg=AOvVaw1g1erSUAZkFAxAq2tCMA3w)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246077359&usg=AOvVaw1W6nt9_qbgt1uunkK1meQT)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246077576&usg=AOvVaw0Ro7HYbmt8vY-LgG685R7_)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246077831&usg=AOvVaw0ApGnyckJlJShF3BJcB95L) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246077998&usg=AOvVaw04iDAu9hQIsS7fCFDy8T4t)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246078234&usg=AOvVaw1cRD2mpzoR4NCBCmkF5jQU) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246078334&usg=AOvVaw3mwQFdQiv2nM0IAZfnperp)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246078469&usg=AOvVaw0SBYaPO1QhgtiAcMv24LwL)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246079134&usg=AOvVaw0fRm2AnnYatKeo-IEoxyov)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246079312&usg=AOvVaw2FkGZg80qdoHFWw7LcB2LA)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246079411&usg=AOvVaw1Xq8aO0P2ua7B8Err96_Zg) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246079566&usg=AOvVaw1-U5R0Aq-ci7Jp7KGHKGVb) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246080083&usg=AOvVaw0fMCv71j6MTUmyioPR9Sug) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246080288&usg=AOvVaw34d7r3oBDB_ZhbZa19vTcN) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246080499&usg=AOvVaw3hQ5rYKTbeg3aq3yCEUQR0)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246080680&usg=AOvVaw341ARamWBFC02r56lSr4bk)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246080828&usg=AOvVaw2kzqTsvAk2diLus9EmXJd0): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246081012&usg=AOvVaw1kL--qXpv-9QerA3GmBvMd) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
