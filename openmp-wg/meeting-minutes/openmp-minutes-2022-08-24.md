### 2022, Aug 24

Agenda

  * Replacing libomptarget dependencies with LLVM libraries


  * Replace dlopen [https://reviews.llvm.org/D131507](https://www.google.com/url?q=https://reviews.llvm.org/D131507&sa=D&source=editors&ust=1778600246271348&usg=AOvVaw2DEWG3MKXDrr-Iroj24bNN)
  * Replace libelf [https://reviews.llvm.org/D131401](https://www.google.com/url?q=https://reviews.llvm.org/D131401&sa=D&source=editors&ust=1778600246271473&usg=AOvVaw3BOP8KyM739WjJKDOVSzMO)
  * How to replace libffi for the x86_64 plugin?


  * Deprecating the old driver completely for OpenMP


  * [https://reviews.llvm.org/D130020](https://www.google.com/url?q=https://reviews.llvm.org/D130020&sa=D&source=editors&ust=1778600246271684&usg=AOvVaw3OQIvVXwqle8toRBRb2Bek)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246271862&usg=AOvVaw0uKbXoDNXzZkXT0w4uDQcW)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246271963&usg=AOvVaw2TQEwqyxyfP_sgHFfz6Q4l) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246272106&usg=AOvVaw2rzm2l36288C_eOLJX44sC) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246272306&usg=AOvVaw3rT28HHku1f_8zSwl--dN_) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - shared, managed, gpu, other


  * Does AMD have support?


  * Dynamic shared memory 


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246272717&usg=AOvVaw1JV49RMdUAtInXAK5B36YP) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246272888&usg=AOvVaw1mahBvG-sc9_p1WEy2RG1B) only adds the plugin runtime support


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246273188&usg=AOvVaw3ETlmYSdHyQr4sGAylayrd)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246273385&usg=AOvVaw0WeGnFdON64mf2SDxb5QL_)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246273549&usg=AOvVaw07Af_GbFKWz-ggCbMLCXMb): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246273741&usg=AOvVaw32z87P7sRzEvO2fqiscCkN) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
