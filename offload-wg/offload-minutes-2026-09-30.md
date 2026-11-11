# **Wednesday, Sep 30, 9:00 \- 10:00 am CDT**

# **Agenda**

9. Meeting canceled on Oct 14 due to OpenMP F2F
10. PR review list:
    1. [https\://github.com/llvm/llvm-project/pull/226441](https://github.com/llvm/llvm-project/pull/226441)
    2. [https\://github.com/llvm/llvm-project/pull/220761](https://github.com/llvm/llvm-project/pull/220761)
    3. [https\://github.com/llvm/llvm-project/pull/223730](https://github.com/llvm/llvm-project/pull/223730)
11. Interface/layering cleanup
    1. Pull requests coming up.
    2. Starting with small changes
    3. Refactoring plugin interface may be an option in the future
    4. Launch bound handling may require refactoring as well
    5. Part of work on OpenACC: some plugins still contain references to OMPT, Ivan wants to change this to use the listener interface, but it would ideally use C++ classes.
       1. Add Blazej (blazej-smorawski) to the PR.
    6. Plan to add OpenCL plugin:
       1. OpenCL has different platforms which could be connected to multiple devices.
       2. The abstraction to express that is missing.
       3. The platform can have conflicting devices.
       4. Joseph: the main entities were originally devices, platforms were an implementation detail. We should be careful about what we expose so as not to make things too complex.
       5. No progress to report on openCL.
    7. OpenCL support is delayed.  Can remove this item.
12. SYCL offload context discussion
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
13. OpenACC support
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
        2.
14. Piotr and Lukasz will attend the LLVM conference
    1. Will have a workshop about offload and SYCL.

