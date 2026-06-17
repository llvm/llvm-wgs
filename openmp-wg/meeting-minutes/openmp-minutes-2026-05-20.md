### May 20, 2026

Agenda

  * [llvm-wgs](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs&sa=D&source=editors&ust=1781699927775288&usg=AOvVaw3ePogj4zSxAyfjGwcFkMut) repo for working groups in the LLVM project


  * Converted prior meetings to markdown: [https://github.com/llvm/llvm-wgs/pull/4](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs/pull/4&sa=D&source=editors&ust=1781699927775566&usg=AOvVaw2jg8eJZ2b1adgrU6oqJIX7)
  * Waiting for commit rights


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1781699927776029&usg=AOvVaw0f8cgBIcU3aD_WTGXiB7aZ)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1781699927776531&usg=AOvVaw1_W3jpFUbpP_tBs8hvnL6M)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1781699927776664&usg=AOvVaw02yYSnkWycm5DtKefWOc-q) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1781699927776816&usg=AOvVaw14nskK7a8RZae2p7K1pInP)
  * Any specific bugs to look at? 


  * Move (Flang) OpenMP extensions from OpenMPSupport.md to OpenMP-extensions.md.


  * PR: [https://github.com/llvm/llvm-project/pull/186981](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/186981&sa=D&source=editors&ust=1781699927777208&usg=AOvVaw16vYIBUcaizfGGI8h5vED1) \- merged


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/171515](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/171515&sa=D&source=editors&ust=1781699927777503&usg=AOvVaw34GpLM81qPWZrZ8K8YzhTy)


  * ADDED: offload ToolChain fall back to host's builtin modules


  * More progress has been made.  Michael dealing with the fallout due to cmake's expectations.
  * Discourse post about #include "omp_lib.h" not working anymore due to a difference in paths.
  * Extracting smaller pull requests


  * Flang print the intrinsic module path
  * Change the module search path, counting omp_lib module as intrinsic (not affecting header search path).  Both old and new path are searched now.
  * bbc compiler


  * PR converting iso_fortran_env_impl.F90 file to C++


  * Building of the module and library can be split off
  * Follow-up PR will remove flang from runtimes dependency list


  * Modern libomp development


  * New (2026-04-08): [Meta RFC: ADTs without C++ runtime dependency - LLVM Project - LLVM Discussion Forums](https://www.google.com/url?q=https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317&sa=D&source=editors&ust=1781699927778956&usg=AOvVaw2HqQeIW3yH0xxxcaJUNY2I)
  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1781699927779165&usg=AOvVaw1Pf8QrcP0rNe_bUM32D6LZ)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1781699927779412&usg=AOvVaw2eYIlqmtx1-8Lvk7hx2QW8)
  * [...]
  * For now: proceed with the PRs as an interim solution until the common runtime discussion is finalized
  * There is a consensus that this is useful.  Robert will create a follow-up RFC
  * There are two more PRs, and then there will be another PR for making use of the OMP_DEFAULT_DEVICE.


  * Call for review:


  * [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1781699927780089&usg=AOvVaw0jRBuB_e8iGvbvIP7Nu3rS) 
  * [[libomp] Parse OMP_DEFAULT_DEVICE with new device trait parser by ro-i * Pull Request #176166 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176166&sa=D&source=editors&ust=1781699927780381&usg=AOvVaw0bnvBlqCElmeqOkAqzpLFX) 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1781699927781221&usg=AOvVaw1j4y_Ttypu9yTTBUlI2LxE))


  * Michael is testing this with different OSs.


  * In old-school Fortran, where nothing is declared, the compiler will mangle RT names in ways that are incompatible with this implementation.  This is a blocker, since there is still a lot of code that follows that.


  * AsyncInfo usage in libomptarget

* * *
