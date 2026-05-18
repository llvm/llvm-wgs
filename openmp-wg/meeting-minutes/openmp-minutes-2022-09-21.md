### 2022, Sept 21

Agenda

  *   OMP_TGT_MAPTYPE_CLOSE           = 0x400,   // copy data to device


  * Need additional bits to indicate the location like cache …


  * No more backward compatibility.


  * [https://reviews.llvm.org/D133277](https://www.google.com/url?q=https://reviews.llvm.org/D133277&sa=D&source=editors&ust=1778600246257431&usg=AOvVaw07P963z6PTTUhudXHciQub) and [https://reviews.llvm.org/D133276](https://www.google.com/url?q=https://reviews.llvm.org/D133276&sa=D&source=editors&ust=1778600246257515&usg=AOvVaw3F64tDQ-TylEuUHt91t9lQ).
  * Ever since we build libomptarget and plugins as LLVM libraries, the "backward compatibility" is gone. Given that fact, we can change existing interfaces w/o the need of consideration of backward compatibility.
  * ^ we also never had backwards compatibility afaik, certainly never tested to see if it worked
  * [https://reviews.llvm.org/D133053](https://www.google.com/url?q=https://reviews.llvm.org/D133053&sa=D&source=editors&ust=1778600246257904&usg=AOvVaw13ZhWEYUkarlM0t_3Y2vtZ) changes free interface between the plugins


  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246258081&usg=AOvVaw2tIHT34cxT8CbSm0n5Pl26)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * New Link for meeting (see top of doc for link & ICS file)
  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * OpenMP GPU Reduction
  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246258894&usg=AOvVaw1JuTEiVLOs6rDZst5bG4zZ)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246259004&usg=AOvVaw0Y3QVLkxhqTapLa5ivSlLC) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246259167&usg=AOvVaw2aKfyrRuyLgUlsrMfSCOLj) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246259367&usg=AOvVaw1M6ErsRyAKPfu0eSEanCV1) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  * ^ if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA. Open question about what omp_target_is_present() is supposed to return on migratable memory.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246259987&usg=AOvVaw22kU0292KyXkkMp3jXb9e_) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246260162&usg=AOvVaw1lDA2RSxGBm8I3STKu6xzH) only adds the plugin runtime support


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246260461&usg=AOvVaw1SbKd1JYjIhykjoNMhrb77)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246260644&usg=AOvVaw1v2pf1M7OLEd7iIJnXdKR3)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246260806&usg=AOvVaw0hAsTAM-sG1dsEfo_GFwp6): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246260989&usg=AOvVaw0UVLSOIO82uM0Y4jnn5LLg) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246261266&usg=AOvVaw3Jk1vGXOXIdHxcgBsLR0UL) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246261385&usg=AOvVaw12zKSj1eV6_Vz6wZdbkCVJ)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246261497&usg=AOvVaw1QlUyBtOUwY7oeAIbMgoU_)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246261607&usg=AOvVaw3kIwX-WHFUO-7dmelbtpGO)



###
