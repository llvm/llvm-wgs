### 2023, Mar 01

Agenda

  * More info for kernel launches w/ AMDGPU: [https://reviews.llvm.org/D144521](https://www.google.com/url?q=https://reviews.llvm.org/D144521&sa=D&source=editors&ust=1778600246165108&usg=AOvVaw034epE0uUU_lpVWpqtdXIu)
  * Firstprivate variables are passed by-ref if its alignment is greater than alignof(uintptr_t)


  * [https://godbolt.org/z/6jPvMvsxh](https://www.google.com/url?q=https://godbolt.org/z/6jPvMvsxh&sa=D&source=editors&ust=1778600246165308&usg=AOvVaw1h2n_-9skISQa5w9hAUbYU)
  * Shouldn't we be able to pass this by-value
  * [https://godbolt.org/z/sPbE3aP7n](https://www.google.com/url?q=https://godbolt.org/z/sPbE3aP7n&sa=D&source=editors&ust=1778600246165458&usg=AOvVaw2ZBxRsw9rcnA11EN4xRgkb) <\- 64 aligned load is emitted (w/o by-value) (line 262)


  * Status of omp loop directive?


  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246165639&usg=AOvVaw24UYSaWlBz68k-egONtsZE) 


  * Proposal to break non-globally installed clang openmp, [https://reviews.llvm.org/D143306](https://www.google.com/url?q=https://reviews.llvm.org/D143306&sa=D&source=editors&ust=1778600246165790&usg=AOvVaw1t9PEFVfNRQIl2uEf5P7r_)


  * Specifically, stop setting rpath because fedora don't like it, thus openmp programs won't find openmp libraries, and they'll refuse to run. Unless people set LD_LIBRARY_PATH or mess around with the linker themselves, but that'll closely approximate people trying openmp and concluding that it's just broken and giving up
  * It seems there's a configuration file alternative functionality in clang, though I can't see how that could fix things unless it also sets rpath, in which case why would fedora be ok with it? But whatever, the consensus in D143306 is going against me, so if we _don't_ want openmp to stop working from local installs on llvm-16, please speak up


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246166547&usg=AOvVaw3mECZhtTF0fuDi03skApgL)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246166862&usg=AOvVaw2taiU6hWsd9eGFZb0ft_pG) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246166988&usg=AOvVaw1B1UaoMc4JwSSC6D3RW21p) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246167091&usg=AOvVaw3viDgF-xwCKHiNr4Z0ZbxF) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246167603&usg=AOvVaw1tGFtpdH8B9qWxraSJVNmL)


  40. Allocate "all" device memory
  41. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  42. Replay -> load image + user allocated memory, launch with argos and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246167967&usg=AOvVaw14N_CIJJOhe2tzdc9S1Zre)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246168047&usg=AOvVaw3G5eqAwUevopA467emnT9D)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246168286&usg=AOvVaw1mj8ORJLrWhMkWahTFX8fv)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246168552&usg=AOvVaw0Gr7nDupbjmFROK_gcpG20) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246168710&usg=AOvVaw08PBgkzIV5thKRkK3Pyi1g)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246168955&usg=AOvVaw2w8jqoqEq7tIHrwT59KxOA) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246169048&usg=AOvVaw1MTxLKBqZcMVbjnuvH_HXl)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246169193&usg=AOvVaw25OoU2gn4CnXjclHtG2B2S)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246169862&usg=AOvVaw2SkVDpiAmAWFXfMssKjUV6)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246170032&usg=AOvVaw3uxE9svhUCMWqE92lKq6OB)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246170142&usg=AOvVaw3AKmr5M7jjvW3XQKRfa7ic) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246170333&usg=AOvVaw2YPkBm_vlytVSPSt_6-IJX) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246170873&usg=AOvVaw0-M-jJBFTRthiABPFdaxh6) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246171044&usg=AOvVaw2hDqWTBZXufyOLCw_hFipz) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246171256&usg=AOvVaw1yiS5WkOk_zXYtbkEjomT-)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246171450&usg=AOvVaw0z5PUSUD1PP-cR-xaLZRTd)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246171629&usg=AOvVaw0H9DTsTlmfkeOelUcHUFmn): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246171822&usg=AOvVaw10A5AF3-tggLx9M8c-DKAH) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
