### 2024, Mar 27

Agenda 

New 

  * Mapper bug [llvm#61636](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/61636&sa=D&source=editors&ust=1778600246032390&usg=AOvVaw1ug-dEupNrbed98wfjwNEC), potential fix:


  * [https://github.com/jdoerfert/llvm-project/commit/527bf4b1293f452aac1f872c4f771c7950b911f9](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commit/527bf4b1293f452aac1f872c4f771c7950b911f9&sa=D&source=editors&ust=1778600246032569&usg=AOvVaw3XLS2ETMDjGUGodUMqWmzp)


  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * New PR: [https://github.com/llvm/llvm-project/pull/75125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/75125&sa=D&source=editors&ust=1778600246032797&usg=AOvVaw13I6WXUiWdmECkVM018dwe)
  * AMD would  like to make sure it builds.
  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246033032&usg=AOvVaw1EE1bxnr62CH87w-x4rHSj) 
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246033195&usg=AOvVaw2zmZJGq8bGJS6Re6DYTk5o)


  * Moving to statically linking plugins


  * [https://github.com/llvm/llvm-project/pull/86683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/86683&sa=D&source=editors&ust=1778600246033371&usg=AOvVaw2_z0qoHRhmidl6EVenECTG)


  * Hang started Feb 22/23:


  * [https://discourse.llvm.org/t/openmp-offloading-double-build-hanging/77256](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-offloading-double-build-hanging/77256&sa=D&source=editors&ust=1778600246033558&usg=AOvVaw38ons0pCgJTAmUd5a1G1B1)
  * Seems resolved.


  * Feature flags for offloading tests:


  * [https://github.com/llvm/llvm-project/pull/83261#issuecomment-2022901322](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/83261%23issuecomment-2022901322&sa=D&source=editors&ust=1778600246033788&usg=AOvVaw1aQAN9MtbLKi5Q-L-Qdw2p)


  * Compound/composite constructs in Flang (and Clang)
  * OpenMP version 5.2 as default
  * OpenMP Examples : 


  * target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

#pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);
