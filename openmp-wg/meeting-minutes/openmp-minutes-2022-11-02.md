### 2022, Nov 02

Agenda

  * Openmp amdgpu buildbot failure:  
[https://lab.llvm.org/buildbot/#/builders/193/builds/21152](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193/builds/21152&sa=D&source=editors&ust=1778600246243743&usg=AOvVaw3WQWv35_eDSzqDsOxNh6dW) ([https://reviews.llvm.org/D135444](https://www.google.com/url?q=https://reviews.llvm.org/D135444&sa=D&source=editors&ust=1778600246243829&usg=AOvVaw3beH0MBE_pLWtRf36ke6PG))


  * JD: I'll fix it now


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246244010&usg=AOvVaw2IpdfS88gBn0lq377-TPUx)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246244096&usg=AOvVaw3e9-Y8i-yKoTATfmJucL6a)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246244340&usg=AOvVaw1QqktKvg1mfpHIGDBtjwXE)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246244599&usg=AOvVaw0auQqM_h92iVourw0Y8Wv9) 



  * [⚙ [OpenMP] Add non-blocking support for target nowait regions](https://www.google.com/url?q=https://reviews.llvm.org/D132005&sa=D&source=editors&ust=1778600246244743&usg=AOvVaw1oEvJEJN1MR0t9hmPNSbAU)


  * OpenMP Cluster and MPI plugin
  * [Presented slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1yFaIanlR4JccYFhrKe_30k17LgjvyvC6DkOgc1Hum5c/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246244888&usg=AOvVaw3l5UokmDUYVFpNie_hQP78)


  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246245120&usg=AOvVaw1MrylruMbwJujbQaCigVc-)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246245266&usg=AOvVaw0tKQI8kHzEzm0IBBxwExmz)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246245930&usg=AOvVaw0JJtLQVDdVE-JXNhEmo4Dv)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246246106&usg=AOvVaw3JrnhsN-QaUrlYo59MTaiH)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246246220&usg=AOvVaw0uPy6ie9F6BoZxWybdMkOv) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246246379&usg=AOvVaw0ipv2WdUnkUxMZaPs5nF3a) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246246897&usg=AOvVaw0Wq-EOKVH7q8_cNTAheYPX) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246247069&usg=AOvVaw0zL2xZpV1h0fbDbfkb9cXG) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246247276&usg=AOvVaw1_dc3r4KnyxNekqNkabe33)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246247470&usg=AOvVaw2VmUmwpZhEsd3-i2ipOqlX)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246247626&usg=AOvVaw18DCKW6J3EKUmQIwCGQ9q_): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246247804&usg=AOvVaw21LJab-YZd5-7CjmSqNfls) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
