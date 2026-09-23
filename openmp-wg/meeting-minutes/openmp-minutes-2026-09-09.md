### Sep 9, 2026

**Agenda**

* Issues:  
  * [Clang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aclang%3Aopenmp)  
  * [Flang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aflang%3Aopenmp)   
  * [OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aopenmp)  
  * Any specific bugs to look at?   
    * [https://github.com/llvm/llvm-project/issues/192276](https://github.com/llvm/llvm-project/issues/192276)   
      * Undeferred detached task dependence issue  
* Libomptarget to liboffload migration  
  * [https://github.com/llvm/llvm-project/pull/221730](https://github.com/llvm/llvm-project/pull/221730)   
    * PR stack (15 PRs at the moment)  
  * The exports file in liboffload contains a list of functions that are exported from the library.  The PRs are removing these imports from the list step by step.  
  * Seems like a good idea overall.  
* Auto-generating OpenMP definitions: current status  
  * Descriptors for clauses, modifiers, and modifier sets/groups are checked in.  
  * In flang, syntactic modifier and modifier set/group properties are verified using the descriptors.  
  * Next steps: add clause set/group descriptors, then directive descriptors. Extend usage.  
* Call for review:  
  * [\[libomp\] Parse OMP\_DEFAULT\_DEVICE with new device trait parser by ro-i · Pull Request \#176166 · llvm/llvm-project](https://github.com/llvm/llvm-project/pull/176166) (merged)  
  * [\[openmp\] \- Remove hwloc INSTALL\_INTERFACE on omp target](https://github.com/llvm/llvm-project/pull/218923)  
* Support for Fortran API with adapter routines  
  * Some changes to handling module files have landed that would affect the proposal  
  * We may need to use a C-based interface with CFI\_desc\_t exposed.  
    * Michael: need to figure out if all we need to do can be done this way.  
  * PR showing downstream implementation: [https://github.com/llvm/llvm-project/pull/191504](https://github.com/llvm/llvm-project/pull/191504)  
  * Joseph:  
    * Nothing uses flang except for modules  
    * One Fortran file was replaced with a C version  
  * Side note: there is an ongoing effort to reduce the memory usage when compiling flang.  
  * There was an issue where the compiler would reject call to OpenMP APIs where the integer kind of the argument didn’t exactly match the kind of the parameter.  
    * A PR was created to add different variants and do up/downcasts. It was then reverted due to creating a dependency between flang-rt and libomp.  
    * New PR: [https://github.com/llvm/llvm-project/pull/221451](https://github.com/llvm/llvm-project/pull/221451)   
    * Issue: [https://github.com/llvm/llvm-project/issues/123948](https://github.com/llvm/llvm-project/issues/123948)   
* Libomp target debug support (Jason)  
  * Does AMD have any downstream implementation of debug info  
  * 3 PRs coming in near future. Will handle target-related debug info, among other things  
* IWOMP in Vienna in about 3 weeks. Registration is still open.  
  * T-shirts available while supplies last  
  * Together with EuroMPI  
  * Followed by OpenMP F2F

