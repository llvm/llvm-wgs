### February 25, 2026

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245878397&usg=AOvVaw1m0rnu5Pa5qbNWLuOg-XRQ)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * OMPT upstreaming plans from AMD


  * AMD plans to provide an update to this group on Feb 25th, 2026.


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245878931&usg=AOvVaw0hsGzvpHgwgFVPYAubkYk4)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245879035&usg=AOvVaw0_KaQrQOHFm7ul1Y3sGBMx) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1778600245879133&usg=AOvVaw1AZqBXYq5RMxv0WzxMEUCy)
  * Any specific bugs to look at? 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245879758&usg=AOvVaw2aqKemeoN3QrleTNVB56dY))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/169909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169909&sa=D&source=editors&ust=1778600245879957&usg=AOvVaw2tk1PKMS_FPIF830h6bkkj) (merged)
  * [https://github.com/llvm/llvm-project/pull/169638](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169638&sa=D&source=editors&ust=1778600245880135&usg=AOvVaw3oRmr7oZ96NY5pH_q_qVBT) (merged)
  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245880268&usg=AOvVaw3eTHI9lTJNvV_Tgjk2Er2h)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Extracted smaller PRs at reviewer request:


  * [https://github.com/llvm/llvm-project/pull/171610](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171610&sa=D&source=editors&ust=1778600245880514&usg=AOvVaw3m7Z4QwPFeM1wapsrVCxj5) 
  * [https://github.com/llvm/llvm-project/pull/177953](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/177953&sa=D&source=editors&ust=1778600245880636&usg=AOvVaw09LIHauCte_TMGbo2dAhmR)


  * Removing standalone/LLVM_ENABLE_PROJECTS build modes


  * [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1778600245880830&usg=AOvVaw2WRP_XYAjly2D0Ejvq_6II)
  * [https://github.com/llvm/llvm-project/pull/152189](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152189&sa=D&source=editors&ust=1778600245880941&usg=AOvVaw3R792kkEqaCZ53jsdCfZnr) (merged)
  * [https://github.com/llvm/llvm-project/pull/149878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149878&sa=D&source=editors&ust=1778600245881067&usg=AOvVaw05jy9V_8Gx64b3IouWdhyE) (merged)
  * [https://github.com/llvm/llvm-project/pull/162904](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/162904&sa=D&source=editors&ust=1778600245881217&usg=AOvVaw2Lwxg9iRgl_uJ_aiEE4gfk) (closed)


  * Previous patches broke the documentation build for [llvm.org](https://www.google.com/url?q=http://llvm.org&sa=D&source=editors&ust=1778600245881361&usg=AOvVaw2Sl4dtmhEBPyauRrQ1lrVA)
  * Removing "standalone build" creates the impression that the build will always require LLVM to be built as well, which is not true.


  * [https://github.com/llvm/llvm-zorg/pull/699](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/699&sa=D&source=editors&ust=1778600245881603&usg=AOvVaw1McN-wXJy_ikxHDI9L_k-6) (merged)


  * ([docs][openmp] Switch to LLVM_ENABLE_RUNTIMES build)


  * [https://github.com/llvm/llvm-project/pull/176948](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176948&sa=D&source=editors&ust=1778600245881804&usg=AOvVaw00iEZtGHSfIbL2GKRk5FrQ) (merged)


  * ([runtimes] Share doxygen handling with LLVM)


  * [https://github.com/llvm/llvm-zorg/pull/716](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/716&sa=D&source=editors&ust=1778600245882020&usg=AOvVaw2i51QAL5QAvs8KtCCs778s) (closed)


  * (rejected by maintainer)


  * [https://github.com/llvm/llvm-project/pull/178298](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/178298&sa=D&source=editors&ust=1778600245882217&usg=AOvVaw0lr29HxUacIm-le51Iujrf) (merged)


  * ([openmp] Build doxygen in bootstrapping builds)


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245882468&usg=AOvVaw2hSi8fTw5hhcnWlGUpyl8f) (merged)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.
  * One more PR coming (for codegen): [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245882761&usg=AOvVaw1QIbFutiiaNYmi--03TXLD)


  * Modern libomp development


  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1778600245882944&usg=AOvVaw3oMWxbb2AbAwPk6p7a_FaK)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1778600245883085&usg=AOvVaw1AzbWUSYVIMnjr0VVBdUwt)
  * libomp is C++-ish, but should not link against the C++ stdlib
  * Most C++ stdlib features (e.g. std::vector) cannot be used
  * LLVM features, such as llvm::StringRef or llvm::SmallVector, cannot be used
  * -> introduce Advanced Data Types for libomp (currently kmp_str_ref and kmp_vector) to improve the development situation and make new features, such as [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1778600245883611&usg=AOvVaw163CimdRRoW3VIqKUBM7aK), more streamlined and less annoying to review


  * Call for review:


  * Virtual function support:


  * [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245883858&usg=AOvVaw3jl_spuV9l_WQTh1QKb6kU) 


  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245883986&usg=AOvVaw1-X70Jbp4998koUHGp0jSi), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245884041&usg=AOvVaw0QpXDNv04TN9D8HXc1jm2Y), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245884096&usg=AOvVaw1RnYGvc8Zg_mqHSsbBv5rZ))


  * Kevin: Fix approved by lang committee; PR update coming soon



* * *

  *
