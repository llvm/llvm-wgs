### January 14, 2026

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245890015&usg=AOvVaw34Yn8aRfXlYuwMKdC14lcv)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245890431&usg=AOvVaw2X628eeXndSxAfHJ_tuC13)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245890535&usg=AOvVaw3OuYlA4OywsW6SAEqdxqum) 
  * Any specific bugs to look at? 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245891202&usg=AOvVaw0-N-AF-ZLtsEXhZRR7Taav))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/169909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169909&sa=D&source=editors&ust=1778600245891374&usg=AOvVaw3pbt1-DRAyz22UnXk5PGYh)
  * [https://github.com/llvm/llvm-project/pull/169638](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169638&sa=D&source=editors&ust=1778600245891488&usg=AOvVaw2UgSVN-LX540Ut9pznKZGp)
  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245891598&usg=AOvVaw00WLgfpP_vv9e7OT9jiJ61)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * https://github.com/llvm/llvm-project/pull/171610


  * Make the change first, then refactor in a separate PR


  * Removing standalone/LLVM_ENABLE_PROJECTS build modes


  * [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1778600245892003&usg=AOvVaw00_Od56xttl9LXYaBMBzOf)
  * [https://github.com/llvm/llvm-project/pull/152189](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152189&sa=D&source=editors&ust=1778600245892116&usg=AOvVaw1_CmUc3jpin-rs8ohneWnc)
  * [https://github.com/llvm/llvm-project/pull/149878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149878&sa=D&source=editors&ust=1778600245892231&usg=AOvVaw22mT8C91CRk3z7bixHz0Jc)
  * [https://github.com/llvm/llvm-project/pull/162904](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/162904&sa=D&source=editors&ust=1778600245892346&usg=AOvVaw2IxZoSznJJLtz2q3x_7sHv)


  * Previous patches broke the documentation build for [llvm.org](https://www.google.com/url?q=http://llvm.org&sa=D&source=editors&ust=1778600245892483&usg=AOvVaw368iNRCDAkHqyHcF8Iol2W)
  * Removing "standalone build" creates the impression that the build will always require LLVM to be built as well, which is not true.


  * Code style for LLVM OpenMP project:


  * About 5% in new LLVM coding style
  * Remainder in old KMP coding style
  * Which way should we be going?
  * ~100kloc, written in C++, but not using any C++ features that require linking C++ runtime


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245893084&usg=AOvVaw0a_9Sxf0r18cZHI248Row2)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.
  * One more PR coming (for codegen): [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245893396&usg=AOvVaw1FqC8x3p0S03EnDhjG-yFG)
  * 

  * Call for review:


  * Virtual function support:


  * [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245893619&usg=AOvVaw0RNs9ONPMuqRQ5IGTSgYOS) 


  * CMake improvement: [https://github.com/llvm/llvm-project/pull/159416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159416&sa=D&source=editors&ust=1778600245893756&usg=AOvVaw3ugxomCr-UwIwS91672g7n)
  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245893882&usg=AOvVaw1PB6mrJ6Q_avhq0A4dGWSK), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245893942&usg=AOvVaw3rMpS_G6OBJ88QcutGWU8a), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245893997&usg=AOvVaw0dQsq30_fdFPPoLjGR2ETv))


  * Kevin: Performance degradation detected, needs few fixes


  * [OpenMP][Offload] Add a buffer layer to debug messaging ([https://github.com/llvm/llvm-project/pull/172446](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/172446&sa=D&source=editors&ust=1778600245894249&usg=AOvVaw3d5jT6LakHbI-p0QVzesYa))
  * [OpenMP][Offload] Translate Info types to Debug types when debug enabled ([https://github.com/llvm/llvm-project/pull/175599](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/175599&sa=D&source=editors&ust=1778600245894436&usg=AOvVaw3eC-7ZKc7ZgLktlKYJ6VVx))
  * [OpenMP] Preserve the original address when use_device_ptr/addr lookup fails. ([#174659](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174659&sa=D&source=editors&ust=1778600245894589&usg=AOvVaw1r2WYDpOwYUzwrZ_sfbXiY))


  * \+ the stack for use_device_ptr(fb_nullify/preserve): [#169603](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169603&sa=D&source=editors&ust=1778600245894758&usg=AOvVaw1IlF5OOJvQHDIPc36GC9vH), [#170578](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170578&sa=D&source=editors&ust=1778600245894817&usg=AOvVaw1HuD6cKRv4Y8UlmY1Tb8OQ), [#173930](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/173930&sa=D&source=editors&ust=1778600245894875&usg=AOvVaw2nhVKGCjbfBfJ7SLZnNMSY), [#173931](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/173931&sa=D&source=editors&ust=1778600245894933&usg=AOvVaw20nKVsxlQ_AV9vOdlkXJSP) 


  * [https://github.com/llvm/llvm-project/pull/171201](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171201&sa=D&source=editors&ust=1778600245895047&usg=AOvVaw1oU_9tno7HdNcrsVxjW6Tn) 


  * Should this wait until the follow-up PR is ready?
  * Kevin: Delayed until next LLVM branch


  * OMPT upstreaming plans from AMD


  * AMD is working on an updated timeline for further PRs to be published.

* * *
