# Wednesday, December 10 2025, 9:00 - 10:00 am CST

# Agenda

  76. Next meeting: December 17, 2025
  77. PR Review list


  1. 

  78. Level zero plugin


  1. Review in progress: https://github.com/llvm/llvm-project/pull/158900
  2. Build bot needed


  1. Intel has setup a build bot already.
  2. Build bot will become active once the PR lands.


  3. Kevin's suggestions on the PR have been implemented.
  4. New plugin will be have to be activated for now; experimental status for now.
  5. Joseph will re-review the PR


  1. Concerns on the dependency on libomp; has been removed already.


  79. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. Many ELF aspects are specific to OpenMP support
  2. Should move to libomptarget; might not work with CUDA/HIP anyways.
  3. Level Zero consumes SPIR-V and does not need ELF.
  4. Needs expansion of binary magic number detection.
  5. NEW: Formalizing program image format for olCreateProgram. Should it just accept Offload Binary (after its extended to support SYCL https://discourse.llvm.org/t/rfc-syclbin-a-format-for-sycl-device-code/88603/1 ) ?


  1. Working on extending olCreateProgram to accept other formats (e.g. SPIRV).


  1. [https://github.com/llvm/llvm-project/pull/166545](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/166545&sa=D&source=editors&ust=1779820786862377&usg=AOvVaw08Ch3w9cdiMm02TaSLNyB2) 


  2. It should really accept any offload format.  What should that format be?
  3. Will it use clang-linker-wrapper for SYCL?


  6. ELF is not an issue anymore, Alex has a workaround that takes care of it
  7. We should move all of this to libomptarget.
  8. Plan to close it


  80. API for initializing a subset of supported platforms --continued


  1. Lots of env variables, make them part of the config
  2. Ideas to abstract away the ABI changes when the config structure is modified?


  1. Making the structure internal hides the problem, but is cumbersome to use, when multiple calls are needed to set it up
  2. Alex: do these changes related to env variables need to be a part of initialization?
  3. Joseph: env vars control different aspects of the platform (global cfg and device cfg)


  3. How do we decide which platforms to initialize?


  1. Use an enum (keep what we have now) or a bitfield that could be "or" of different values?
  2. Assume the host is always initialized
  3. Alex: do we allow external platforms (not compiled-in)?
  4. Joseph: this used to be allowed, but was never used.  Deleting it simplified the code


  4. In addition to the ability to filter out platforms there should be stable device identifiers


  1. SYCL has env variables to specify devices to use (identifiers provided by syclls)
  2. In order for that to work the device identifiers should be stable between applications.
  3. Proposal: add a requirement that plugins enumerate devices in the same order every time.


  81. Add context to offloading API


  1. [https://github.com/llvm/llvm-project/pull/158900](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/158900&sa=D&source=editors&ust=1779820786865986&usg=AOvVaw1B__ShoHbCI4peAWj4rhN7)
  2. Part of SYCL 2020 standard
  3. The plan is to make a prototype first to see what changes are required


  82. Dependency on old driver


  1. Some actions are different in the new driver


  1. Bundling is no longer needed, heterogeneous objects are now supported


  2. HIP is moving to the new driver
  3. A lot of cleanup can be done if the old driver is no longer needed


  1. Are there any other frontends that use the old driver? E.g. CUDA, OpenCL, SYCL
  2. SYCL is still working with the old driver, but is moving to the new one


  4. Plan: delete old driver in clang-23



* * *

#
