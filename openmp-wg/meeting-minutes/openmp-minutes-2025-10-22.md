### October 22, 2025

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245916244&usg=AOvVaw3aE44kSRGCF0NL7iCgz55v)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Discuss feature deprecation


  * Conclusion: support deprecated/removed features, emit a warning when -fopenmp-version is set to a version in which the feature is no longer present (or is deprecated)


  * Bug(s) that needs looking into:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245916866&usg=AOvVaw3r7TTtLt5Jr1rgv6zG133-)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245916976&usg=AOvVaw0foAizz_zS7U1gsVatlFQ7) 
  * Any specific bugs to look at? 


  * OMPT upstreaming plans from AMD


  * First OMPT PR (testing framework) has landed: [https://github.com/llvm/llvm-project/pull/154786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154786&sa=D&source=editors&ust=1778600245917243&usg=AOvVaw3QMK870ZkXC-dAHV1_0Z-A) 
  * Device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs
  * Next step: downstream code work to incorporate changes from upstream and work on reducing potential conflicts; refactoring into an abstraction layer.


  * Still ongoing


  * Update and request for discussion to follow soon.


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245917759&usg=AOvVaw0q9gF0jO-IbTg0yfT90KAz)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.


  * Fine-grained debug support (Intel/Alex)


  * Filter things that get output
  * Joseph: two prints, debug and informational.  Deprecate LIBOMPTARGET_DEBUG flag in cmake and use NDEBUG instead
  * Alex: still want to have different debug configurations, get debug support even when LLVM is build with NDEBUG.
  * Joseph: have a flag and use "flag || !NDEBUG" to enable debug prints
  * Have a list of keywords to enable debug prints from different parts, keep backward compatibility with "1", use "all" for everything
  * Alex: there are also debug levels
  * Alex where should this live?  There is some data that shouldn't be in a header file
  * Joseph: use it for liboffload first.  Have it in a header and recompute it in different places at first use.


  * Call for review:


  * Virtual function support: [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245918908&usg=AOvVaw1HW4ZM7v1doTUFxPvYSFm-)
  * CMake improvement: [https://github.com/llvm/llvm-project/pull/159416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159416&sa=D&source=editors&ust=1778600245919044&usg=AOvVaw3jw2a2XKWu7DiMCAroa1SL)
  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245919180&usg=AOvVaw1Ub0FHENUeUaHogkcqNkmg), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245919240&usg=AOvVaw1lV1MEYaVbvL7cOgYhR42R), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245919297&usg=AOvVaw2lYRba32J9nGkzPWYz8Hma))


  * Kevin: dyn_groupprivate has changed in the spec, the PRs need to be updated


  * [OpenMP][Clang] Use ATTACH map-type for list-items with base-pointers. ([#153683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/153683&sa=D&source=editors&ust=1778600245919519&usg=AOvVaw3-Mpcw5OjZ366VLvnb3kot), NFC Subset with utils/helpers 1: [#155625](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155625&sa=D&source=editors&ust=1778600245919610&usg=AOvVaw2lmk5TtBMX3ZXj4c4novE9), NFC subset 2: [#161294](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/161294&sa=D&source=editors&ust=1778600245919676&usg=AOvVaw0heMpekbTJH2fiGm3t6q3s))


  * Please test the first PR
  * Julian has run some tests and they all passed
  * Alexey will review the helper PR (1 merged, 1 remaining)


  * [[OFFLOAD] Add plugin with support for Intel oneAPI Level Zero by adurang * Pull Request #158900 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245920025&usg=AOvVaw1WnFuGOlY6RVj7w7M9vEum)


  * [[OFFLOAD] Add support for indexed per-thread containers](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/164263&sa=D&source=editors&ust=1778600245920149&usg=AOvVaw2VgfUk9bcBNn_MkrmucO5V)


  * Plans to upstream of Level Zero Plugin (Intel/Alex) 


  * Finalizing plans for upstreaming of level 0 plugin
  * What's the best way to review it?  It's a large amount of code.
  * A PR should be ready in the next few days


  * PR: [https://github.com/llvm/llvm-project/pull/158900](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245920533&usg=AOvVaw3yXlVgOxuZgIzO5MTHCi26)
  * There may be more changes needed in the future as more code is integrated with this.


  * Is there an existing public repo with the code?


  * Move libomptarget on top of liboffload


  * Alex: started looking into this
  * Call some functions from liboffload, others from plugins
  * Need to link libomptarget statically into liboffload for some time
  * Assume that there is a single plugin present for now
  * Joseph: turn liboffload into object library
  * Lots of prototyping has been done so far, many workarounds were needed


  * Present the summary at the next meeting


  * Firstprivate behavior on TARGET


  * firstprivate(ptr) will do present lookup on the value of the pointer.  This should happen for a base pointer of a list item on map clause, but not when the pointer is listed on firstprivate.


  * Is this a deliberate choice?  Seems like a bug



* * *
