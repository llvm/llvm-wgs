# Wednesday, February 4, 9:00 - 10:00 am CST

# Agenda

  53. PR Review list


  1.  


  54. Level zero plugin


  1. A system with Intel hardware has been added to the upstream CI


  1. Next: Add tests that exercise this code.
  2. Only 10-15% tests passing, the rest was XFAILED.
  3. Next: work on getting the tests pass


  1. SPIRV device RTL was merged, but is not used yet


  1. Johannes has some fixes (https://github.com/jdoerfert/llvm-project/tree/spirv-offload), seems like lots of errors are caused by a small number of issues


  2. Adding unit tests for L0


  55. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. [...old discussion in prior meeting notes…]
  2. Joseph: Could we look up a global name in SPIRV for the kernel and iterate over the arguments?
  3. Next: see if this is possible. Piotr will discuss this internally
  4. There is an experimental API in L0 to get the argument sizes directly.  The existing launch kernel API can be implemented this way.
  5. The OpenCL is still an issue.


  1. Generic kernel launch API: [https://github.com/llvm/llvm-project/pull/176742](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176742&sa=D&source=editors&ust=1779820786835471&usg=AOvVaw0SpEpDqNrLZwFPdJcQppyB)
  2. Working on generalizing the interface


  56. API for initializing a subset of supported platforms --continued


  1. [...old discussion in prior meeting notes…]
  2. Joseph: thinking about how to make is ABI-stable. Make it append-only for future extensions?
  3. Low priority.


  57. Add context to offloading API


  1. [https://github.com/llvm/llvm-project/issues/171129](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/171129&sa=D&source=editors&ust=1779820786836362&usg=AOvVaw1htVwDflEUbiMlPLgtnlV4) 
  2. Part of SYCL 2020 standard
  3. The plan is to make a prototype first to see what changes are required


  58. PR to remove standalone build for offload


  1. [https://github.com/llvm/llvm-project/pull/17w0693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1779820786836941&usg=AOvVaw36PJX0YQ72CG02kvzy2JMz) 


  59. Dependency on old driver


  1. Some actions are different in the new driver


  1. Bundling is no longer needed, heterogeneous objects are now supported


  2. HIP is moving to the new driver
  3. A lot of cleanup can be done if the old driver is no longer needed


  1. Are there any other frontends that use the old driver? E.g. CUDA, OpenCL, SYCL
  2. SYCL is still working with the old driver, but is moving to the new one


  4. Plan: delete old driver in clang-243
  5. Joseph: working on getting the new driver in HIP, tests are green so far
  6. We'd get the new driver by default with opt-out in clang-23, and only the new driver in clang-24.


  60. GPU offload presentation at FOSDEM by JP Lehr



Recording available here: [FOSDEM 2026 - GPU Offloading in LLVM: Architecture, API, and Plugins](https://www.google.com/url?q=https://fosdem.org/2026/schedule/event/XF8FT9-gpu_offloading_in_llvm_architecture_api_and_plugins/&sa=D&source=editors&ust=1779820786838642&usg=AOvVaw1qeiFvT_1d6UFqhtjercte)

  61. Presentation about OMPT by Michael Halkenhauser in OpenMP in LLVM meeting on Feb 11 25



# Correction: February 25.  (the Feb 11 meeting is canceled due to OpenMP F2F)

* * *
