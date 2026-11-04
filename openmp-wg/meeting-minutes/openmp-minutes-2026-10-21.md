### Oct 21, 2026

**Agenda**

* Issues:  
  * [Clang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aclang%3Aopenmp)  
  * [Flang OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aflang%3Aopenmp)   
  * [OpenMP issues](https://github.com/llvm/llvm-project/issues?q=is%3Aissue%20state%3Aopen%20label%3Aopenmp)  
  * Any specific bugs to look at?   
    * [https\://github.com/llvm/llvm-project/issues/192276](https://github.com/llvm/llvm-project/issues/192276)   
      * Undeferred detached task dependence issue  
* OpenMP 6.1 coming up  
  * Release date November 12  
  * Face-to-face meetings last week, finishing a lot of the QC process  
  *   
* Libomptarget to liboffload migration TODO  
  * Reimplement interop ([https\://github.com/llvm/llvm-project/pull/234165](https://github.com/llvm/llvm-project/pull/234165))  
  * Decouple RecordReplay ([https\://github.com/llvm/llvm-project/pull/236814](https://github.com/llvm/llvm-project/pull/236814))  
    * Add Virtual Address APIs? (TBD)  
  * Migrate alloc/free (stack)  
    * Use temporary helpers to decouple libomptarget ([https\://github.com/llvm/llvm-project/pull/238763](https://github.com/llvm/llvm-project/pull/238763))  
    * Split detection & reporting for diagnostics ([https\://github.com/llvm/llvm-project/pull/238764](https://github.com/llvm/llvm-project/pull/238764))  
    * Move reporting specific parts to libomptarget (TBD)  
    * Replace helpers (TBD)  
  * Cleanup DeviceImage usages (TBD)  
  * Add tear-down support to libofflooad (TBD)  
  * Final cleanup (TBD)  
  * JP is working on OMPT, that work will need to be coordinated with this effort.  
* Call for review:  
  *   
* Auto-generating OpenMP definitions: current status  
  * Descriptors for clauses, modifiers, and modifier sets/groups are checked in.  
  * In flang, syntactic modifier and modifier set/group properties are verified using the descriptors.  
  * Next steps: add clause set/group descriptors, then directive descriptors. Extend usage.  
  * Descriptors for directives are checked in.  
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
  * RFC: [\[RFC\] Add opt-in option for full source paths in offload INFO output](https://discourse.llvm.org/t/rfc-add-opt-in-option-for-full-source-paths-in-offload-info-output/91901) (Closed)  
  * RFC:  [RFC: extend LIBOMPTARGET\_INFO functionality to allow verbosity control](https://discourse.llvm.org/t/rfc-extend-libomptarget-info-functionality-to-allow-verbosity-control/92522)   
    * Joseph: we should consolidate the different ways of showing debug information  
  * [https\://github.com/llvm/llvm-project/pull/222389](https://github.com/llvm/llvm-project/pull/222389) (merged)  
  * [https\://github.com/llvm/llvm-project/pull/223730](https://github.com/llvm/llvm-project/pull/223730) (merged)  
  * What is the status of upstreaming of the kernel tracing in amdflang?  
    * Michael: we should have an uniform way of doing this (Intel, Cray have their ways of profiling)  
    * Jason: happy to start working on this, but if amdflang already has it it could be reused  
    * Michael: will follow up internally  
* Task dependency issue and possible fix (Joachim)  
  * Task data structures are never removed from lists  
  * Alex offered to help

