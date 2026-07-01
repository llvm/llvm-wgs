### June 17, 2026

**Agenda**

* [llvm-wgs](https://github.com/llvm/llvm-wgs) repo for working groups in the LLVM project  
  * Minutes for prior meetings available at [https://github.com/llvm/llvm-wgs/tree/main/openmp-wg](https://github.com/llvm/llvm-wgs/tree/main/openmp-wg)  
* Where are we right now regarding documents, such as what features are supported and what are not?  
  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst)    
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.  
    * If you have commit access, you can make the change yourself.  
  * Github will auto-merge PRs that pass CI (and are approved?)  
* Issues:  
  * [Clang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aclang%3Aopenmp)  
  * [Flang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aflang%3Aopenmp)   
  * [OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aopenmp)  
  * Any specific bugs to look at?   
* Modern libomp development  
  * [Meta RFC: ADTs without C++ runtime dependency \- LLVM Project \- LLVM Discussion Forums](https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317)  
  * [\[libomp\] Add kmp\_str\_ref (ADT 1/2) by ro-i · Pull Request \#176162 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176162) (merged)  
  * [\[libomp\] Add kmp\_vector (ADT 2/2) by ro-i · Pull Request \#176163 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176163)  
  * \[...\]  
  * For now: proceed with the PRs as an interim solution until the common runtime discussion is finalized  
  * There is a consensus that this is useful.  Robert will create a follow-up RFC  
  * There are two more PRs, and then there will be another PR for making use of the OMP\_DEFAULT\_DEVICE.  
* Call for review:  
  * [\[libomp\] OpenMP 6.0: Add device trait parser by ro-i · Pull Request \#176164 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176164)   
  * [\[libomp\] Parse OMP\_DEFAULT\_DEVICE with new device trait parser by ro-i · Pull Request \#176166 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176166) 


