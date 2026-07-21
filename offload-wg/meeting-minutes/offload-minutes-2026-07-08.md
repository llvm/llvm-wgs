# **Wednesday, July 8, 9:00 \- 10:00 am CDT**

# **Agenda**

1. Prior minutes are now in [https://github.com/llvm/llvm-wgs/tree/main/offload-wg/meeting-minutes](https://github.com/llvm/llvm-wgs/tree/main/offload-wg/meeting-minutes)  
2. PR Review list  
   1. [https://github.com/llvm/llvm-project/pull/206752](https://github.com/llvm/llvm-project/pull/206752)   
      1. [Will be merged tomorrow if there are no more comments](https://github.com/llvm/llvm-project/pull/206752)  
3. SYCL offload context discussion  
   1. [https://github.com/llvm/llvm-project/pull/201398](https://github.com/llvm/llvm-project/pull/201398)     
   2. Joseph: generally ok, some things were already intended to be handled by plugins  
   3. Lukasz: there are additional trackers needed, for example to track shared memory allocations for the AMDGPU plugin  
   4. Joseph: it’s strange that there is still a global state even with the context present  
   5. Lukasz: the PR is still not a final implementation, more cleanup can be done  
   6. Lukasz: the context is needed for SYCL and OpenCL, not specifically for L0  
   7. Cleanup ongoing, resolving merge conflicts  
   8. Added additional APIs with mem alignment  
4. Follow up proposal to OL\_KERNEL\_LAUNCH\_PROP\_TYPE\_SIZE:   [https://github.com/llvm/llvm-project/pull/194333](https://github.com/llvm/llvm-project/pull/194333) (merged)  
   1. Piotr working on a follow-up  
   2. [https://github.com/llvm/llvm-project/pull/205224 (merged)](https://github.com/llvm/llvm-project/pull/205224)  
   3. Accepted, can be merged now  
5. Host plugin seems to run each function once, unlike GPU plugins that execute the kernels multiple times.  
   1. Joseph: the host plugin historically has been intended to test the OpenMP implementation, without attempts to optimize it; it can be improved  
   2. Piotr: SYCL has a “native” CPU support.  Unifying the plugin structure would be helpful   
      1. Intel has a SYCL support as a part of the one API.  
      2. Plan to upstream the native CPU adapter/plugin.  
   3. Joseph: it would be good to get the offload test suite to pass with the host plugin  
   4. Remove this list item from the agenda for the next meeting.  
6. OpenACC support  
   1. NVIDIA is in the process of upstreaming OpenACC support in flang.  Will also upstream runtime implementation.  
   2. Has prototype that uses liboffload/libomptarget  
   3. RFC will published soon (within a couple of weeks)  
   4. Joseph: sounds reasonable  
      1. Noted that libomptarget should depend on liboffload, not the other way around.  
      2. Public buildbot would be good to have  
   5. Still working on it.  Making sure that the code that was going to be published with the RFC is in a good shape.  
   6. RFC: [https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793](https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793)  
   7. PR: https://github.com/llvm/llvm-project/pull/197894  
   8. The dependence issue may be addressed later.  Common code may be extracted into a support library.  
   9. There will need to be a buildbot to test the OpenACC code.  
      1. Joseph: we should have unit tests that will have better coverage (than OpenMP tests) including corner cases.  
   10. Compiler support (in flang) will be upstreamed in parallel.  
   11. Ivan will start creating non-draft PRs  
   12. PRs:  
       [https://github.com/llvm/llvm-project/pull/208113](https://github.com/llvm/llvm-project/pull/208113)  
       [https://github.com/llvm/llvm-project/pull/208205](https://github.com/llvm/llvm-project/pull/208205)  
   13. [These two PRs are preparing the runtime to split the common parts for OpenMP and OpenACC.  Will use a linker script to export only the relevant names, based on the way that GCC/Clang mangle symbols.](https://github.com/llvm/llvm-project/pull/208205)  
   14. [Will still need to do this with MSVC](https://github.com/llvm/llvm-project/pull/208205)  
   15. [The common library will export both OpenMP and OpenACC functions](https://github.com/llvm/llvm-project/pull/208205)  
   16. [Joseph: this is only necessary if someone uses both at the same time. Otherwise two separate shared libraries would suffice](https://github.com/llvm/llvm-project/pull/208205)  
   17. [Joseph: Having OpenMP and OpenACC share mappings, for example, would be difficult to implement, possibly with unexpected consequences for the user.](https://github.com/llvm/llvm-project/pull/208205)  
   18. [Ivan: Johannes wanted both to cooperate.](https://github.com/llvm/llvm-project/pull/208205)  
   19. [Ivan: can implement the separate libraries first and revisit the cooperative case later.](https://github.com/llvm/llvm-project/pull/208205)  
   20. [Once the two PRs are merged, Ivan will create a PR that splits the common parts into a separate library.](https://github.com/llvm/llvm-project/pull/208205)  
7. RFC [“Proposed extension to the \--offload-arch option”](https://discourse.llvm.org/t/rfc-proposed-extension-to-the-offload-arch-option/90790).  What are the remaining open issues, and how can we drive this to a conclusion?  
   1. RFC: [https://discourse.llvm.org/t/rfc-proposed-extension-to-the-offload-arch-option/90790](https://discourse.llvm.org/t/rfc-proposed-extension-to-the-offload-arch-option/90790/23)  
   2. Joseph: concerned about increase in complexity in the driver, these flags should instead be toolchain-specific; not opposed to the options existing  
   3. Greg: specifying virtual ISAs is common enough to warrant a driver (top-level) option, rest can be toolchain-specific.  
   4. Joseph: ok with that. More discussion (about specific option naming/syntax) to follow  
   5. The discussion will continue in PRs.  
8. Lukasz still waiting for the offload-reviewers team.  
9. Lukasz: No testing of offload in pre-commit PRs.  
   1. Joseph: we should have building of offload ibraries as a pat of the pre-commit CI  
   2. Joseph: Running tests is disabled because some of them are expensive, plus there are lots of flaky tests.  
   3. Lukasz: it would be nice to be able to test offload via common CI  
10. Lukasz: are we active on discord?  
    1. Channels: runtime or openmp.


