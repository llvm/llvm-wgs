### 2023, Jan 11

Agenda

  * When 2 meet next: [https://www.when2meet.com/?18056590-SQ9TR](https://www.google.com/url?q=https://www.when2meet.com/?18056590-SQ9TR&sa=D&source=editors&ust=1778600246202847&usg=AOvVaw1N0Fuem2OvAqtAf7WRJwpH) 
  * New kernel launch API: [https://reviews.llvm.org/D141232](https://www.google.com/url?q=https://reviews.llvm.org/D141232&sa=D&source=editors&ust=1778600246202967&usg=AOvVaw02gTDtRrdNKW0mA6HNWrh2)
  * Dynamic shared memory per kernel: [https://reviews.llvm.org/D141233](https://www.google.com/url?q=https://reviews.llvm.org/D141233&sa=D&source=editors&ust=1778600246203096&usg=AOvVaw31rQdyOTKMbn9g4Cyo8okl) 
  * Pinned memory:


  * ½ [https://reviews.llvm.org/D138933](https://www.google.com/url?q=https://reviews.llvm.org/D138933&sa=D&source=editors&ust=1778600246203246&usg=AOvVaw02yP6_sBgRTfG0nM8vBgUY)
  * 2/2 [https://reviews.llvm.org/D139208](https://www.google.com/url?q=https://reviews.llvm.org/D139208&sa=D&source=editors&ust=1778600246203356&usg=AOvVaw2pzMUm5XKSq5L79w7CIpiL) 


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


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246203973&usg=AOvVaw0SHNBhbhECb9Dh1TlpoNwd)


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246204097&usg=AOvVaw1pNWeQf7nb3C8MWfThw9mb)) 


  58. Allocate "all" device memory
  59. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  60. Replay -> load image + user allocated memory, launch with argos and parameters


  * JIT image patch: [https://reviews.llvm.org/D140945](https://www.google.com/url?q=https://reviews.llvm.org/D140945&sa=D&source=editors&ust=1778600246204450&usg=AOvVaw2t9FNxaX2rvA_q8Tiz6cCf) 
  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246204574&usg=AOvVaw0Aaf4r6Tk08kD5n0V6nAuJ)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246204650&usg=AOvVaw0ePeL65qPs7YSplHRDpx_i)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246204869&usg=AOvVaw1SHl0_nUNkO8HPJu6fqDrh)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246205142&usg=AOvVaw2BvHms5-k3yIi8tY8YShld) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246205300&usg=AOvVaw3qYdfY8OYlvcUo2cHNYu2V)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246205454&usg=AOvVaw0_mJX-vHbFRfeEOFxQRW-j)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246205682&usg=AOvVaw2eAdvVMBwQ9n63Se6v0mE1) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246205772&usg=AOvVaw1-YUjTUQ6IKD3h4w6mheB7)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246205909&usg=AOvVaw3zuYkLxZEv0JQNAejsS9uV)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246206583&usg=AOvVaw2rkchiIr3c6JkqB0SPTt30)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246206762&usg=AOvVaw3Y_iY72toWU4UDACO3yk4w)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246206860&usg=AOvVaw0tWdQM-ExAQ9jDgmGxeCO1) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246207011&usg=AOvVaw1uaawMCcsnEGIKOA15xwKD) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246207536&usg=AOvVaw0wgQnI019krswFowO-aLBQ) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246207716&usg=AOvVaw3Zy8-GQBc_CUWlNSzXfzB3) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246207924&usg=AOvVaw1StJNrUrj5u-dYEqnVwTAh)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246208117&usg=AOvVaw3S_KJQUVpWehSfXGRNDZRO)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246208277&usg=AOvVaw0NjFHINAoSFxita2wDNqAI): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246208459&usg=AOvVaw3pnK-HzomZSDJXvQwyqToc) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
