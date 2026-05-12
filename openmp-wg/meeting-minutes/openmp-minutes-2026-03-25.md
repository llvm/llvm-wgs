### March 25, 2026

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245866221&usg=AOvVaw2chMb0H4QKkYmak0az-ZiP)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245866646&usg=AOvVaw1dxA3AlAC7-esZjCEVa1Da)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245866759&usg=AOvVaw1c8fRqzCjEY7IkTyLWYeID) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1778600245866850&usg=AOvVaw1IwvBiNOwBWfFH-GXSYoE_)
  * Any specific bugs to look at? 


  * Move (Flang) OpenMP extensions from OpenMPSupport.md to OpenMP-extensions.md.


  * PR: [https://github.com/llvm/llvm-project/pull/186981](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/186981&sa=D&source=editors&ust=1778600245867148&usg=AOvVaw1Bh2y9bLp2hX0IK4iIPLFn)


  * PR [https://github.com/llvm/llvm-project/pull/188434](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/188434&sa=D&source=editors&ust=1778600245867275&usg=AOvVaw0bCrct6sv69T93rl6gyTnv) to fix "broken" -W options for OpenMP.


  * RFC: [https://discourse.llvm.org/t/openmp-misspelling-of-wopen-mp/90196](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-misspelling-of-wopen-mp/90196&sa=D&source=editors&ust=1778600245867482&usg=AOvVaw3pCX13kC4G_s7JR0m0F4By) 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245868066&usg=AOvVaw3G2kKisINwbBJWDk0QGN32))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1778600245868276&usg=AOvVaw1qgbMY_0pgJ1KPj1SCGYM4)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * Extracted smaller PRs at reviewer request:


  * [https://github.com/llvm/llvm-project/pull/171610](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171610&sa=D&source=editors&ust=1778600245868526&usg=AOvVaw0GjSCf5WH2fV97jIs3RzsF) (approved under condition that @petrhosek also approves)
  * [https://github.com/llvm/llvm-project/pull/177953](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/177953&sa=D&source=editors&ust=1778600245868712&usg=AOvVaw0WXsH5z-tgZLEXerGZ-vH4) (approved)
  * [https://github.com/llvm/llvm-project/pull/187868](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187868&sa=D&source=editors&ust=1778600245868834&usg=AOvVaw3bN7aWajjW_ehDmU2QzJko) (approved)


  * Modern libomp development


  * Runtime needs to parse context-selectors, for that using certain C++/LLVM runtime utilities can help.
  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1778600245869174&usg=AOvVaw09tbyuY3wWrPJlF9sPbhNB)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1778600245869326&usg=AOvVaw3U8T8lwaJApRo_xSmkdIUP)
  * libomp is C++-ish, but should not link against the C++ stdlib
  * Most C++ stdlib features (e.g. std::vector) cannot be used
  * LLVM features, such as llvm::StringRef or llvm::SmallVector, cannot be used (because they can use C++ runtime features internally)
  * -> introduce Advanced Data Types for libomp (currently kmp_str_ref and kmp_vector) to improve the development situation and make new features, such as [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1778600245869894&usg=AOvVaw2n5LT2iCbwAh1NTXt8oLEb), more streamlined and less annoying to review
  * Joachim: Sanitizers have a similar restriction, they supply their own implementations of certain data structures.
  * Michael: Same for flang-rt.
  * Abhinav: liboffload uses llvm::SmallVector, why libomp can't?
  * Joachim: liboffload is only usable with clang, libomp can be used with a variety of compilers.
  * Michael: Using liboffload with flang is also sub-optimal.
  * Alex: Why does it matter that C++RT would be required? We could statically link the C++RT if ABI compatibility is the issue
  * Joachim: maybe we could still use C++RT but with all names inside of some namespace to avoid mismatches with names from different C++RT implementations.
  * Michael: libc contains copies of libc++ standard headers to be independent from the actual C++ implementation.


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



Call for review:

* * *
