### 2022, July 20

Agenda

  * Linking llvm libs into libomptarget (instead of copy/pasting from llvm for D127432 etc)


  * Previously thwarted by license differences, since been resolved
  * Every time this is proposed people come out of the woodwork to complain about the library they use from llvm using other parts of llvm
  * Let's tell those people to just build llvm if they want to use parts of llvm
  * https://reviews.llvm.org/D129875


  * Updating default version to 5.1


  * Do we want to do it?
  * When? Before llvm-15 branching?
  * [https://clang.llvm.org/docs/OpenMPSupport.html#openmp-5-1-implementation-details](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246290646&usg=AOvVaw0P4s9kngyQnTkDBwpbuAN1) 


  * Deprecating the old driver completely for OpenMP


  * https://reviews.llvm.org/D130020


  * LLVM objcopy for offloading images


  * Should allow us to treat them like the old offload-bundler


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246291059&usg=AOvVaw1LtRm19mewLHAU0gCga0-C)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246291161&usg=AOvVaw0LZPpnQO3JTiLUTn4m7xjc) 


  * Multi-arch compilation support


  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246291291&usg=AOvVaw1ag05pMi7p8HarOMPqUMKu): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D127432](https://www.google.com/url?q=https://reviews.llvm.org/D127432&sa=D&source=editors&ust=1778600246291415&usg=AOvVaw0hobNgNeIfufSL_SLCiL-T): [Libomptarget] Add support for offloading binaries in libomptarget
  * [D127505](https://www.google.com/url?q=https://reviews.llvm.org/D127505&sa=D&source=editors&ust=1778600246291535&usg=AOvVaw3XlPYxa4X_5JogJmLHO-lt): [Libomptarget] Add checks for CUDA subarchitecture using new info
  * [D127769](https://www.google.com/url?q=https://reviews.llvm.org/D127769&sa=D&source=editors&ust=1778600246291654&usg=AOvVaw0U1gmi7bJt0bff12MZMGh1): [Libomptarget] Add checks for AMDGPU TargetID using new image info
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246291775&usg=AOvVaw1xJksElgjejWvS7JB8WQ9X): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D128090](https://www.google.com/url?q=https://reviews.llvm.org/D128090&sa=D&source=editors&ust=1778600246291906&usg=AOvVaw0UdL-LVPKQGhQt1qhRRViO): [Clang][OpenMP] Process multi-arch compilation options given via -march


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246292120&usg=AOvVaw0Ydp5KF1x578SQS6fdn0ed) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246292309&usg=AOvVaw1Z0Njy39NJhozoGASC2js1) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * _OPENMP (Joachim)


  * Currently 201611 (= TR4 date - aka 5.0 Preview 1)


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246292793&usg=AOvVaw2qabzgRRq_AbceGWQPebb0) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246292964&usg=AOvVaw3bPAHosrD0NXWPaG9jsydV) only adds the plugin runtime support


  * Change the target interface to __tgt_target_kernel and use a struct for the arguments.


  * [D128549](https://www.google.com/url?q=https://reviews.llvm.org/D128549&sa=D&source=editors&ust=1778600246293175&usg=AOvVaw2aVpyJeobVkb6cLlERtLdT) [Libomptarget] Implement a unified kernel entry function
  * [D128817](https://www.google.com/url?q=https://reviews.llvm.org/D128817&sa=D&source=editors&ust=1778600246293299&usg=AOvVaw368RVvohJ-FVaY04kZxSWS) [Libomptarget] Use new tripcount argument instead of the push function


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246293612&usg=AOvVaw0BTbVCxhSHDfrWSjlWFJZZ)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246293803&usg=AOvVaw0d6Eaz-XfWSMqGaB_ez952)
  * -O3 optimization for new Device RTL


  * [https://reviews.llvm.org/D129344](https://www.google.com/url?q=https://reviews.llvm.org/D129344&sa=D&source=editors&ust=1778600246293946&usg=AOvVaw0O4MZuyAZ73oV-3z1NaiU_) 



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246294136&usg=AOvVaw2u5-pBn8EVtHRyvX6ticQT) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246294258&usg=AOvVaw1tJv7lX0nyWfONUE8iQdW2)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246294370&usg=AOvVaw1KhT4u-AnDwsQNIoLFO2hN)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246294482&usg=AOvVaw1gw1zxGEbexRHkmaFTIHpK)



###
