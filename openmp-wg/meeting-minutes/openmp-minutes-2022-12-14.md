### 2022, Dec 14

Agenda

  * Meetings during holidays  Dec 28th meeting canceled.
  * OpenMP-opt slack:


  * [https://join.slack.com/t/openmp-opt/shared_invite/zt-1ktv8h0wx-6Ks4PjL3qnx8dhC9Nx4fgg](https://www.google.com/url?q=https://join.slack.com/t/openmp-opt/shared_invite/zt-1ktv8h0wx-6Ks4PjL3qnx8dhC9Nx4fgg&sa=D&source=editors&ust=1778600246221903&usg=AOvVaw24-vFHMz080mus_KcErLSe) 


  * Pinned memory:


  * ½ [https://reviews.llvm.org/D138933](https://www.google.com/url?q=https://reviews.llvm.org/D138933&sa=D&source=editors&ust=1778600246222044&usg=AOvVaw38p_eZpebjEs0P6dHK5ava)
  * 2/2 [https://reviews.llvm.org/D139208](https://www.google.com/url?q=https://reviews.llvm.org/D139208&sa=D&source=editors&ust=1778600246222152&usg=AOvVaw10fzuV1MV4pd6A3RbkELTa) 


  * NextGen AMD Plugin


  * Jan-Patrick is testing it
  * Latest status: [https://github.com/kevinsala/llvm-project/tree/develop](https://www.google.com/url?q=https://github.com/kevinsala/llvm-project/tree/develop&sa=D&source=editors&ust=1778600246222387&usg=AOvVaw0HdCmiXa7Z_YHdWCn9nSPM) 


  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * Record + Replay ([https://reviews.llvm.org/D138931](https://www.google.com/url?q=https://reviews.llvm.org/D138931&sa=D&source=editors&ust=1778600246222919&usg=AOvVaw1obGpF8WYlS1mKp0nTNuTL)) 


  67. Allocate "all" device memory
  68. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  69. Replay -> load image + user allocated memory, launch with argos and parameters


  * New meeting time for Jan 23, when2meet?
  *   * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246223358&usg=AOvVaw3wCg-mE6n7vIKA0GkXnyET)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246223444&usg=AOvVaw2qucP7rPMIiLzyIb8SZxQf)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246223660&usg=AOvVaw1EqI95ayG-2GdQslKylF5O)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246223916&usg=AOvVaw2Sf94B5S5rJuaAHxwQuUAC) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246224062&usg=AOvVaw31GA1EggI6Pkr_A7OcReCC)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246224215&usg=AOvVaw0upKEU6NTZr20aY_Gvs1h1)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246224456&usg=AOvVaw1XyUTuOWTKY1DKQ3cq7QnH) 


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246224568&usg=AOvVaw22pKvaKMfEJJUPntyWNnsg)
  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246224665&usg=AOvVaw1gmqxCtFDvKlVub7sdzGE9)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246224800&usg=AOvVaw36Mt6OC7K7nyRhFZM42LD0)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246225515&usg=AOvVaw1W_XqblXOPOxjp3gU50D-e)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246225693&usg=AOvVaw01zTkQLApBKDGuHtdlaC2Z)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246225790&usg=AOvVaw34j3lNI4QEg6Gs-Ukx1Qsv) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246225939&usg=AOvVaw3eiHPqbGo-1Lb07Wy9YOSw) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246226467&usg=AOvVaw3H3isZCkHJ439Xsbtjqdd6) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246226641&usg=AOvVaw2TuhntTeHguMGjb9ueB_S_) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246226844&usg=AOvVaw2beehX2YAsoc-VvyjCK_--)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246227023&usg=AOvVaw3Vucjrn2N5kshZIcWylqBJ)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246227189&usg=AOvVaw2dqyoPBU15g02DKykRHBKh): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246227373&usg=AOvVaw36Mb84NZ3_RiLbpOm0IeXL) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
