### 2025, August 13

Agenda

 

  * Discuss 5.2 and 6.0 features


  * omp_target_is_accessible - may need to be modified in the spec, we can implement 5.2 behavior for now


  * 5.2: the pointer passed is a valid host pointer
  * 6.0: the pointer passed is a pointer
  * Nicole: still working on the implementation. ([#138294](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/138294&sa=D&source=editors&ust=1778600245934683&usg=AOvVaw1QICgaMPcpFVrGvLrtcNst))


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245934841&usg=AOvVaw26G-oMjr5Q56pniPCtxJ4E)        
  * OpenMP version 5.2 as default


  * Worthwhile to update to 5.2 as default, but needs more thorough review


  * Make sure all the new features are guarded by a warning
  * Updating the version itself implies changing lots of tests
  * Catherine with help, Deepak: will do the assessment


  * Catherine: updated webpage with items that AMD is working on (for 6.0).
  * Deepak: still working on this


  * Could go straight to 6.0 and not bother with 5.2 at all


  * Not ready


  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245935641&usg=AOvVaw1pVUMW34yo43oNlG_GNARr) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * The OpenMPSupport.rst document linked above
  * Nicole: when should we be updating this document?  Another PR emerged implementing the same feature as one already in progress.
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Bug(s) that needs looking into:


  * any? 


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events).


  * Upstream PR opened  
[https://github.com/llvm/llvm-project/pull/147381](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/147381&sa=D&source=editors&ust=1778600245936530&usg=AOvVaw0F9Q8fMoM_b32iUaJYahYK)


  * Got positive feedback so far
  * Feel free to chime in if you have any comments
  * This is the precursor to JP's downstream work on refactoring the general architecture of OMPT, will be upstreamed when ready


  * Downstream implementation  
[https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245936945&usg=AOvVaw2m6G5e9fwCf0k4ito-VvO2)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245937153&usg=AOvVaw2wMOMQXyUEQBSzG_y2LgE_) 


  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * Call for review:


  * [[Offload] Introduce ATTACH map-type support for pointer attachment. by abhinavgaba * Pull Request #149036 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149036&sa=D&source=editors&ust=1778600245937521&usg=AOvVaw3y7CEJG5gfovrN8GvYWJpX)
  * Joseph: extracting OpenMP-specific parts can happen in a separate PR
  * # [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245937757&usg=AOvVaw31kIJDZAQQgnqAGRYvRAwk), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245937820&usg=AOvVaw1uMFunsHGgJxpQlWGn1als), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245937879&usg=AOvVaw0HFn-UPQJcNKVH-mt1yiFQ))



  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245938205&usg=AOvVaw3W1ZE4pzaSemmrPrEPkUWO) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245938388&usg=AOvVaw2lgfKTIhtvqFssFbiz-X8j)


  * Move libomptarget on top of liboffload


  * Alejandro: started looking into this
  * Call some functions from liboffload, others from plugins
  * Need to link libomptarget statically into liboffload for some time
  * Assume that there is a single plugin present for now
  * Joseph: turn liboffload into object library



* * *
