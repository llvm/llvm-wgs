### 2024, April 24

Agenda 

New 

  * Mapper bug [llvm#61636](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/61636&sa=D&source=editors&ust=1778600246030221&usg=AOvVaw3sqUi5J_MneT1JvQySp4eU), potential fix:


  * [https://github.com/jdoerfert/llvm-project/commit/527bf4b1293f452aac1f872c4f771c7950b911f9](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commit/527bf4b1293f452aac1f872c4f771c7950b911f9&sa=D&source=editors&ust=1778600246030402&usg=AOvVaw3SBnezd_TAxQ2rFqLQcnPT)


  * Buildbots still need to catch up with move to offload. Changes have not propagated to all builders.


  * Please help avoid breakages by monitoring [https://lab.llvm.org/staging/#/builders/191](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/191&sa=D&source=editors&ust=1778600246030647&usg=AOvVaw3ozZITFix0Zs7G-rmaTHl2) 


  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * New PR: [https://github.com/llvm/llvm-project/pull/75125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/75125&sa=D&source=editors&ust=1778600246030863&usg=AOvVaw1v9yoM1se840I7DY8DGrEj)
  * AMD would  like to make sure it builds.
  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246031088&usg=AOvVaw3qjCRqF0StWt_aJ21vXy9M) 
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246031250&usg=AOvVaw0vQEy27_o50oOuVLgABg4y)


  * Subscription List: [https://github.com/orgs/llvm/teams/pr-subscribers-offload](https://www.google.com/url?q=https://github.com/orgs/llvm/teams/pr-subscribers-offload&sa=D&source=editors&ust=1778600246031404&usg=AOvVaw3L5guIFGdPq9Am42E2updN)
  * Building the DeviceRTL / offload library
  * Moving to statically linking plugins


  * [https://github.com/llvm/llvm-project/pull/86683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/86683&sa=D&source=editors&ust=1778600246031626&usg=AOvVaw0Xz4S9K1K1RoD2LCORrDjE)


  * Compound/composite constructs in Flang (and Clang)
  * OpenMP version 5.2 as default


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * OpenMP Examples : 


  * target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

#pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);
