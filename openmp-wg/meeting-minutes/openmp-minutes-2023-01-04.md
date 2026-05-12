### 2023, Jan 4

Agenda

  * When 2 meet next: [https://www.when2meet.com/?18056590-SQ9TR](https://www.google.com/url?q=https://www.when2meet.com/?18056590-SQ9TR&sa=D&source=editors&ust=1778600246208800&usg=AOvVaw3179L31YVaBIvhpQuU58tN) 
  * Pinned memory:


  * ½ [https://reviews.llvm.org/D138933](https://www.google.com/url?q=https://reviews.llvm.org/D138933&sa=D&source=editors&ust=1778600246208950&usg=AOvVaw1UihcadqDa1itbVHb27eD6)
  * 2/2 [https://reviews.llvm.org/D139208](https://www.google.com/url?q=https://reviews.llvm.org/D139208&sa=D&source=editors&ust=1778600246209051&usg=AOvVaw22UuHNT99OlZ6Qhj_bngci) 


  * AMDGPU JIT [https://reviews.llvm.org/D140720](https://www.google.com/url?q=https://reviews.llvm.org/D140720&sa=D&source=editors&ust=1778600246209176&usg=AOvVaw11nON4SJvNRSt2_p7GlOPb) 
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


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246209762&usg=AOvVaw3svCzpft2F1zR7d4tGzKgq)


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246209884&usg=AOvVaw0bAnvM0zC75gYJPNiMHM6w)) 


  61. Allocate "all" device memory
  62. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  63. Replay -> load image + user allocated memory, launch with argos and parameters


  * JIT image patch: [https://reviews.llvm.org/D140945](https://www.google.com/url?q=https://reviews.llvm.org/D140945&sa=D&source=editors&ust=1778600246210256&usg=AOvVaw2FH5tfTrlU72XHRhy1bbM9) 
  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246210374&usg=AOvVaw2Qv-sc5-YDssnZbJ13Haql)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246210450&usg=AOvVaw3SMR5bdFtzN951ZNMgRyd9)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246210676&usg=AOvVaw0T6b0203RpIkcKk4qqnzeg)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246210933&usg=AOvVaw1wuLLe3MtMlRntAf5zeElN) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246211087&usg=AOvVaw05_4LibM_nuTGxAR8DPUKU)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246211245&usg=AOvVaw0O-3wgtbtivGjWue4wVOTM)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246211538&usg=AOvVaw0kwSy8-GiGEkog2O-h6NtF) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246211635&usg=AOvVaw1IIPjtNEtmO2XKqpIc0T6Q)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246211770&usg=AOvVaw0kUNI4UbubterA7PfKy4z-)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246212461&usg=AOvVaw0D7pUVlYT07suTSsHcem3r)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246212658&usg=AOvVaw2ov_2c9z0M07w1Tks6wyIX)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246212758&usg=AOvVaw2A64k050-5RvROWbpnPUk6) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246212909&usg=AOvVaw28J_j-V0iwqKwWZCIf26EL) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246213440&usg=AOvVaw2K-QDw-TwfcWqiUpOiBeDE) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246213612&usg=AOvVaw0mfdqJ_xeFK6QQNAT4sGpQ) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246213813&usg=AOvVaw2Km3SwfJ3zdcld6LRMQTFC)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246213995&usg=AOvVaw29wSKIYnLi0HC92K8VHUC1)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246214168&usg=AOvVaw3tcva4ur8Rfwm7Hh4SJ3ZM): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246214359&usg=AOvVaw2ZD5UJ4z-YgZpSVRbTeJXe) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
