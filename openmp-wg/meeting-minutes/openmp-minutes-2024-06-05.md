### 2024, June 5

Agenda 

New 

  * KernelArgsTy :  Vendor specific field
  * OpenMP hull tasks:


  * What is the community's feeling on the hull tasks discussion in the language committee and potential implementation in the LLVM libomp runtime?
  * Is there some interest to try to get an implementation going to get some better idea of the feature impact before the TR of OpenMP 6.0 or something?


  * Subscription List: [https://github.com/orgs/llvm/teams/pr-subscribers-offload](https://www.google.com/url?q=https://github.com/orgs/llvm/teams/pr-subscribers-offload&sa=D&source=editors&ust=1778600246025050&usg=AOvVaw1Q-_O9iz-7dap2fcKKYtc1)
  * Building the DeviceRTL / offload library
  * Compound/composite constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm.


  * OpenMP version 5.2 as default


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * OpenMP Examples : 


  * target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

#pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);
