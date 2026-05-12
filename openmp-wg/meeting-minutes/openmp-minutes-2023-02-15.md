### 2023, Feb 15

Agenda

  * Remove old plugins: ~ end of Feb
  * Short talk on implementing RPC in LibC


  * [https://docs.google.com/presentation/d/1uLDPBtTVCHucedIohCPpH0IaP8FceKZYSx7N8FsuZk8](https://www.google.com/url?q=https://docs.google.com/presentation/d/1uLDPBtTVCHucedIohCPpH0IaP8FceKZYSx7N8FsuZk8&sa=D&source=editors&ust=1778600246178462&usg=AOvVaw3GiwNyj520nHHQU5tsGe_L)


  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246178600&usg=AOvVaw1OJk1vBSkX6MtfP4iHGWpV) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246178718&usg=AOvVaw3MFzvX0eCdQxDghywXm_ZY) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246178819&usg=AOvVaw3tVOcgTLh2UdkbQy_gPWxs) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246179318&usg=AOvVaw20O2a_Gdy4IzJYQjKbRk4I)


  46. Allocate "all" device memory
  47. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  48. Replay -> load image + user allocated memory, launch with argos and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246179680&usg=AOvVaw0fgHkACTJtv7BYbuOfuFTN)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246179759&usg=AOvVaw0zTNQUjx39omtdT1UeohU8)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246179983&usg=AOvVaw2LWLG_d-z506RHYMe9zdBu)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246180240&usg=AOvVaw1S-7BMhWSUWqBpYQzdkgBy) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246180399&usg=AOvVaw3b1dqlR3JQvGgabjFeNVoR)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246180640&usg=AOvVaw2wskBNxt73GUa9wituPCfO) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246180730&usg=AOvVaw37n0idGtULCGOWOYOXvojT)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246180862&usg=AOvVaw3ibMcmhOmQfY5BLgqEWcQt)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246181566&usg=AOvVaw38FjCOdC7guXVuKdoX1Y0Z)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246181742&usg=AOvVaw1ZledsE_AYHQw-bC1a8FJP)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246181849&usg=AOvVaw2KojmY4TWNKlk99LT1eFJs) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246182001&usg=AOvVaw1DSLzuTLipMsSOZIzI-9lv) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246182518&usg=AOvVaw1tVuy6Ti562-KIjx8682WS) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246182687&usg=AOvVaw1qeB_iUJcXKTiopBvwfF2y) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246182887&usg=AOvVaw39fakcXEcvV0gbOHDmnzUT)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246183080&usg=AOvVaw0TTL1iEZ177OhpJPwFa0vP)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246183242&usg=AOvVaw1--ITh2a6biTEsDLtGz4e3): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246183455&usg=AOvVaw1UT0EZ0BO04GrU2rqTGaZ8) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
