### September 10, 2025

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245926266&usg=AOvVaw37b4VOPTLvnIv2bZrD6Cbe)        
  * Nicole: when should we be updating this document?  Another PR emerged implementing the same feature as one already in progress.
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Discuss 5.2 and 6.0 features


  * OpenMP version 5.2 as default


  * Worthwhile to update to 5.2 as default, but needs more thorough review


  * Make sure all the new features are guarded by a warning
  * Updating the version itself implies changing lots of tests
  * Catherine with help, Deepak: will do the assessment


  * Catherine: updated webpage with items that AMD is working on (for 6.0).
  * Deepak: very few 5.2 features are actually complete
  * Not ready yet
  * Solvve tests could be used for validation


  * Bug(s) that needs looking into:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245927432&usg=AOvVaw2ZXuDrBgQBPnMxai8YZXJl)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245927548&usg=AOvVaw3EQ6mwmOiPt1eWrz2IpdtX) 
  * Any specific bugs to look at? 


  * OMPT upstreaming plans from AMD


  * Device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs
  * First OMPT PR has landed: [https://github.com/llvm/llvm-project/pull/154786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154786&sa=D&source=editors&ust=1778600245927942&usg=AOvVaw33V-0BwzOyp7hJGw2YeSHi) 
  * Next step: downstream code work to incorporate changes from upstream and work on reducing potential conflicts; refactoring into an abstraction layer.
  * Update and request for discussion to follow soon.


  * Call for review:


  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245928351&usg=AOvVaw2AGK5c1d2lBlMEO02nD9f8), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245928415&usg=AOvVaw30BwibqmVP6R3uP8akbysb), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245928471&usg=AOvVaw3yFylLMXSpiGS3_kmvAQ5K))
  * [OpenMP][Clang] Use ATTACH map-type for list-items with base-pointers. ([#153683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/153683&sa=D&source=editors&ust=1778600245928622&usg=AOvVaw2RcQtTqgUStIGhhlgse8sK), NFC Subset with utils/helpers: [#155625](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155625&sa=D&source=editors&ust=1778600245928708&usg=AOvVaw052sW-pJrnFkxX8nnKK76x))


  * Please test the first PR
  * Julian has run some tests and they all passed
  * Alexey will review the helper PR


  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245929107&usg=AOvVaw3byp3q92rJf_LuWC4bimO5) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245929312&usg=AOvVaw0PLaSPGCvDlBZoPbFOo2Rl)


  * Need to change cmake used to configure LLVM
  * [https://github.com/llvm/llvm-project/blob/main/offload/cmake/caches/Offload.cmake](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/offload/cmake/caches/Offload.cmake&sa=D&source=editors&ust=1778600245929522&usg=AOvVaw3Qn3qKdRZI35RAsdVy83sm)
  * Also described in OpenMP documentation


  * Plans to upstream of Level Zero Plugin (Intel/Alex)


  * Finalizing plans for upstreaming of level 0 plugin
  * What's the best way to review it?  It's a large amount of code.
  * A PR should be ready in the next few days


  * Move libomptarget on top of liboffload


  * Alejandro: started looking into this
  * Call some functions from liboffload, others from plugins
  * Need to link libomptarget statically into liboffload for some time
  * Assume that there is a single plugin present for now
  * Joseph: turn liboffload into object library



* * *

* * *
