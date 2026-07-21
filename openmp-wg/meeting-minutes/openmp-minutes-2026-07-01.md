### July 1, 2026

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
* OpenMP 6.1 comment draft (aka Technical Report 15\) expected to be released on July 9  
  * Will be available for download at [openmp.org](http://openmp.org)  
    * Please add your comments either in this meeting, via email at [info@openmp.org](mailto:info@openmp.org), or Michael.Klemm@openmp.org  
    * Changes include multidimensional grids  
  * OpenMP 6.1 planned release date is November 12, 2026  
* Modern libomp development  
  * The basic support has been merged. The effort will continue under the generalized project: [https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317](https://discourse.llvm.org/t/meta-rfc-adts-without-c-runtime-dependency/90317)  
* Call for review:  
  * [\[libomp\] OpenMP 6.0: Add device trait parser by ro-i · Pull Request \#176164 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176164)   
  * [\[libomp\] Parse OMP\_DEFAULT\_DEVICE with new device trait parser by ro-i · Pull Request \#176166 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176166)   
* Support for Fortran API with adapter routines  
  * Some changes to handling module files  have landed that would affect the proposal  
  * We may need to use a C-based interface with CFI\_desc\_t exposed.  
  * PR showing downstream implementation: [https://github.com/llvm/llvm-project/pull/191504](https://github.com/llvm/llvm-project/pull/191504)  

