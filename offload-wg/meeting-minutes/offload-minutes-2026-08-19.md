# **Wednesday, Aug 19, 9:00 \- 10:00 am CDT**

# **Agenda**

5. PR review list:  
   1. [https://github.com/llvm/llvm-project/pull/213867](https://github.com/llvm/llvm-project/pull/213867) (merged)  
6. Interface/layering cleanup  
   1. Pull requests coming up.  
   2. Starting with small changes  
   3. Refactoring plugin interface may be an option in the future  
   4. Launch bound handling may require refactoring as well  
7. SYCL offload context discussion  
   1. [https://github.com/llvm/llvm-project/pull/201398](https://github.com/llvm/llvm-project/pull/201398) (draft)  
      1. Initial implementation, should be closed eventually  
   2. Joseph: generally ok, some things were already intended to be handled by plugins  
   3. Lukasz: there are additional trackers needed, for example to track shared memory allocations for the AMDGPU plugin  
   4. Joseph: it’s strange that there is still a global state even with the context present  
   5. Lukasz: the PR is still not a final implementation, more cleanup can be done  
   6. Lukasz: the context is needed for SYCL and OpenCL, not specifically for L0  
   7. Cleanup ongoing, resolving merge conflicts  
   8. Added additional APIs with mem alignment  
   9. The API changes are split in several PRs  
      1. Initial one is ‘c’ on the SYCL PR discussion  
   10. New PR: [https://github.com/llvm/llvm-project/pull/213057](https://github.com/llvm/llvm-project/pull/213057) (merged)  
       1. When this one is merged there will be another one that depends on this  
   11. Two more PRs should be created this week, then the context handling can be completed.  
8. OpenACC support  
   1. \[Prior discussion in meeting minutes...\]  
   2. Compiler support (in flang) will be upstreamed in parallel.  
   3. Ivan will start creating non-draft PRs  
   4. PRs:  
      [https://github.com/llvm/llvm-project/pull/208113](https://github.com/llvm/llvm-project/pull/208113)   
      [https://github.com/llvm/llvm-project/pull/208205](https://github.com/llvm/llvm-project/pull/208205) (merged)  
   5. These two PRs are preparing the runtime to split the common parts for OpenMP and OpenACC.  Will use a linker script to export only the relevant names, based on the way that GCC/Clang mangle symbols.  
   6. Will still need to do this with MSVC  
   7. The common library will export both OpenMP and OpenACC functions  
   8. Joseph: this is only necessary if someone uses both at the same time. Otherwise two separate shared libraries would suffice  
   9. Joseph: Having OpenMP and OpenACC share mappings, for example, would be difficult to implement, possibly with unexpected consequences for the user.  
   10. Ivan: Johannes wanted both to cooperate.  
   11. Ivan: can implement the separate libraries first and revisit the cooperative case later.  
   12. Once the two PRs are merged, Ivan will create a PR that splits the common parts into a separate library.  
   13. New PR:  
       1. [https://github.com/llvm/llvm-project/pull/213784](https://github.com/llvm/llvm-project/pull/213784)   
       2. Alex: make sure that the debug prefix doesn’t change  
       3. Ivan: prefix is preserved  
   14. Ivan trying to Nvidia bots running

