### 2023, Feb 22

Agenda

  * More info for kernel launches w/ AMDGPU: [https://reviews.llvm.org/D144521](https://www.google.com/url?q=https://reviews.llvm.org/D144521&sa=D&source=editors&ust=1778600246172158&usg=AOvVaw1ozxNxet0EDddEHxgLMUGG) 
  * Proposal to break non-globally installed clang openmp, [https://reviews.llvm.org/D143306](https://www.google.com/url?q=https://reviews.llvm.org/D143306&sa=D&source=editors&ust=1778600246172310&usg=AOvVaw3n-NafSB_vrJlbxPWWZ3op)


  * Specifically, stop setting rpath because fedora don't like it, thus openmp programs won't find openmp libraries, and they'll refuse to run. Unless people set LD_LIBRARY_PATH or mess around with the linker themselves, but that'll closely approximate people trying openmp and concluding that it's just broken and giving up
  * It seems there's a configuration file alternative functionality in clang, though I can't see how that could fix things unless it also sets rpath, in which case why would fedora be ok with it? But whatever, the consensus in D143306 is going against me, so if we _don't_ want openmp to stop working from local installs on llvm-16, please speak up


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246173065&usg=AOvVaw3AoO-QuQ6o623Aw2gmxokg) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246173199&usg=AOvVaw3LlMjQcEBSLRGom2N3d9dk) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246173303&usg=AOvVaw0TTYrVKmLcpSsTz2GLr2-V) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246173795&usg=AOvVaw14Wa_9yRyVWJ_S1JD5pelG)


  43. Allocate "all" device memory
  44. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  45. Replay -> load image + user allocated memory, launch with argos and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246174159&usg=AOvVaw0o40SUsYmXyhYbT9iyvqkb)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246174250&usg=AOvVaw3NtavYv4OiWDdTP0fOr-ZK)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246174468&usg=AOvVaw06u7aUQuvvv3h99QuB4Lj0)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246174722&usg=AOvVaw2789_ybMBNUYoll1i-ywME) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246174876&usg=AOvVaw34DXRw9_zTsMSRYswozOpO)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246175107&usg=AOvVaw2ZmPG3ykfTfYJ1hkp6znm_) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246175214&usg=AOvVaw3eA1t-75VVKDn1-PBrAOOC)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246175349&usg=AOvVaw23dwctqRtAKa3qTe3qWRz9)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246176057&usg=AOvVaw18yw-x_7nV2GBZwQWWM54P)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246176272&usg=AOvVaw3Cw2AB-IivDrKXW88yJ5GC)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246176375&usg=AOvVaw3sFws59nm3JZ9z92aBxXyh) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246176535&usg=AOvVaw28ZGc_1jkez3yxw3YWY703) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246177070&usg=AOvVaw0NS8zoZOIQv1gVWnUigRIf) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246177250&usg=AOvVaw38i6tyrbY0Jodp_Gm4KoG2) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246177455&usg=AOvVaw1uNTgcVEfItKVyrpWS4HKr)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246177636&usg=AOvVaw1FTnq-OsBjYaHWT9C53lmK)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246177819&usg=AOvVaw2646GalzwTDzk2aXMoqm7J): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246178005&usg=AOvVaw3ZeNXgGckeO7oJEghd1oM2) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
