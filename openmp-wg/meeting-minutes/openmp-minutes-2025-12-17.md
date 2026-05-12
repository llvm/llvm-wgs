### December 17, 2025

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245895751&usg=AOvVaw3y5egUo61wHA_M8QwQ1ryb)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245896166&usg=AOvVaw2w9-VgXbe8iJDlBtlgXw8J)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245896274&usg=AOvVaw2g93X7OUACgKx0l4Y6C2yI) 
  * Any specific bugs to look at? 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245896902&usg=AOvVaw1klOtrWEUi79tLK-QxKcjM))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/169909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169909&sa=D&source=editors&ust=1778600245897086&usg=AOvVaw1-hlAq816yQJbIC5dzzaLd)
  * [https://github.com/llvm/llvm-project/pull/169638](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169638&sa=D&source=editors&ust=1778600245897208&usg=AOvVaw1PHP8stmO7gxh1oj5rnPTU)
  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245897327&usg=AOvVaw0kjkc2QklvSVe9SU8jH4r7)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Removing standalone/LLVM_ENABLE_PROJECTS build modes


  * [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1778600245897582&usg=AOvVaw3g3y9MaueLGf_i_I1-LzUr)
  * [https://github.com/llvm/llvm-project/pull/152189](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152189&sa=D&source=editors&ust=1778600245897701&usg=AOvVaw2PhDNUxv4EVGRkaERIIZEq)
  * [https://github.com/llvm/llvm-project/pull/149878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149878&sa=D&source=editors&ust=1778600245897814&usg=AOvVaw0FeGa14uAwabFC9gv0iavF)
  * [https://github.com/llvm/llvm-project/pull/162904](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/162904&sa=D&source=editors&ust=1778600245897924&usg=AOvVaw1QuzrKu_YnDmkWhSy8a1U0)
  * 

  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245898124&usg=AOvVaw2ycBXhbSJZBN41l7OxIYcw)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.
  * One more PR coming (for codegen): [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245898467&usg=AOvVaw3l3hvMJWgL5yLQ6ogOP2rU)


  * Fine-grained debug support (Intel/Alex) ([https://github.com/llvm/llvm-project/pull/165416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/165416&sa=D&source=editors&ust=1778600245898624&usg=AOvVaw3Qa7sTGDOVfzvM8X-cAIYl))


  * Filter things that get output
  * Joseph: two prints, debug and informational.  Deprecate LIBOMPTARGET_DEBUG flag in cmake and use NDEBUG instead
  * Alex: still want to have different debug configurations, get debug support even when LLVM is build with NDEBUG.
  * Joseph: have a flag and use "flag || !NDEBUG" to enable debug prints
  * Have a list of keywords to enable debug prints from different parts, keep backward compatibility with "1", use "all" for everything
  * Alex: there are also debug levels
  * Alex where should this live?  There is some data that shouldn't be in a header file
  * Joseph: use it for liboffload first.  Have it in a header and recompute it in different places at first use.
  * Joseph: when adding a new feature it's hard to determine what level to put it under, using tags should be enough
  * Alex: disagrees, if a component wants to support levels, there would need to be additional tags for each level (for the same component).
  * Joseph: do we really need to have a complicated mechanism for this?
  * Alex: users wanted different levels to limit the amount of information
  * Joseph: it should be easy for people to write new code that uses this functionality
  * Alex: in the absence of levels people tend to print too little debug information
  * Michael Klemm: Users say that the debugging experience in LLVM is difficult and complicated.  Have a single way to control debugging of OpenMP-related code (not specific to liboffload and libomptarget). In the future it could be extended to libomp.
  * Alex: this makes sense, but not clear where/how to implement it


  * The code would have to live somewhere, there is no code in common with libomp at the moment


  * Consensus has been reached, now implementing the changes.
  * Need help with adopting plugins to use the new messages (e.g. AMD plugin).
  * 

  * Call for review:


  * Virtual function support:


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245900702&usg=AOvVaw0GxaaXEylFb7Y96PL5Dwy0)
  * [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245900829&usg=AOvVaw2XzkL-4ZCOtFIb1t98FaLb) 


  * CMake improvement: [https://github.com/llvm/llvm-project/pull/159416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159416&sa=D&source=editors&ust=1778600245900972&usg=AOvVaw1kxefz3KFM0q0gbLuqLq8_)
  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245901103&usg=AOvVaw3nyGF863ryMP4ESdl-G5SH), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245901184&usg=AOvVaw3uzundU-yY7BRoOleTh7CP), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245901245&usg=AOvVaw2DaoqWjDZTAFLiFGWQj-E6))


  * Kevin: Performance degradation detected, needs few fixes


  * [OpenMP][Offload] Add a buffer layer to debug messaging ([https://github.com/llvm/llvm-project/pull/172446](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/172446&sa=D&source=editors&ust=1778600245901493&usg=AOvVaw0Gxb-3rHZnyQPM3BrUmFPF))
  * [[OFFLOAD] Add plugin with support for Intel oneAPI Level Zero by adurang * Pull Request #158900 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245901664&usg=AOvVaw0YheQiMsSrGGtufEC62jiI) 
  * [https://github.com/llvm/llvm-project/pull/171201](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171201&sa=D&source=editors&ust=1778600245901781&usg=AOvVaw1zmhLCsUEPSdwhnfmDkRMs) 


  * Should this wait until the follow-up PR is ready?
  * Kevin: Delayed until next LLVM branch


  * OMPT upstreaming plans from AMD


  * AMD is working on an updated timeline for further PRs to be published.

* * *
