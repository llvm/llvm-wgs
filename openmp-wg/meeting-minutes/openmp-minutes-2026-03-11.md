### March 11, 2026

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245871900&usg=AOvVaw0N4jUo4VUsTOrhRRGn6uRF)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245872326&usg=AOvVaw1FjazUAeU4nhX22ZqgtLnl)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245872440&usg=AOvVaw1RQ_PNwVHB7O_eMfZpAQ1M) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1778600245872541&usg=AOvVaw2u1FiJgI_WQUUOQc6IGNt7)
  * Any specific bugs to look at? 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces catn no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245873212&usg=AOvVaw2nP90HCoLtM1QrbXldYwPc))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/169909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169909&sa=D&source=editors&ust=1778600245873386&usg=AOvVaw1SJKBhvcmw4ppso40pyWPY) (merged)
  * [https://github.com/llvm/llvm-project/pull/169638](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169638&sa=D&source=editors&ust=1778600245873510&usg=AOvVaw3dnk6Ki6oZvLACj-YM_qgm) (merged)
  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245873648&usg=AOvVaw0GiBh2S0iC0w-PQar6QHtq)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Extracted smaller PRs at reviewer request:


  * [https://github.com/llvm/llvm-project/pull/171610](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171610&sa=D&source=editors&ust=1778600245873892&usg=AOvVaw31Z-1b9gTrokH3r0EdRfrQ) 
  * [https://github.com/llvm/llvm-project/pull/177953](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/177953&sa=D&source=editors&ust=1778600245874021&usg=AOvVaw2p4GHzaf-CIH4xiG2t0Phg)


  * Removing standalone/LLVM_ENABLE_PROJECTS build modes


  * [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1778600245874223&usg=AOvVaw0-Y7D4f_JDYW-ptjQWEFjk)


  * Talk about splitting this into openmp and offload


  * [https://github.com/llvm/llvm-project/pull/152189](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152189&sa=D&source=editors&ust=1778600245874441&usg=AOvVaw0n9oP2ntjxUu51uoNGqtt3) (merged)
  * [https://github.com/llvm/llvm-project/pull/149878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149878&sa=D&source=editors&ust=1778600245874570&usg=AOvVaw1W89hT4xWBaEAAdh-l1qT3) (merged)
  * [https://github.com/llvm/llvm-project/pull/162904](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/162904&sa=D&source=editors&ust=1778600245874723&usg=AOvVaw14Myl0ZgnLJvOQyaJFqJ6B) (closed)


  * Previous patches broke the documentation build for [llvm.org](https://www.google.com/url?q=http://llvm.org&sa=D&source=editors&ust=1778600245874868&usg=AOvVaw0suQLlB6jHzO639zzcQAJl)
  * Removing "standalone build" creates the impression that the build will always require LLVM to be built as well, which is not true.


  * [https://github.com/llvm/llvm-zorg/pull/699](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/699&sa=D&source=editors&ust=1778600245875125&usg=AOvVaw0V0uuudCMA9E9bNfVV70n8) (merged)


  * ([docs][openmp] Switch to LLVM_ENABLE_RUNTIMES build)


  * [https://github.com/llvm/llvm-project/pull/176948](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176948&sa=D&source=editors&ust=1778600245875347&usg=AOvVaw2z-cAWjfnaX0YMGJ5LUa-B) (merged)


  * ([runtimes] Share doxygen handling with LLVM)


  * [https://github.com/llvm/llvm-zorg/pull/716](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/716&sa=D&source=editors&ust=1778600245875541&usg=AOvVaw3jeiQOWzyLYCs3p0mSIaOU) (closed)


  * (rejected by maintainer)


  * [https://github.com/llvm/llvm-project/pull/178298](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/178298&sa=D&source=editors&ust=1778600245875717&usg=AOvVaw3PUYYmasjOKNyUfBTkVYRa) (merged)


  * ([openmp] Build doxygen in bootstrapping builds)


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245875973&usg=AOvVaw0_nItxd8CCgUdPVD6uzzW3) (merged)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.
  * One more PR coming (for codegen): [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245876273&usg=AOvVaw3ZR65aDjlUOPugo3dfKZen) (merged)


  * Modern libomp development


  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1778600245876490&usg=AOvVaw11xJnQUcjR7UtUHoByHwE5)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1778600245876635&usg=AOvVaw0VZx9QJ7LJyd_pupDXtZrn)
  * libomp is C++-ish, but should not link against the C++ stdlib
  * Most C++ stdlib features (e.g. std::vector) cannot be used
  * LLVM features, such as llvm::StringRef or llvm::SmallVector, cannot be used
  * -> introduce Advanced Data Types for libomp (currently kmp_str_ref and kmp_vector) to improve the development situation and make new features, such as [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1778600245877181&usg=AOvVaw19oSSVPMbgqrgxCtq2TsT1), more streamlined and less annoying to review


  * OMPT presentation:


  * Requesting feedback
  * Questions/requests:


  * Could multiple profilers be supported?
  * Could profilers be selected at runtime instead of build time?


  * Out of scope for the current effort.  May be implemented later.
  * There is currently only one profiler, which is enabled via #ifdef in the source code.


  * How will the current implementation be affected when libomptarget is implemented on top of liboffload?
  * Could there be filtering mechanisms (e.g. to only trace interactions between the host and the device)?


  * The preference of the community is for the work to be done upstream


  * Call for review:

* * *
