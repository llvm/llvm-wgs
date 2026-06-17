### June 3, 2026

Agenda

  * [llvm-wgs](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs&sa=D&source=editors&ust=1781699927769326&usg=AOvVaw0WkcFg43aIYPDZIjTMfhKR) repo for working groups in the LLVM project


  * Converted prior meetings to markdown: [https://github.com/llvm/llvm-wgs/pull/4](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs/pull/4&sa=D&source=editors&ust=1781699927769536&usg=AOvVaw3oh_Sdjk3uvERQR8VEQmfI)
  * Waiting for commit rights


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1781699927769932&usg=AOvVaw2td6fdFc6wpHP2zQMXzN58)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1781699927770448&usg=AOvVaw2z_VdkjPs10Ha07lyIpczP)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1781699927770588&usg=AOvVaw1Jhpyf-9HE7_49leB5Sjcs) 
  * [OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aopenmp&sa=D&source=editors&ust=1781699927770738&usg=AOvVaw3-Wy0rJoCZahYhP1NI-LSQ)
  * Any specific bugs to look at? 


  * Changes for building Flang omp_lib.mod


  * Completed


  * Modern libomp development


  * [Meta RFC: ADTs without C++ runtime dependency - LLVM Project - LLVM Discussion Forums](https://www.google.com/url?q=https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317&sa=D&source=editors&ust=1781699927771165&usg=AOvVaw2BnGufAE8LoAi62vZ8hB96)
  * [[libomp] Add kmp_str_ref (ADT 1/2) by ro-i * Pull Request #176162 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176162&sa=D&source=editors&ust=1781699927771469&usg=AOvVaw3xCJb-TLAWzxoCyWOnN1u2)
  * [[libomp] Add kmp_vector (ADT 2/2) by ro-i * Pull Request #176163 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176163&sa=D&source=editors&ust=1781699927771801&usg=AOvVaw3oh8pZAhuiCHi5dNPuUjZX)
  * [...]
  * For now: proceed with the PRs as an interim solution until the common runtime discussion is finalized
  * There is a consensus that this is useful.  Robert will create a follow-up RFC
  * There are two more PRs, and then there will be another PR for making use of the OMP_DEFAULT_DEVICE.


  * Ignore teams ICV setters in restricted contexts


  * [[OpenMP] Ignore teams ICV setters in restricted contexts by Saieiei * Pull Request #194428 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/194428&sa=D&source=editors&ust=1781699927772923&usg=AOvVaw2OSyoEc1N945aHuZgs7gfC)  \- merged


  * Call for review:


  * [[libomp] OpenMP 6.0: Add device trait parser by ro-i * Pull Request #176164 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176164&sa=D&source=editors&ust=1781699927773317&usg=AOvVaw2U-KSF-gzzU7Bvu2a-mi3j) 
  * [[libomp] Parse OMP_DEFAULT_DEVICE with new device trait parser by ro-i * Pull Request #176166 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176166&sa=D&source=editors&ust=1781699927773596&usg=AOvVaw2fRNJM2ErqpWS2zXF-6USm) 
  * [CI] Enable OpenMP and Offload runtime in premerge: [https://github.com/llvm/llvm-project/pull/174955](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174955&sa=D&source=editors&ust=1781699927773846&usg=AOvVaw1ueVu4N-oJwx0NT82PKnGF) 


  * Support for Fortran API with adapter routines


  * Deferred to early 2026
  * Michael Klemm to follow up with Intel OpenMP runtime devs.
  * Some C/C++ interfaces can no longer be exported with '_' added


  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1781699927774619&usg=AOvVaw0w0RHaBpBlWJ-u6mRch92t))


  * Michael is testing this with different OSs.


  * In old-school Fortran, where nothing is declared, the compiler will mangle RT names in ways that are incompatible with this implementation.  This is a blocker, since there is still a lot of code that follows that.



* * *
