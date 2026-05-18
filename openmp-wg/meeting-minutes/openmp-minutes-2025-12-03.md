### December 3, 2025

Agenda (copied from last meeting for now, new stuff in red)

 

  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245902493&usg=AOvVaw357cEjpNpCDH6rr9nYyI4h)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Issues:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245902901&usg=AOvVaw0tvojzOJ6khEldtR4TE6zv)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245903004&usg=AOvVaw2pcTelVfrZnGSBIsayUKa_) 
  * Any specific bugs to look at? 


  * Support for Fortran API with adapter routines


  * Some C/C++ interfaces can no longer be exported with '_' added
  * Fortran adapter layer might be needed for future OpenMP API routines
  * Current example: omp_get_device_from_uid() and omp_get_uid_from_device() (see [[OpenMP] Add Fortran support for omp_* functions needing adapters by ro-i * Pull Request #170374 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170374&sa=D&source=editors&ust=1778600245903509&usg=AOvVaw0ipKosJpoubpSVEIssTfr1))


  * Changes for building Flang omp_lib.mod


  * [https://github.com/llvm/llvm-project/pull/169909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169909&sa=D&source=editors&ust=1778600245903691&usg=AOvVaw2iyVkuXLFPifzc1kLLwqfn) 
  * [https://github.com/llvm/llvm-project/pull/169638](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169638&sa=D&source=editors&ust=1778600245903802&usg=AOvVaw2nWyfEQ-kNuwDroDkU6qcX) 


  * Virtual function calls on target


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245903970&usg=AOvVaw1w7CfpujF9QaZTDgLVucm3)
  * Create indirect call table, do binary search. Assumes Itanium ABI at the moment.
  * Supports indirect function calls as well.


  * Fine-grained debug support (Intel/Alex) ([https://github.com/llvm/llvm-project/pull/165416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/165416&sa=D&source=editors&ust=1778600245904274&usg=AOvVaw1cl9ZdhybpCvcLYr8H0IT8))


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


  * Consensus has been reached, now implementing the changes.
  * Need help with adopting plugins to use the new messages (e.g. AMD plugin).
  * 

  * Call for review:


  * Virtual function support:


  * [https://github.com/llvm/llvm-project/pull/159856](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159856&sa=D&source=editors&ust=1778600245906459&usg=AOvVaw3CBPNK0kovvqr4BAhYSh6W)
  * [https://github.com/llvm/llvm-project/pull/159857](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159857&sa=D&source=editors&ust=1778600245906596&usg=AOvVaw3YYGJZwhdFWu1YEUXKi2iJ) 


  * CMake improvement: [https://github.com/llvm/llvm-project/pull/159416](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/159416&sa=D&source=editors&ust=1778600245906730&usg=AOvVaw3WLCgaMyBIWlSkYViWm2Gw)
  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245906854&usg=AOvVaw1fNMwhKfARL5o2evodPkZR), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245906918&usg=AOvVaw2R20vmEZa3w2K8-oP1a-Hx), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245906977&usg=AOvVaw1dnDBpYmW-A5L6-eZSK-nK))


  * Kevin: Updated to latest OpenMP spec


  * [OpenMP][Clang] Use ATTACH map-type for list-items with base-pointers. ([#153683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/153683&sa=D&source=editors&ust=1778600245907172&usg=AOvVaw1_N9mW8J2Ll88VVCEvuHVs), NFC Subset with utils/helpers 1: [#155625](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155625&sa=D&source=editors&ust=1778600245907271&usg=AOvVaw0xnirprys63VvyA_ZqvW_C), NFC subset 2: [#161294](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/161294&sa=D&source=editors&ust=1778600245907339&usg=AOvVaw1QTZeF8dR7gkNVVx8k4Yjn))
  * [[OFFLOAD] Add plugin with support for Intel oneAPI Level Zero by adurang * Pull Request #158900 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245907509&usg=AOvVaw0utXwMNeZZJjkQFZS-Ijb_)
  * [OpenMP] Preserve the original address when use_device_ptr/addr lookup fails. ([#169438](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169438&sa=D&source=editors&ust=1778600245907649&usg=AOvVaw1xZ-tpU_pd2vC6b-tmfel2))


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


  * Slides: [https://drive.google.com/file/d/1Zdmwjzoyebac9m5E6o__z07oXoZ-KL2s/view?usp=drive_link](https://www.google.com/url?q=https://drive.google.com/file/d/1Zdmwjzoyebac9m5E6o__z07oXoZ-KL2s/view?usp%3Ddrive_link&sa=D&source=editors&ust=1778600245908672&usg=AOvVaw2lCwkhf_OqM2S44tEN3bpn)


  * OMPT upstreaming plans from AMD


  * First OMPT PR (testing framework) has landed: [https://github.com/llvm/llvm-project/pull/154786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154786&sa=D&source=editors&ust=1778600245908915&usg=AOvVaw3JIV7AAXZ8vn-E9QVShfxh) 
  * Device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs
  * Next step: downstream code work to incorporate changes from upstream and work on reducing potential conflicts; refactoring into an abstraction layer.


  * Still ongoing


  * Update and request for discussion to follow soon.


  * Hopefully at the next meeting (Nov 19)


  * 


Meeting canceled due to SC25.

* * *
