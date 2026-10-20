### Sep 23, 2026

**Agenda**

* Issues:  
  * [Clang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aclang%3Aopenmp)  
  * [Flang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aflang%3Aopenmp)   
  * [OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aopenmp)  
  * Any specific bugs to look at?   
    * [https\://github.com/llvm/llvm-project/issues/192276](https://github.com/llvm/llvm-project/issues/192276)   
      * Undeferred detached task dependence issue  
* Meeting schedule:  
  * Oct 7 call will be canceled due to IWOMP and EuroMPI taking place  
* Libomptarget to liboffload migration  
  * [https\://github.com/llvm/llvm-project/pull/221730](https://github.com/llvm/llvm-project/pull/221730)   
    * PR stack (15 PRs at the moment)  
  * The exports file in liboffload contains a list of functions that are exported from the library.  The PRs are removing these imports from the list step by step.  
  * Seems like a good idea overall.  
  * Summary of transition roadblocks: [https\://github.com/llvm/llvm-wgs/blob/main/openmp-wg/meeting-minutes/liboffload-transition-summary-2026-09-23.md](https://github.com/llvm/llvm-wgs/blob/main/openmp-wg/meeting-minutes/liboffload-transition-summary-2026-09-23.md)   
    * Joseph: suggest the first approach to avoid complicating things  
  * JP is working on OMPT, that work will need to be coordinated with this effort.  
* Call for review:  
  * [\[offload\]\[omp\] Move reading \_kernel\_environment to libomptarget by adurang · Pull Request \#222606 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/222606)   
* Auto-generating OpenMP definitions: current status  
  * Descriptors for clauses, modifiers, and modifier sets/groups are checked in.  
  * In flang, syntactic modifier and modifier set/group properties are verified using the descriptors.  
  * Next steps: add clause set/group descriptors, then directive descriptors. Extend usage.  
* Support for Fortran API with adapter routines  
  * Some changes to handling module files have landed that would affect the proposal  
  * We may need to use a C-based interface with CFI\_desc\_t exposed.  
    * Michael: need to figure out if all we need to do can be done this way.  
  * Draft PR showing downstream implementation: [https\://github.com/llvm/llvm-project/pull/191504](https://github.com/llvm/llvm-project/pull/191504)  
  * Joseph:  
    * Nothing uses flang except for modules  
    * One Fortran file was replaced with a C version  
  * Side note: there is an ongoing effort to reduce the memory usage when compiling flang.  
  * There was an issue where the compiler would reject call to OpenMP APIs where the integer kind of the argument didn’t exactly match the kind of the parameter.  
    * A PR was created to add different variants and do up/downcasts. It was then reverted due to creating a dependency between flang-rt and libomp.  
    * New PR: [https\://github.com/llvm/llvm-project/pull/221451](https://github.com/llvm/llvm-project/pull/221451) (merged)  
    * Issue: [https\://github.com/llvm/llvm-project/issues/123948](https://github.com/llvm/llvm-project/issues/123948)   
  * Joachim: we should have flags to allow linking mixed C/C++/Fortran code.  
* Debug information (non-dwarf, LIBOMPTARGET\_INFO improvements)   
  * 3 PRs coming in near future. Will handle target-related debug info, among other things  
  * RFC: [\[RFC\] Add opt-in option for full source paths in offload INFO output](https://discourse.llvm.org/t/rfc-add-opt-in-option-for-full-source-paths-in-offload-info-output/91901)  
  * [https\://github.com/llvm/llvm-project/pull/222389](https://github.com/llvm/llvm-project/pull/222389)  
  * [https\://github.com/llvm/llvm-project/pull/223730](https://github.com/llvm/llvm-project/pull/223730)    
* IWOMP in Vienna on Oct 7-9. Registration is still open.  
  * T-shirts available while supplies last  
  * Together with EuroMPI  
  * Followed by OpenMP F2F  
* Task dependency issue and possible fix (Joachim)  
  * Task data structures are never removed from lists  
  * Alex offered to help
