### August 27, 2025

Agenda

 

  * Discuss 5.2 and 6.0 features


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245930644&usg=AOvVaw0O7utm0c87iTc2Us_9sf45)        
  * OpenMP version 5.2 as default


  * Worthwhile to update to 5.2 as default, but needs more thorough review


  * Make sure all the new features are guarded by a warning
  * Updating the version itself implies changing lots of tests
  * Catherine with help, Deepak: will do the assessment


  * Catherine: updated webpage with items that AMD is working on (for 6.0).
  * Deepak: still working on this


  * Could go straight to 6.0 and not bother with 5.2 at all


  * Not ready


  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245931371&usg=AOvVaw3P1SC37PKhtTNJsy1VIDVc) 


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * The OpenMPSupport.rst document linked above
  * Nicole: when should we be updating this document?  Another PR emerged implementing the same feature as one already in progress.
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Bug(s) that needs looking into:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245932069&usg=AOvVaw09FaXRGzVMt9TOT0LpjZfk)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245932175&usg=AOvVaw0AJwxBoVWLQzTP70CT0Rbh) 
  * Any specific bugs to look at? 


  * OMPT upstreaming plans from AMD


  * Device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs
  * First OMPT PR has landed: [https://github.com/llvm/llvm-project/pull/154786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154786&sa=D&source=editors&ust=1778600245932528&usg=AOvVaw2dbbig5n-a_74a83wsJddh) 
  * Next step: downstream code work to incorporate changes from upstream and work on reducing potential conflicts; refactoring into an abstraction layer.
  * Update and request for discussion to follow soon.


  * Call for review:


  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245932942&usg=AOvVaw3l23NAgxHXrD9Ijll1WHTa), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245933004&usg=AOvVaw2DR6ayaHsVl6eTM2SJwi2q), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245933061&usg=AOvVaw284ct3hnJ5GqFzubX1s0Y9))
  * [OpenMP][Clang] Use ATTACH map-type for list-items with base-pointers. ([#153683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/153683&sa=D&source=editors&ust=1778600245933212&usg=AOvVaw12NEwbInzhUAYgpzJGwzt-), NFC Subset with utils/helpers: [#155625](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155625&sa=D&source=editors&ust=1778600245933298&usg=AOvVaw28y9whb1HrV4vuP4U2MWz1))


  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245933544&usg=AOvVaw36sGOjsisvWxs43HQrB9TY) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245933718&usg=AOvVaw3R3b54bDhVySV7WiUd72us)


  * Move libomptarget on top of liboffload


  * Alejandro: started looking into this
  * Call some functions from liboffload, others from plugins
  * Need to link libomptarget statically into liboffload for some time
  * Assume that there is a single plugin present for now
  * Joseph: turn liboffload into object library



* * *
