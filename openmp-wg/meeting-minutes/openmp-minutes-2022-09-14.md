### 2022, Sept 14

Agenda

  *   OMP_TGT_MAPTYPE_CLOSE           = 0x400,   // copy data to device


  * Need additional bits to indicate the location like cache …


  * No more backward compatibility.


  * [https://reviews.llvm.org/D133277](https://www.google.com/url?q=https://reviews.llvm.org/D133277&sa=D&source=editors&ust=1778600246262064&usg=AOvVaw1hr6zqSSgVHuaHCB1cOqEi) and [https://reviews.llvm.org/D133276](https://www.google.com/url?q=https://reviews.llvm.org/D133276&sa=D&source=editors&ust=1778600246262150&usg=AOvVaw2Y_Pb1NMMIYYG8WcCM4GnB).
  * Ever since we build libomptarget and plugins as LLVM libraries, the "backward compatibility" is gone. Given that fact, we can change existing interfaces w/o the need of consideration of backward compatibility.
  * ^ we also never had backwards compatibility afaik, certainly never tested to see if it worked
  * [https://reviews.llvm.org/D133053](https://www.google.com/url?q=https://reviews.llvm.org/D133053&sa=D&source=editors&ust=1778600246262545&usg=AOvVaw27DW9lPV75T4DifVOiIUwP) changes free interface between the plugins


  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246262715&usg=AOvVaw0WraBA3iV56ECJxYQksvaF)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * New Link for meeting (see top of doc for link & ICS file)
  * OpenMP GPU Reduction
  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246263278&usg=AOvVaw3EC9P6q_QYD1DeTDpLAWis)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246263384&usg=AOvVaw1LTniFCjEOnO5ENGk7uzcE) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246263526&usg=AOvVaw0RhGt71UHGune_M-AUuzEH) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246263724&usg=AOvVaw2UMwmem_mt4cx8z21gvU03) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  * ^ if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA. Open question about what omp_target_is_present() is supposed to return on migratable memory.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246264333&usg=AOvVaw3z4gCRJOcAzKH0uz3ki8IK) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246264498&usg=AOvVaw02pF2PCCospfAqMD8m7Grp) only adds the plugin runtime support


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246264803&usg=AOvVaw1dUAQU3ULBLEdB8qZAqDcX)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246264987&usg=AOvVaw3vw1CaZsClC2uBOpIg0M5F)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246265150&usg=AOvVaw0kn73vC1-rW4r1o28KmpKa): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246265337&usg=AOvVaw0liEnoOk-806AIpTt0Bxbd) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
