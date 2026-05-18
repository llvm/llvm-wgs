### January 28, 2026

Agenda

 

  * February 11 meeting canceled due to a conflict with Barcelona F2F.
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245884711&usg=AOvVaw238HwWGP6X3cEAFr3AZTGv)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245885140&usg=AOvVaw3Emn04vDxDzsC_fi5afuD6)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245885250&usg=AOvVaw13AOsLWf_Fcp91KljzZb_r) 
  * Any specific bugs to look at? 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245885865&usg=AOvVaw3wOhKRPzbeHiQYEmlWGDuV))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/169909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169909&sa=D&source=editors&ust=1778600245886039&usg=AOvVaw24uRhYe8y0tGmFDvME2uAm)
  * [https://github.com/llvm/llvm-project/pull/169638](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169638&sa=D&source=editors&ust=1778600245886154&usg=AOvVaw0pCxO7daootzHyHq7HPjO3)
  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245886273&usg=AOvVaw2baEs3OxKNhT6qPBedKvhN)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Extracted smaller PRs at reviewer request:


  * [https://github.com/llvm/llvm-project/pull/171610](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171610&sa=D&source=editors&ust=1778600245886513&usg=AOvVaw1UCjpHjWz-h8xU0R1aOqEc) 
  * [https://github.com/llvm/llvm-project/pull/177953](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/177953&sa=D&source=editors&ust=1778600245886644&usg=AOvVaw3possvW4x_JcPnOvo2mCjh)


  * Removing standalone/LLVM_ENABLE_PROJECTS build modes


  * [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1778600245886826&usg=AOvVaw14CHo3EXT017W9xaXPfQ3h)
  * [https://github.com/llvm/llvm-project/pull/152189](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152189&sa=D&source=editors&ust=1778600245886936&usg=AOvVaw2AwmojNGWhkcXKAZlCgs8K)
  * [https://github.com/llvm/llvm-project/pull/149878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149878&sa=D&source=editors&ust=1778600245887043&usg=AOvVaw1w_PywenCyObNdzTmWb1dq)
  * [https://github.com/llvm/llvm-project/pull/162904](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/162904&sa=D&source=editors&ust=1778600245887164&usg=AOvVaw0wgbyH7of5UNn-81_FZcYF)


  * Previous patches broke the documentation build for [llvm.org](https://www.google.com/url?q=http://llvm.org&sa=D&source=editors&ust=1778600245887279&usg=AOvVaw0k81KlGxaI0TyNiEJjvPMf)
  * Removing "standalone build" creates the impression that the build will always require LLVM to be built as well, which is not true.


  * [https://github.com/llvm/llvm-zorg/pull/699](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/699&sa=D&source=editors&ust=1778600245887514&usg=AOvVaw0TFphM1Z70Up-PV3vEDufr) ([docs][openmp] Switch to LLVM_ENABLE_RUNTIMES build)
  * [https://github.com/llvm/llvm-project/pull/176948](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176948&sa=D&source=editors&ust=1778600245887667&usg=AOvVaw0A0nMn0oK3PSap-J79hqIl) ([runtimes] Share doxygen handling with LLVM)
  * [https://github.com/llvm/llvm-zorg/pull/716](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/716&sa=D&source=editors&ust=1778600245887805&usg=AOvVaw37woOkeCO9jWYcjhp6UXd9) (rejected by maintainer)
  * [https://github.com/llvm/llvm-project/pull/178298](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/178298&sa=D&source=editors&ust=1778600245887932&usg=AOvVaw0FvEMK_HqTn1H5KbikyhIW) ([openmp] Build doxygen in bootstrapping builds)


  * Code style for LLVM OpenMP project:


  * About 5% in new LLVM coding style
  * Remainder in old KMP coding style
  * Which way should we be going?
  * ~100kloc, written in C++, but not using any C++ features that require linking C++ runtime
  * Joseph: remain consistent with what's already there, change the "new style" code back into the old style.


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245888543&usg=AOvVaw06TjR3oaZDPWxZpBgxroqL) (merged)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.
  * One more PR coming (for codegen): [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245888845&usg=AOvVaw3TW5dQTDsM2LuyvC-ck5GN)
  * 

  * Call for review:


  * Virtual function support:


  * [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245889059&usg=AOvVaw1J1yEVy2ZtBzFAux2IYOlq) 


  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245889195&usg=AOvVaw3YgxB-Th8hGulmlRfg6k8v), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245889256&usg=AOvVaw3V1EQXkLTxdamPDLnW3Sjp), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245889316&usg=AOvVaw2Fn4IDbymtWom_TQXEPahp))


  * Kevin: Performance degradation detected, needs few fixes


  * OMPT upstreaming plans from AMD


  * AMD plans to provide an update to this group on Feb 25th, 2026.



* * *
