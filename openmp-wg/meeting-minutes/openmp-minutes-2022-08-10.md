### 2022, Aug 10

Agenda

  * Virtual function support
  * Replacing libomptarget dependencies with LLVM libraries


  * Replace dlopen [https://reviews.llvm.org/D131507](https://www.google.com/url?q=https://reviews.llvm.org/D131507&sa=D&source=editors&ust=1778600246276884&usg=AOvVaw3oAEFS265D6VzVeNzEbXdm)
  * Replace libelf [https://reviews.llvm.org/D131401](https://www.google.com/url?q=https://reviews.llvm.org/D131401&sa=D&source=editors&ust=1778600246277037&usg=AOvVaw1Tfiea7FJRPeu7CAVFhFZ6)
  * How to replace libffi for the x86_64 plugin?


  * Deprecating the old driver completely for OpenMP


  * [https://reviews.llvm.org/D130020](https://www.google.com/url?q=https://reviews.llvm.org/D130020&sa=D&source=editors&ust=1778600246277282&usg=AOvVaw1lOZRbDrxrCa5wxjLkvrfs)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246277457&usg=AOvVaw00OFtf8D0cdIbq-QBYft9B)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246277555&usg=AOvVaw05u3hdZBFQUAeP69iokuaA) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246277694&usg=AOvVaw1VucbLhJeOU2nV5M3o75Y5) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246277877&usg=AOvVaw2trsdC31CRbz0OuJn4SGKA) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)


  * Allocators - shared, managed, gpu, other


  * Does AMD have support?


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246278345&usg=AOvVaw1DBbkcPnbEpsw9L4gbQ3VL) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246278517&usg=AOvVaw2lcRYNaP1WMkbMT-6LF7k0) only adds the plugin runtime support


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246278804&usg=AOvVaw0u5Rs_Dz3hGeosNc5khUkW)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246278997&usg=AOvVaw3mHWzcZ0dw9lwNoRGUT71X)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246279151&usg=AOvVaw0vwXuxrA19QqVtKRBn9CBU): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246279341&usg=AOvVaw1Yw1B0z-Oo85r0wSwes2gD) 


  * Who all are planning to attend SC22 in Nov?



###
