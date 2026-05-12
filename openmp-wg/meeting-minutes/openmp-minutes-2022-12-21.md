### 2022, Dec 21

Agenda

  * When 2 meet next: [https://www.when2meet.com/?18056590-SQ9TR](https://www.google.com/url?q=https://www.when2meet.com/?18056590-SQ9TR&sa=D&source=editors&ust=1778600246214660&usg=AOvVaw0wsBBRIB2EDY_va47-XM3T) 
  * AMDGPU spill patch (reverted: [https://reviews.llvm.org/D124196#4007017](https://www.google.com/url?q=https://reviews.llvm.org/D124196%234007017&sa=D&source=editors&ust=1778600246214795&usg=AOvVaw2VoD-8d2XX5A8BYJYv5Fyx)) 
  * LIT will require Python 3 soon [https://reviews.llvm.org/D139855](https://www.google.com/url?q=https://reviews.llvm.org/D139855&sa=D&source=editors&ust=1778600246214923&usg=AOvVaw3JWVAe_59jTyaBtSqwu1Nv)
  * Meetings during holidays  Dec 28th meeting canceled.
  * OpenMP-opt slack:


  * [https://join.slack.com/t/openmp-opt/shared_invite/zt-1ktv8h0wx-6Ks4PjL3qnx8dhC9Nx4fgg](https://www.google.com/url?q=https://join.slack.com/t/openmp-opt/shared_invite/zt-1ktv8h0wx-6Ks4PjL3qnx8dhC9Nx4fgg&sa=D&source=editors&ust=1778600246215199&usg=AOvVaw0OOIGf-AeGCptdF1ArshoO) 


  * Pinned memory:


  * ½ [https://reviews.llvm.org/D138933](https://www.google.com/url?q=https://reviews.llvm.org/D138933&sa=D&source=editors&ust=1778600246215334&usg=AOvVaw2l35HS4S9F1F83TvwA1TLm)
  * 2/2 [https://reviews.llvm.org/D139208](https://www.google.com/url?q=https://reviews.llvm.org/D139208&sa=D&source=editors&ust=1778600246215442&usg=AOvVaw3hGSPqurwOnUnIgpNAGYp0) 


  * NextGen AMD Plugin


  * Jan-Patrick is testing it
  * Latest status: [https://github.com/kevinsala/llvm-project/tree/develop](https://www.google.com/url?q=https://github.com/kevinsala/llvm-project/tree/develop&sa=D&source=editors&ust=1778600246215670&usg=AOvVaw0-P-NxsCnR5GCvvLnLU2pE) 
  * Landed


  * Adding support for `--offload-arch=native`


  * Autodetects the GPU architecture


  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246216303&usg=AOvVaw0XRz2zlU2tgbhHlKsu0zqK)) 


  64. Allocate "all" device memory
  65. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  66. Replay -> load image + user allocated memory, launch with argos and parameters


  * New meeting time for Jan 23, when2meet?
  *   * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246216725&usg=AOvVaw1nY6_cvlZd2ngowbZk0dYC)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246216803&usg=AOvVaw3KTNN7tgUJccSdvbnHaTIi)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246217054&usg=AOvVaw2G8LEv0YhbZtLzPKn0z21i)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246217329&usg=AOvVaw0defcz8SYhCSDrnzk6_9X-) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246217474&usg=AOvVaw1pS8CBCUYaHzlFydDQOawv)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246217623&usg=AOvVaw0x_EyvchrkCrRgNaoHl7XK)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246217858&usg=AOvVaw2SdGVVhqBpZeVuKTw2Mw6O) 


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246217966&usg=AOvVaw3iZLHQW5CFvRFFoewrqfYH)
  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246218066&usg=AOvVaw0JFQGQch-FWqFD9ruIgtoQ)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246218218&usg=AOvVaw0u9KAl295u-p8NbvY9U3bo)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246218897&usg=AOvVaw1TSYYGP0uFLAJbFHMuDgaA)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246219101&usg=AOvVaw3og6UPAaWVwT6w1-y2NADE)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246219219&usg=AOvVaw3D3DM6-PaZaBLWqgUNpKy-) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246219380&usg=AOvVaw0ttPvPhqVIrd4I8osyJeKq) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246219932&usg=AOvVaw1TWxIsNDajDZQZihyDzLKw) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246220095&usg=AOvVaw1W3MF7O35IWMS1t2t5fZu3) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246220307&usg=AOvVaw0-qX9HvWCcH5rSryx1N537)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246220490&usg=AOvVaw1JUy8qYJFYmB1VXQQvmKra)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246220652&usg=AOvVaw2-8lnM8sjKi-F77sTsB5X3): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246220832&usg=AOvVaw1fuwWLSrk2dfodpprAz90I) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246221139&usg=AOvVaw3pZ7mTGGKEZ9jP63Twsybo) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246221262&usg=AOvVaw1B5SGZbIu7QPmi47bWLxF7)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246221373&usg=AOvVaw1-qeh-1ffp590HAxooX7aY)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246221488&usg=AOvVaw3c0pY4mB6v0obYMWTzn3A-)



opencl

###
