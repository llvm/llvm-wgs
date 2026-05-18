### 2022, Nov 30

Agenda

  * NextGen AMD Plugin


  * Jan-Patrick is testing it
  * Latest status: [https://github.com/kevinsala/llvm-project/tree/develop](https://www.google.com/url?q=https://github.com/kevinsala/llvm-project/tree/develop&sa=D&source=editors&ust=1778600246233591&usg=AOvVaw1RztrPvUAg260groHvUiz3) 


  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)
  * 

  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246234132&usg=AOvVaw3_SZAEZYE8J5K4qRdPJck_)) 


  73. Allocate "all" device memory
  74. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  75. Replay -> load image + user allocated memory, launch with argos and parameters


  * New meeting time for Jan 23, when2meet?
  *   * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246234561&usg=AOvVaw1fcyVVt5Gj9CZcfdmJauzx)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246234639&usg=AOvVaw19Vg4ZN_Fj6pVo8-ZqCBRR)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246234865&usg=AOvVaw1_G31yACNAkQ0AeCjr9-3k)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246235137&usg=AOvVaw0Q_MJbwipUtbquj0Hem2cR) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246235290&usg=AOvVaw1yFOflr_8RiQubzbyakQTE)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246235440&usg=AOvVaw0mEkX9lUeEleLIyPcbqyTl)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246235669&usg=AOvVaw3utK1HJEOuFPGuAmqm_htw) 


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246235777&usg=AOvVaw06rEzBXyPuylcZ6DhXbMO1)
  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246235878&usg=AOvVaw1TFXO6nZ4MPJFXTE0UuGAf)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246236012&usg=AOvVaw1en-UAbntL3S-qvc_yo5oc)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246236683&usg=AOvVaw0pQIrVG_mNPhaINtf3KKqC)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246236870&usg=AOvVaw0HtnTiaSKV0YfBv3qI6cvD)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246236980&usg=AOvVaw2Lqx5j6PixtK1JHzjK6Nwm) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246237138&usg=AOvVaw3veaIpjasbwrHzaReC_d97) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246237655&usg=AOvVaw2vbn-YXTF0Tvq0NpgUEfDu) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246237837&usg=AOvVaw2A4svZ65E5zw6Hnb61qCt6) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246238042&usg=AOvVaw1Jo-FeCfDZfCL_tJ-rmj5t)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246238230&usg=AOvVaw1b4NXb4wAAWFJWZRZL9K5y)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246238387&usg=AOvVaw3pK1KCHy04BxlyPqeW9Ovo): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246238586&usg=AOvVaw3YOYLVU0KrYYzfDZGGE12k) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
