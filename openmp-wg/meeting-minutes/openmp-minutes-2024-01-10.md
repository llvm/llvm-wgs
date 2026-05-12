### 2024, Jan 10

Agenda 

New 

  * Getting rid of the plugin design and statically linking instead


  * Similar to LLVM's design for target backends


  * More a note than a discussion point: libomptarget -> offload: Buildbots should move accordingly
  * OpenMP Examples : target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

 #pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);

  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246044197&usg=AOvVaw2yu75iQtrERPVJJnbvzPlc) 
  * Deep copy of libomptarget and (offload, libomptarget) co-exist till offload is stable enough to become default and libomptarget can be deleted?
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246044508&usg=AOvVaw2jTqqnsm2DTva5WTWdc3Gc)


  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246044737&usg=AOvVaw2yoNLwVenxv-jd5llyfabw) (-DLLVM_ENABLE_PROJECTS=openmp): 34 failed tests
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246044875&usg=AOvVaw2lUNA51FT0JRCpg8RAwqHZ) (-DLLVM_ENABLE_RUNTIMES=openmp): 34 failed tests
  * [[libomptarget][tests] Maximum assumed device heap size. * Issue #71747](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/71747&sa=D&source=editors&ust=1778600246045045&usg=AOvVaw28I10NGe0T2OzGY69uLlLy) (4 tests)



###
