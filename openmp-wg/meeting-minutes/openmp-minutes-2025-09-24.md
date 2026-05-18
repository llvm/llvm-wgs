### September 24, 2025

Agenda

 

  * October 8 meeting canceled


  * OpenMP face-to-face meetings


  * Where are we right now regarding documents, such as what features are supported and what are not?


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245922200&usg=AOvVaw1uQl962POiVaYunPO6P0c0)        
  * Open a PR and add mjklemm and/or jhuber6 and/or kparzysz as reviewers, open it when the work starts to avoid duplication of effort.


  * If you have commit access, you can make the change yourself.


  * Github will auto-merge PRs that pass CI (and are approved?)


  * Discuss feature deprecation


  * For example, 5.2 deprecated a number of features
  * How do we want to handle deprecations?  Warning, error?


  * ARB: Implementation can continue to support it
  * Michael: emit warnings stating what to use instead (if known) that can be suppressed or converted to an error
  * Catherine: only emit the warning if -fopenmp-version is set to a version in which the feature is deprecated
  * Emit a warning even for features that have been removed


  * Bug(s) that needs looking into:


  * [Clang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aclang%253Aopenmp&sa=D&source=editors&ust=1778600245923154&usg=AOvVaw2c6SIeP8vStHnj2te5hpZq)
  * [Flang OpenMP issues](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Aflang%253Aopenmp&sa=D&source=editors&ust=1778600245923267&usg=AOvVaw1hDycjPkbVwHYNGc-ECRG-) 
  * Any specific bugs to look at? 


  * OMPT upstreaming plans from AMD


  * Device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs
  * First OMPT PR has landed: [https://github.com/llvm/llvm-project/pull/154786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154786&sa=D&source=editors&ust=1778600245923620&usg=AOvVaw3z1gzdVHUUoRgqI4LpYqf5) 
  * Next step: downstream code work to incorporate changes from upstream and work on reducing potential conflicts; refactoring into an abstraction layer.
  * Update and request for discussion to follow soon.


  * Call for review:


  * [OpenMP][Offload] Add support for dyn_groupprivate clause ([#152651](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152651&sa=D&source=editors&ust=1778600245924016&usg=AOvVaw3UqVLo9CXMN5RKz7lBuIPA), [#152830](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152830&sa=D&source=editors&ust=1778600245924083&usg=AOvVaw2pkDmTnPG_Qu_2SHhChogP), [#152831](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152831&sa=D&source=editors&ust=1778600245924146&usg=AOvVaw3Euv6G9qSyhqSp_IJMF_bB))


  * Kevin: dyn_groupprivate has changed in the spec, the PRs need to be updated


  * [OpenMP][Clang] Use ATTACH map-type for list-items with base-pointers. ([#153683](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/153683&sa=D&source=editors&ust=1778600245924378&usg=AOvVaw3q0gflg76gzExmCdruqMV_), NFC Subset with utils/helpers 1: [#155625](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155625&sa=D&source=editors&ust=1778600245924472&usg=AOvVaw0cescGg-g_MoqhmRDxqCLE), NFC subset 2: [#161294](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/161294&sa=D&source=editors&ust=1778600245924540&usg=AOvVaw1nAy156Pc35bi5a092Rdpt))


  * Please test the first PR
  * Julian has run some tests and they all passed
  * Alexey will review the helper PR (1 merged, 1 remaining)


  * [[OFFLOAD] Add plugin with support for Intel oneAPI Level Zero by adurang * Pull Request #158900 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245924875&usg=AOvVaw3YG14CN3DhtDBRpAYKwrb_)


  * Plans to upstream of Level Zero Plugin (Intel/Alex)


  * Finalizing plans for upstreaming of level 0 plugin
  * What's the best way to review it?  It's a large amount of code.
  * A PR should be ready in the next few days


  * PR: [https://github.com/llvm/llvm-project/pull/158900](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1778600245925279&usg=AOvVaw3wNxd2oRKZGEEMyPZFO8MA)
  * There may be more changes needed in the future as more code is integrated with this.


  * Is there an existing public repo with the code?


  * Move libomptarget on top of liboffload


  * Alejandro: started looking into this
  * Call some functions from liboffload, others from plugins
  * Need to link libomptarget statically into liboffload for some time
  * Assume that there is a single plugin present for now
  * Joseph: turn liboffload into object library



* * *

* * *
