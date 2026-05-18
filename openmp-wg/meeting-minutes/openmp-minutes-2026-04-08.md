### April 8, 2026

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245860622&usg=AOvVaw0zAnkwPVGmhmQmnD7YHld2)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245861049&usg=AOvVaw1Gaq4_d2Qb983MV_Ic-zPV)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245861161&usg=AOvVaw0h7ounMRC-7qYn6NHi5JeI) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1778600245861257&usg=AOvVaw3b3qxZTZ5lTOy2tsMKq8ra)
  * Any specific bugs to look at? 


  * Move (Flang) OpenMP extensions from OpenMPSupport.md to OpenMP-extensions.md.


  * PR: [https://github.com/llvm/llvm-project/pull/186981](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/186981&sa=D&source=editors&ust=1778600245861524&usg=AOvVaw0vdCENtNNC_rgPDPWrV0qi)


  * PR [https://github.com/llvm/llvm-project/pull/188434](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/188434&sa=D&source=editors&ust=1778600245861675&usg=AOvVaw1wJG1kZF7ERVhW9X8wWZHv) to fix "broken" -W options for OpenMP.


  * RFC: [https://discourse.llvm.org/t/openmp-misspelling-of-wopen-mp/90196](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-misspelling-of-wopen-mp/90196&sa=D&source=editors&ust=1778600245861880&usg=AOvVaw1o2oqJeL3XS4bWBdUtz-3M) 
  * Will remain open until the end of April for visibility.


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245862130&usg=AOvVaw3iwWWqEFKfSJtRDSPGEJs7)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Extracted smaller PRs at reviewer request:


  * [https://github.com/llvm/llvm-project/pull/171610](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171610&sa=D&source=editors&ust=1778600245862382&usg=AOvVaw0OmqyOqRozj70vj8Q3A7_u) (approved under condition that @petrhosek also approves)
  * [https://github.com/llvm/llvm-project/pull/177953](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/177953&sa=D&source=editors&ust=1778600245862546&usg=AOvVaw0tcLroq9DQM23ybxEIDEXW) (merged)
  * [https://github.com/llvm/llvm-project/pull/187868](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187868&sa=D&source=editors&ust=1778600245862660&usg=AOvVaw2bsIL92Yxaja9v1U4B5iB5) (merged)


  * Modern libomp development


  * New (2026-04-08): [Meta RFC: ADTs without C++ runtime dependency - LLVM Project - LLVM Discussion Forums](https://www.google.com/url?q=https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317&sa=D&source=editors&ust=1778600245862903&usg=AOvVaw3tyq31ILOiAe81-AZKlk_l)
  * Runtime needs to parse context-selectors, for that using certain C++/LLVM runtime utilities can help.
  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1778600245863174&usg=AOvVaw0F0LhVpLgHnHcHihVnslqm)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1778600245863332&usg=AOvVaw04U7xlQO2NiEmHzJVQyWNN)
  * libomp is C++-ish, but should not link against the C++ stdlib
  * Most C++ stdlib features (e.g. std::vector) cannot be used
  * LLVM features, such as llvm::StringRef or llvm::SmallVector, cannot be used (because they can use C++ runtime features internally)
  * -> introduce Advanced Data Types for libomp (currently kmp_str_ref and kmp_vector) to improve the development situation and make new features, such as [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1778600245863895&usg=AOvVaw0gywTRG3zAUZeInQ2mGv_8), more streamlined and less annoying to review
  * Joachim: Sanitizers have a similar restriction, they supply their own implementations of certain data structures.
  * Michael: Same for flang-rt.
  * Abhinav: liboffload uses llvm::SmallVector, why libomp can't?
  * Joachim: liboffload is only usable with clang, libomp can be used with a variety of compilers.
  * Michael: Using liboffload with flang is also sub-optimal.
  * Alex: Why does it matter that C++RT would be required? We could statically link the C++RT if ABI compatibility is the issue
  * Joachim: maybe we could still use C++RT but with all names inside of some namespace to avoid mismatches with names from different C++RT implementations.
  * Michael: libc contains copies of libc++ standard headers to be independent from the actual C++ implementation.
  * For now: proceed with the PRs as an interim solution until the common runtime discussion is finalized


  * Call for review:
  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245865548&usg=AOvVaw04IaHqiEesDhiRAJts9Q-s))


  * Michael is testing this with different OSs.


  * In old-school Fortran, where nothing is declared, the compiler will mangle RT names in ways that are incompatible with this implementation.  This is a blocker, since there is still a lot of code that follows that.

* * *
