### 2023, Jan 18

Agenda

  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246195812&usg=AOvVaw1n8wjkx-st8cJjbypRbCfc) 
  * New kernel launch API: [https://reviews.llvm.org/D141232](https://www.google.com/url?q=https://reviews.llvm.org/D141232&sa=D&source=editors&ust=1778600246195925&usg=AOvVaw2xdowmQc8uRuBJOJL-h3ft)
  * Dynamic shared memory per kernel: [https://reviews.llvm.org/D141233](https://www.google.com/url?q=https://reviews.llvm.org/D141233&sa=D&source=editors&ust=1778600246196044&usg=AOvVaw2C1ctAVzqmZi_RVbVlvjMU) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246196139&usg=AOvVaw2Yu4Xr6Ca47WHXiuieCvd9) 
  * Num threads: [https://github.com/llvm/llvm-project/blob/feee22db52259d19a8624318517ef5688abfc67c/openmp/libomptarget/DeviceRTL/src/State.cpp#L356](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/feee22db52259d19a8624318517ef5688abfc67c/openmp/libomptarget/DeviceRTL/src/State.cpp%23L356&sa=D&source=editors&ust=1778600246196380&usg=AOvVaw0EWuaK43yVH5AMmRlMudEX) 
  * Pinned memory:


  * ½ [https://reviews.llvm.org/D138933](https://www.google.com/url?q=https://reviews.llvm.org/D138933&sa=D&source=editors&ust=1778600246196521&usg=AOvVaw1VX1U-ME14ASpc9YZDaE91)
  * 2/2 [https://reviews.llvm.org/D139208](https://www.google.com/url?q=https://reviews.llvm.org/D139208&sa=D&source=editors&ust=1778600246196620&usg=AOvVaw0n5RNnf4jwL9fLB2DRZQpd) 


  * Adding support for `--offload-arch=native`


  * Autodetects the GPU architecture


  * Only build GPU tests if a GPU is found on the system: [https://reviews.llvm.org/D142018](https://www.google.com/url?q=https://reviews.llvm.org/D142018&sa=D&source=editors&ust=1778600246196876&usg=AOvVaw2eoBpJV7YjG1g2XKazh3h1)
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246197407&usg=AOvVaw2M1vPrm92jgDxIxFZCph4z)


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246197536&usg=AOvVaw25rnfeYHEvEexHcH0Ei0Yq)) 


  55. Allocate "all" device memory
  56. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  57. Replay -> load image + user allocated memory, launch with argos and parameters


  * JIT image patch: [https://reviews.llvm.org/D140945](https://www.google.com/url?q=https://reviews.llvm.org/D140945&sa=D&source=editors&ust=1778600246197884&usg=AOvVaw1KVOmh4ByRLL2Y8YIwl3Gr) 
  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246198010&usg=AOvVaw0NvQJTFT4DKT22DY-Uit9V)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246198093&usg=AOvVaw0F32tuc_6XFlFP8VjQrPzo)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246198316&usg=AOvVaw23PXdS5t2Bld1WPW3msO7a)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246198580&usg=AOvVaw3BJD_RJF4K09Qf9J_nAapZ) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246198736&usg=AOvVaw3GQ8GAJB9iYwevW1x4Z6Q6)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246198887&usg=AOvVaw2vPgJVmEWx5SlzYNjiWbTz)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246199137&usg=AOvVaw2_lNKBOeERSI85oE_BwFdE) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246199240&usg=AOvVaw0Z8GUcuZJqG7mZINBPh5e_)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246199377&usg=AOvVaw1k8oeqLUKtCD1bjMAE2V7D)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246200048&usg=AOvVaw0-IsCOGXhHKEgEkxctEfxG)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246200231&usg=AOvVaw02SWDVSCJziFgGmPWIfrfu)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246200333&usg=AOvVaw205-5tgYvVjbE6fRiSCJym) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246200486&usg=AOvVaw2nQuPL_IRmdLKOcHAlm704) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246201034&usg=AOvVaw12nS2oTJkI3jGv0qAmAK2D) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246201212&usg=AOvVaw0CKTheS-hBLRgHCaOQpcu0) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246201413&usg=AOvVaw0FKe3PZsYYqq6ht7JaY2Pz)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246201604&usg=AOvVaw3ul3HLWMMkdyZZ6QLSkyxP)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246201756&usg=AOvVaw2kKLGRPlaGLhe9W-sy0iOh): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246201938&usg=AOvVaw3X3v4_v4mriZ7glRnsOtEg) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246202253&usg=AOvVaw1B0ChPMPokF1vbc20Qlkj6) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246202375&usg=AOvVaw0sGT8kqG7k0mRZVBdAa4gH)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246202487&usg=AOvVaw2Y-PD1K4JdmgowQAY5MPMZ)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246202621&usg=AOvVaw1zE30l8Yx6sWZRYusu5_E4)
