### 2024, June 19

Agenda 

New 

  * KernelArgsTy :  Vendor specific field
  * OpenMP transparent tasks:


  * What is the community's feeling on the transparent tasks discussion in the language committee and potential implementation in the LLVM libomp runtime?
  * Is there some interest to try to get an implementation going to get some better idea of the feature impact before the TR of OpenMP 6.0 or something?


  * Task Graph
  * Target data as a task generating construct
  * Subscription List: [https://github.com/orgs/llvm/teams/pr-subscribers-offload](https://www.google.com/url?q=https://github.com/orgs/llvm/teams/pr-subscribers-offload&sa=D&source=editors&ust=1778600246023615&usg=AOvVaw04QTj-SoZtQCZf5SjVzxrt)
  * Building the DeviceRTL / offload library
  * Compound/composite constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm.


  * OpenMP version 5.2 as default


  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246023997&usg=AOvVaw08N-Y-8O6gs_-SbW5Hk93S) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * OpenMP Examples : 


  * target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

#pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);
