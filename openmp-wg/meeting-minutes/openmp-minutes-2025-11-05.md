### November 5, 2025

Agenda

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245909810&usg=AOvVaw11jcQJyWVczQ4-F6xKVuis)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245910220&usg=AOvVaw24KhpDej_N7zC5uQdBw73U)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245910330&usg=AOvVaw3acLdlzzCA3pP4oleRdL7J) 
  * Any specific bugs to look at? 


  * OMPT upstreaming plans from AMD


  * First OMPT PR (testing framework) has landed: [https://github.com/llvm/llvm-project/pull/154786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154786&sa=D&source=editors&ust=1778600245910575&usg=AOvVaw1faNEQ47IWYLRMUK3c1PPg) 
  * Device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs
  * Next step: downstream code work to incorporate changes from upstream and work on reducing potential conflicts; refactoring into an abstraction layer.


  * Still ongoing


  * Update and request for discussion to follow soon.


  * Hopefully at the next meeting (Nov 19)


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245911154&usg=AOvVaw1XioTvhU_VYFqpam57BSp-)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.


  * Fine-grained debug support (Intel/Alex) ([https://github.com/llvm/llvm-project/pull/165416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/165416&sa=D&source=editors&ust=1778600245911449&usg=AOvVaw0PaKTUrvBdBrpWM99CQ6Lx))


  * Filter things that get output
  * Joseph: two prints, debug and informational.  Deprecate LIBOMPTARGET_DEBUG flag in cmake and use NDEBUG instead
  * Alex: still want to have different debug configurations, get debug support even when LLVM is build with NDEBUG.
  * Joseph: have a flag and use "flag || !NDEBUG" to enable debug prints
  * Have a list of keywords to enable debug prints from different parts, keep backward compatibility with "1", use "all" for everything
  * Alex: there are also debug levels
  * Alex where should this live?  There is some data that shouldn't be in a header file
  * Joseph: use it for liboffload first.  Have it in a header and recompute it in different places at first use.
  * Joseph: when adding a new feature it's hard to determine what level to put it under, using tags should be enough
  * Alex: disagrees, if a component wants to support levels, there would need to be additional tags for each level (for the same component).
  * Joseph: do we really need to have a complicated mechanism for this?
  * Alex: users wanted different levels to limit the amount of information
  * Joseph: it should be easy for people to write new code that uses this functionality
  * Alex: in the absence of levels people tend to print too little debug information
  * Michael Klemm: Users say that the debugging experience in LLVM is difficult and complicated.  Have a single way to control debugging of OpenMP-related code (not specific to liboffload and libomptarget). In the future it could be extended to libomp.
  * Alex: this makes sense, but not clear where/how to implement it


  * The code would have to live somewhere, there is no code in common with libomp at the moment


  * 

  * Call for review:


  * Virtual function support:


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245913431&usg=AOvVaw1AkKaafx6bKprrJ42VCLLh)
  * [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245913560&usg=AOvVaw1OeMeK8He3r2L31xiJ2qKn) 


  * CMake improvement: [https://github.com/llvm/llvm-project/pull/159416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159416&sa=D&source=editors&ust=1778600245913690&usg=AOvVaw1zvTPnCPmLYySfrlnrt8o2)
  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245913814&usg=AOvVaw1L-fG4-RrrueqnQaYFO80-), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245913868&usg=AOvVaw3sJU6xamM98mJRLN9no0_y), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245913931&usg=AOvVaw0iHzHr8YQqRRqfdpf2lVxT))


  * Kevin: dyn_groupprivate has changed in the spec, the PRs need to be updated


  * [OpenMP][Clang] Use ATTACH map-type for list-items with base-pointers. ([#153683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/153683&sa=D&source=editors&ust=1778600245914157&usg=AOvVaw2TVvGmnuCRym6DeAqwVR7l), NFC Subset with utils/helpers 1: [#155625](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155625&sa=D&source=editors&ust=1778600245914258&usg=AOvVaw0tVpmDPX3oHsTCxB7apfwv), NFC subset 2: [#161294](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/161294&sa=D&source=editors&ust=1778600245914325&usg=AOvVaw2snwfbA1-3fMgZHXT8WNX_))
  * [[OFFLOAD] Add plugin with support for Intel oneAPI Level Zero by adurang * Pull Request #158900 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245914498&usg=AOvVaw0w1h6smD9Ww3pXh7_2-Oyu)


  * [[OFFLOAD] Add support for indexed per-thread containers](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/164263&sa=D&source=editors&ust=1778600245914613&usg=AOvVaw2XlS7yrGLo8YCL4ii98BXY)


  * [[OpenMP][clang][HIP][CUDA] fix weak alias emit on device compilation](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/164326&sa=D&source=editors&ust=1778600245914766&usg=AOvVaw1lDbDeixwwPNjSHIJ8PZF8)


  * Move libomptarget on top of liboffload


  * Alex: started looking into this
  * Call some functions from liboffload, others from plugins
  * Need to link libomptarget statically into liboffload for some time
  * Assume that there is a single plugin present for now
  * Joseph: turn liboffload into object library
  * Lots of prototyping has been done so far, many workarounds were needed


  * Present the summary at the next meeting


  * Firstprivate behavior on TARGET


  * firstprivate(ptr) will do present lookup on the value of the pointer.  This should happen for a base pointer of a list item on map clause, but not when the pointer is listed on firstprivate. Is this a deliberate choice? Seems like a bug


  * Someone working on the PR


  * Presentation by Gregory Fine


  * Slides: [https://drive.google.com/file/d/1Zdmwjzoyebac9m5E6o__z07oXoZ-KL2s/view?usp=drive_link](https://www.google.com/url?q=https://drive.google.com/file/d/1Zdmwjzoyebac9m5E6o__z07oXoZ-KL2s/view?usp%3Ddrive_link&sa=D&source=editors&ust=1778600245915824&usg=AOvVaw3-mK3DDxxjsiZsiZtZMRvM)
