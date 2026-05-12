### 2022, Aug 17

Agenda

  * Replacing libomptarget dependencies with LLVM libraries


  * Replace dlopen [https://reviews.llvm.org/D131507](https://www.google.com/url?q=https://reviews.llvm.org/D131507&sa=D&source=editors&ust=1778600246274131&usg=AOvVaw24q_QATM0S2Cz1NNcfZl2_)
  * Replace libelf [https://reviews.llvm.org/D131401](https://www.google.com/url?q=https://reviews.llvm.org/D131401&sa=D&source=editors&ust=1778600246274259&usg=AOvVaw20HmRgomrQkDZ6rO5J3sf2)
  * How to replace libffi for the x86_64 plugin?


  * Deprecating the old driver completely for OpenMP


  * [https://reviews.llvm.org/D130020](https://www.google.com/url?q=https://reviews.llvm.org/D130020&sa=D&source=editors&ust=1778600246274481&usg=AOvVaw0MO8-X2sLqcg36fmCh73tL)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246274660&usg=AOvVaw1MIXatkvButVfrAv0XKUfl)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246274757&usg=AOvVaw1yo7jEIcPDwqWllBHtRlD3) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246274896&usg=AOvVaw2XYLS9KpatLPu9ZYze_wE-) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246275079&usg=AOvVaw2nD0iKFwFFeEznExmUm9_O) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)


  * Allocators - shared, managed, gpu, other


  * Does AMD have support?


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246275558&usg=AOvVaw10sFI1gDpvRatF9UZ3O5o-) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246275724&usg=AOvVaw1_gdIrJOhr4AW_Ps6uN8lg) only adds the plugin runtime support


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246276020&usg=AOvVaw3UacrEJ7o4gElS_uwuMKcY)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246276205&usg=AOvVaw2pvlDCy0aFqp9D1Z9ER15C)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246276364&usg=AOvVaw39dQO4JNXSgBvDWDdB-0FO): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246276546&usg=AOvVaw2-gkcio00ARUhfKCruramj) 



###
