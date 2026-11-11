# **Wednesday, Oct 28, 9:00 \- 10:00 am CDT**

# **Agenda**

1. Momentary difficulties getting the meeting started…
   1. Use this link (this time only): [https\://teams.microsoft.com/meet/224101510874062?p=zIgGEsCC0x6hrFhGZa](https://teams.microsoft.com/meet/224101510874062?p=zIgGEsCC0x6hrFhGZa)
   2. Michael will create a new Teams invite
      1. Will be published in the agenda
2. Meeting ownership/agenda location
   1. There will be a new location for the agenda document.
      1. [https\://docs.google.com/document/d/19DKO1xAm7RHDTnZ2PsPr5Qj2lefVZvLzuTe1Z0UBoK0](https://docs.google.com/document/d/19DKO1xAm7RHDTnZ2PsPr5Qj2lefVZvLzuTe1Z0UBoK0)
      2.
   2. Read-only for everyone, write access by request.
3. PR review list:
   1. [https\://github.com/llvm/llvm-project/pull/222650](https://github.com/llvm/llvm-project/pull/222650)
   2. [https\://github.com/llvm/llvm-project/pull/234758](https://github.com/llvm/llvm-project/pull/234758)
   3. [https\://github.com/llvm/llvm-project/pull/231174](https://github.com/llvm/llvm-project/pull/231174)
4. Interface/layering cleanup
   1. Pull requests coming up.
   2. Starting with small changes
   3. Refactoring plugin interface may be an option in the future
   4. Launch bound handling may require refactoring as well
   5. Part of work on OpenACC: some plugins still contain references to OMPT, Ivan wants to change this to use the listener interface, but it would ideally use C++ classes.
      1. Add Blazej (blazej-smorawski) to the PR.
   6. Plan to add OpenCL plugin delayed
5. SYCL offload context discussion
   1. \[Prior discussion in meeting minutes...\]
   2. Lukasz: the context is needed for SYCL and OpenCL, not specifically for L0
   3. Cleanup ongoing, resolving merge conflicts
   4. Added additional APIs with mem alignment
   5. The API changes are split in several PRs
      1. Initial one is ‘c’ on the SYCL PR discussion
   6. New PR: [https\://github.com/llvm/llvm-project/pull/213057](https://github.com/llvm/llvm-project/pull/213057) (merged)
      1. When this one is merged there will be another one that depends on this
   7. Two more PRs should be created this week, then the context handling can be completed.
   8. The only functionality that needs to be changed is allocations.  PR coming.
      1. [https\://github.com/llvm/llvm-project/pull/222677](https://github.com/llvm/llvm-project/pull/222677) (merged)
      2. Will remove device parameter from host allocations in a follow-up.
6. OpenACC support
   1. \[Prior discussion in meeting minutes...\]
   2. The common library will export both OpenMP and OpenACC functions
   3. Joseph: this is only necessary if someone uses both at the same time. Otherwise two separate shared libraries would suffice
   4. Joseph: Having OpenMP and OpenACC share mappings, for example, would be difficult to implement, possibly with unexpected consequences for the user.
   5. Ivan: Johannes wanted both to cooperate.
   6. Ivan: can implement the separate libraries first and revisit the cooperative case later.
   7. Once the two PRs are merged, Ivan will create a PR that splits the common parts into a separate library.
   8. New PR:
      1. [https\://github.com/llvm/llvm-project/pull/213784](https://github.com/llvm/llvm-project/pull/213784) (merged)
      2. Alex: make sure that the debug prefix doesn’t change
      3. Ivan: prefix is preserved
   9. Ivan trying to Nvidia bots running
   10. Buildbots are almost prepared, PR ready that includes them.
   11. Buildbot up and running: https\://lab.llvm.org/buildbot/\#/builders/239
   12. Refactoring in progress, one PR is coming.
   13. Do we want the OpenACC libraries built on all buildbots?
       1. JP from AMD and Nick from Intel maintain respective buildbots
   14. https\://github.com/llvm/llvm-project/pull/231174

7. Piotr and Lukasz will attend the LLVM conference
   1. Will have a workshop about offload and SYCL.
8. Libomptarget and Plugin Interface decoupling (liboffload migration)
* Link against liboffload and plugins through liboffload (done)
* Decouple Error classes (done)
* Use liboffload to get device properties (mostly done)
* Use liboffload queues and events (done)
* Memory locking and other memory operations (done)
* RPC setup through liboffload (done)
* Load binaries and resolve symbols through liboffload (done)
* Use liboffload for memory movement operations (done)
* Use liboffload to launch kernels ([https\://github.com/llvm/llvm-project/pull/233735](https://github.com/llvm/llvm-project/pull/233735))
* Use liboffload for allocations
  * [\[Offload\] Manage all allocations through PluginCtx](https://github.com/llvm/llvm-project/pull/234758)
  * Decouple diagnostics (OMPX\_TrackNumKernelLaunches & OMPX\_TrackAllocationTraces )
  * Migrate alloc/free to liboffload
* Use liboffload for interop
  * Get native handles (done)
  * Add backend specific behaviors ([\[Offload\]\[Omp\] Add Backend specific OpenMP-only options](https://github.com/llvm/llvm-project/pull/235844))
  * Interop rewrite: [https\://github.com/llvm/llvm-project/pull/234165](https://github.com/llvm/llvm-project/pull/234165) (in progress)
* Record replay
  * Not to be moved out of the plugins
  * Define temporary liboffload helpers so the PluginTypes don't leak into libomptarget (tbd)
* Other small usages, mostly to get information
  * HostUid, remove data\_fence, remove usages of GenericDeviceTy (done)
  * [\[Offload\]\[Omp\] Migrate readGlobalFromImage through liboffload](https://github.com/llvm/llvm-project/pull/235935)
  * [\[Offload\]\[Omp\] Compute getBlockLimit through liboffload](https://github.com/llvm/llvm-project/pull/236400)
  * [\[Offload\]\[Omp\] Remove references to InfoTreeNode and DeviceInfo](https://github.com/llvm/llvm-project/pull/236407)
  * Device use\_auto\_zero\_copy property (tbd)
  * Get Kernel properties (tbd, depends on launch kernel PR)
  * …
* Better tear-down sync with liboffload (tbd)
