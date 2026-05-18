### April 22, 2026

Agenda

 

  * May 6 meeting canceled due to OpenMP F2F.
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245854053&usg=AOvVaw3TBV6umOdXlRwhfM5Co7DB)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245854509&usg=AOvVaw0wlrBCwgoCAp1UHhibMrui)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245854620&usg=AOvVaw1wT9kEvpYBZEjjFATHPmqd) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1778600245854712&usg=AOvVaw2mOa9f5NBlRquLtaSNyhrr)
  * Any specific bugs to look at? 


  * Move (Flang) OpenMP extensions from OpenMPSupport.md to OpenMP-extensions.md.


  * PR: [https://github.com/llvm/llvm-project/pull/186981](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/186981&sa=D&source=editors&ust=1778600245855018&usg=AOvVaw1xE2d9q6SIJRq3moFuCGWv) \- merged


  * PR [https://github.com/llvm/llvm-project/pull/188434](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/188434&sa=D&source=editors&ust=1778600245855185&usg=AOvVaw0lcQKe0zvQbw_FDXqvFe6f) to fix "broken" -W options for OpenMP.


  * RFC: [https://discourse.llvm.org/t/openmp-misspelling-of-wopen-mp/90196](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-misspelling-of-wopen-mp/90196&sa=D&source=editors&ust=1778600245855380&usg=AOvVaw0Tb8oLq2g72a_zKs0SCEoX) 
  * Will remain open until the end of April for visibility.


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245855627&usg=AOvVaw2JL0lEhOvCfJeKd9yoo3nH)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Extracted smaller PRs at reviewer request:


  * [https://github.com/llvm/llvm-project/pull/171610](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171610&sa=D&source=editors&ust=1778600245855876&usg=AOvVaw1kIp89uV7P8mNjLzcEwrkj) (merged)
  * [https://github.com/llvm/llvm-project/pull/177953](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/177953&sa=D&source=editors&ust=1778600245856002&usg=AOvVaw2IH6VXA0TuOoP7iDOdZpCp) (merged)
  * [https://github.com/llvm/llvm-project/pull/187868](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187868&sa=D&source=editors&ust=1778600245856126&usg=AOvVaw1dDQRm5vWeXUZOXPhFiHBs) (merged)


  * More progress has been made.  Michael dealing with the fallout due to cmake's expectations.
  * Discourse post about #include "omp_lib.h" not working anymore due to a difference in paths.


  * Modern libomp development


  * New (2026-04-08): [Meta RFC: ADTs without C++ runtime dependency - LLVM Project - LLVM Discussion Forums](https://www.google.com/url?q=https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317&sa=D&source=editors&ust=1778600245856555&usg=AOvVaw2bWJ-XoqeXLtjJmorbYN5i)
  * Runtime needs to parse context-selectors, for that using certain C++/LLVM runtime utilities can help.
  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1778600245857464&usg=AOvVaw3aZgE8DLb6eUE-0-wx3u9U)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1778600245857642&usg=AOvVaw3eHADrubcz-EQ-qgJjGi9N)
  * libomp is C++-ish, but should not link against the C++ stdlib
  * Most C++ stdlib features (e.g. std::vector) cannot be used
  * LLVM features, such as llvm::StringRef or llvm::SmallVector, cannot be used (because they can use C++ runtime features internally)
  * -> introduce Advanced Data Types for libomp (currently kmp_str_ref and kmp_vector) to improve the development situation and make new features, such as [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1778600245858276&usg=AOvVaw2VsGF0b1Chfd6PGAsZJOCU), more streamlined and less annoying to review
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
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245859923&usg=AOvVaw3c9MesQDorNxLCQlvxs50H))


  * Michael is testing this with different OSs.


  * In old-school Fortran, where nothing is declared, the compiler will mangle RT names in ways that are incompatible with this implementation.  This is a blocker, since there is still a lot of code that follows that.

* * *
