### 2022, July 13

Agenda

  * Linking llvm libs into libomptarget (instead of copy/pasting from llvm for D127432 etc)


  * Previously thwarted by license differences, since been resolved
  * Every time this is proposed people come out of the woodwork to complain about the library they use from llvm using other parts of llvm
  * Let's tell those people to just build llvm if they want to use parts of llvm


  * Updating default version to 5.1


  * Do we want to do it?
  * When? Before llvm-15 branching?
  * [https://clang.llvm.org/docs/OpenMPSupport.html#openmp-5-1-implementation-details](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246295268&usg=AOvVaw3X8K1YdFyKBcY4adYMhNh_) 


  * Deprecating the old driver completely for OpenMP before LLVM15
  * LLVM objcopy for offloading images


  * Should allow us to treat them like the old offload-bundler


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246295641&usg=AOvVaw03F3TvI8Wwq_VrivDsSLmw)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246295741&usg=AOvVaw08CcAAmRz8JwXls1pBntSV) 


  * Multi-arch compilation support


  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246295862&usg=AOvVaw3HIUQ9XHBB97Cb5wku-PRp): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D127432](https://www.google.com/url?q=https://reviews.llvm.org/D127432&sa=D&source=editors&ust=1778600246295984&usg=AOvVaw2fIHONXvNmrFrbtEVv-hic): [Libomptarget] Add support for offloading binaries in libomptarget
  * [D127505](https://www.google.com/url?q=https://reviews.llvm.org/D127505&sa=D&source=editors&ust=1778600246296103&usg=AOvVaw2t8SDO_9Y7t6exLOW_7fkg): [Libomptarget] Add checks for CUDA subarchitecture using new info
  * [D127769](https://www.google.com/url?q=https://reviews.llvm.org/D127769&sa=D&source=editors&ust=1778600246296238&usg=AOvVaw2b18NEH9sAjLpioHyZPdfl): [Libomptarget] Add checks for AMDGPU TargetID using new image info
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246296369&usg=AOvVaw2RfF_cHA3bPnomYwBS_TCX): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D128090](https://www.google.com/url?q=https://reviews.llvm.org/D128090&sa=D&source=editors&ust=1778600246296496&usg=AOvVaw0hyRby0Wd_f-sZVdmbfuBP): [Clang][OpenMP] Process multi-arch compilation options given via -march


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246296693&usg=AOvVaw2K_qvMe8zHCMwzM-R5Aus2) (gdb plugin) - landed!
  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246296802&usg=AOvVaw3lQteFlmPUsEs7AQIuvRxn) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * _OPENMP (Joachim)


  * Currently 201611 (= TR4 date - aka 5.0 Preview 1)


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246297255&usg=AOvVaw2lZRBVHKeToHzIxzN3QdpY) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246297418&usg=AOvVaw2v2oNZvvzfzbsw1J6Cxlx3) only adds the plugin runtime support


  * Change the target interface to __tgt_target_kernel and use a struct for the arguments.


  * [D128549](https://www.google.com/url?q=https://reviews.llvm.org/D128549&sa=D&source=editors&ust=1778600246297625&usg=AOvVaw1G-MbVw_Wm8Oq6wpth9Ufm) [Libomptarget] Implement a unified kernel entry function
  * [D128817](https://www.google.com/url?q=https://reviews.llvm.org/D128817&sa=D&source=editors&ust=1778600246297740&usg=AOvVaw2ZFLSio-PD3VMDak6JwXYR) [Libomptarget] Use new tripcount argument instead of the push function


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246298093&usg=AOvVaw1j1JM9PMvtZjD7V1-lgj8N)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246298286&usg=AOvVaw24LlN1k1bFNtGzaOJZqo4l)
  * -O3 optimization for new Device RTL


  * [https://reviews.llvm.org/D129344](https://www.google.com/url?q=https://reviews.llvm.org/D129344&sa=D&source=editors&ust=1778600246298425&usg=AOvVaw1JQK9BSTegST0UKuAnKN1F) 



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246298613&usg=AOvVaw18OucyUD1dbTBZF1dd6WHq) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246298731&usg=AOvVaw01MTzX1RK_QJQMA1rNtueq)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246298841&usg=AOvVaw1INtDPqcjnMqBfete1B-W0)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246298951&usg=AOvVaw2f8dFgc_IBTNqEr0OfTHhe)



###
