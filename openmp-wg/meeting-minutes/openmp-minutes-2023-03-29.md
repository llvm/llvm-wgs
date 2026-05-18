### 2023, Mar 29

Agenda

  * OpenMP asynchronous memory copy support


  * Not sure if this fully respects the spec: "The value of num_dims must be between 1 and the implementation-defined limit, which must be at least three." and "An application can determine the number of inclusive dimensions supported by an implementation by passing NULL for both dst and src. The routine returns the number of dimensions supported by the implementation for the specified device numbers. No copy operation is performed."
  * [https://reviews.llvm.org/D136103](https://www.google.com/url?q=https://reviews.llvm.org/D136103&sa=D&source=editors&ust=1778600246137101&usg=AOvVaw1Wgyhbe-nC7kN_Q0x9Tuuv) 


  * Expand  RPC support in libc
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246137288&usg=AOvVaw1sTF2EAX07IoPeCk8hSB4E)


  * Status of omp loop directive?


  * Reduction on Loop constructs.  Is it supported
  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246137487&usg=AOvVaw0nxgD0h3-W5aRsoxEvsNez) 
  * [https://reviews.llvm.org/D145823](https://www.google.com/url?q=https://reviews.llvm.org/D145823&sa=D&source=editors&ust=1778600246137578&usg=AOvVaw1fhcuXdSrw59pAB4CS9dHD) 


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246137742&usg=AOvVaw1RMEJiTWNKGd9p7NVirT6L)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246138058&usg=AOvVaw1_KWKr-a8IcXsRjFhipBdC)
  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246138181&usg=AOvVaw3eZCNuS5XfzxRxh9yUo9av)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246138278&usg=AOvVaw2ngE8g1Qp26e1XkRH8scSN)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246138378&usg=AOvVaw336vt3NCMz94wteBELpEyO)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246138555&usg=AOvVaw3yP9h6SbkkYkVByGVZHH7z) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246138673&usg=AOvVaw07QV-F-Gei80e5TjtJFYkO) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246138773&usg=AOvVaw1wqcNYWCOwntHv5PnMi2Ee) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246139279&usg=AOvVaw3miZlGXhT6O4OkypxLDdAS)


  28. Allocate "all" device memory
  29. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  30. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246139636&usg=AOvVaw2jhciAK2fBvNJqHwFGtwMD)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246139723&usg=AOvVaw35BI6g9O3ViJ70jFMgsCcs)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246139937&usg=AOvVaw2a06Zamx-bh2dcg0o_t-fb)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246140193&usg=AOvVaw2UjDJpCkGmUrRqL04R4SQ_) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246140361&usg=AOvVaw3rBFsJBPdWN07iUiWPVZ4h)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246140782&usg=AOvVaw15SPS-Y0BlTpVqalJ6V43B) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246140912&usg=AOvVaw2onrQg4f4dVhwzHsogFP6N)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246141064&usg=AOvVaw3wNY-IHNXXhgbKDiCLqgfg)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246141745&usg=AOvVaw1xSqvSgqbOyqhszFW5QMuf)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246141916&usg=AOvVaw2NZiORfsUKTaesQpe3qOq5)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246142027&usg=AOvVaw3L4VSoOU1A466X4I4QZ9EH) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246142186&usg=AOvVaw0CQwYy4JTSopCWIfjiKIe9) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246142694&usg=AOvVaw0UPlmZWtg-MYRyJVBvvu85) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246142918&usg=AOvVaw1wSSi1GSwvhL7dCwkZqNA4) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246143142&usg=AOvVaw0w05wJeo1ySfwz8bzTIQsL)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246143329&usg=AOvVaw18OqiaVvbCeUoAMO-X1rbH)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246143493&usg=AOvVaw1VT4kh6v9fC6x-rT0lzG1-): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246143676&usg=AOvVaw3W028XoDQ6LYabtZF6bQa7) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
