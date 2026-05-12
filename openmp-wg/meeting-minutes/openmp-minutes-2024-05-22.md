### 2024, May 22

Agenda 

New 

  * DLopen libcuda / libhsa by default


  * Export dynamic cuda / dynamic hsa so libc / clang can use it


  * OpenMP hull tasks:


  * What is the community's feeling on the hull tasks discussion in the language committee and potential implementation in the LLVM libomp runtime?
  * Is there some interest to try to get an implementation going to get some better idea of the feature impact before the TR of OpenMP 6.0 or something?


  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * New PR: [https://github.com/llvm/llvm-project/pull/75125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/75125&sa=D&source=editors&ust=1778600246026546&usg=AOvVaw1DOe5kB5sU0BXNGZzf01P4)
  * AMD would  like to make sure it builds.
  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246026785&usg=AOvVaw01nnGzgDmA1KdjhacCvoQ9) 
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246026935&usg=AOvVaw2E7fBy6vF06SWGsGklfjR3)


  * Subscription List: [https://github.com/orgs/llvm/teams/pr-subscribers-offload](https://www.google.com/url?q=https://github.com/orgs/llvm/teams/pr-subscribers-offload&sa=D&source=editors&ust=1778600246027128&usg=AOvVaw3Z5rhR7mv1pMNhneBrFUQu)
  * Building the DeviceRTL / offload library
  * Moving to statically linking plugins


  * [https://github.com/llvm/llvm-project/pull/86683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/86683&sa=D&source=editors&ust=1778600246027396&usg=AOvVaw1WjzaVlbotWVjzsrAnruRB)


  * Compound/composite constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm.


  * OpenMP version 5.2 as default


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * OpenMP Examples : 


  * target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

#pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2
