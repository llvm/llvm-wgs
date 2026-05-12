### 2025, July 30

Agenda

 

  * Discuss 5.2 and 6.0 features


  * omp_target_is_accessible - may need to be modified in the spec, we can implement 5.2 behavior for now


  * 5.2: the pointer passed is a valid host pointer
  * 6.0: the pointer passed is a pointer
  * Nicole: still working on the implementation. ([#138294](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/138294&sa=D&source=editors&ust=1778600245939382&usg=AOvVaw1siKBubKgVtoDacqLAydB0))


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245939533&usg=AOvVaw35BOii5QBZ5QN4u15qGWZ4)        
  * OpenMP version 5.2 as default


  * Worthwhile to update to 5.2 as default, but needs more thorough review


  * Make sure all the new features are guarded by a warning
  * Updating the version itself implies changing lots of tests
  * Catherine with help, Deepak: will do the assessment


  * Catherine: updated webpage with items that AMD is working on (for 6.0).
  * Deepak: still working on this


  * Could go straight to 6.0 and not bother with 5.2 at all


  * Not ready


  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245940245&usg=AOvVaw2Q7Za0gEfbA4pXkyROX9Hp) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * The OpenMPSupport.rst document linked above
  * Nicole: when should we be updating this document?  Another PR emerged implementing the same feature as one already in progress.
  * Open a PR and add mjklemm and/or jhuber as reviewers, open it when the work starts to avoid duplication of effort.


  * Generic SPMD kernel detection


  * Previous PR closed [https://github.com/llvm/llvm-project/pull/137307](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/137307&sa=D&source=editors&ust=1778600245940850&usg=AOvVaw1hFvgectsw3vtagCmEccCq)
  * Change of approach, new PR: [https://github.com/llvm/llvm-project/pull/150922](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/150922&sa=D&source=editors&ust=1778600245940990&usg=AOvVaw06h6UXwgV2v4GETZGocx0A)


  * Remove from agenda.


  * Bug(s) that needs looking into:


  * any? 


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events).


  * Upstream PR opened  
[https://github.com/llvm/llvm-project/pull/147381](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/147381&sa=D&source=editors&ust=1778600245941363&usg=AOvVaw074y9vs-erZNZ0Uo_xyj3o)


  * Please review
  * Michael Klemm will contact Intel people for review


  * Downstream implementation  
[https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245941633&usg=AOvVaw2spKBW6VWtvVevFm-x-c03)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245941807&usg=AOvVaw2_RQAAufnMR5caEsdHaYGh) 


  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * Call for review:


  * [[OFFLOAD][OPENMP] 6.0 compatible interop interface by adurang * Pull Request #143491 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/143491&sa=D&source=editors&ust=1778600245942158&usg=AOvVaw2SUpi4m5NbCDqKHr2oiWc4)
  * [[Offload] Introduce ATTACH map-type support for pointer attachment. by abhinavgaba * Pull Request #149036 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149036&sa=D&source=editors&ust=1778600245942346&usg=AOvVaw3TYbVHjeh-FvsZaVAtkqKG)


  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245942593&usg=AOvVaw3D_Icz6VLp8ubDJZQSfGVS) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245942768&usg=AOvVaw3WkCN8MlcMCy_MMLGfMhqN)


  * 


* * *

# Previous Meeting
