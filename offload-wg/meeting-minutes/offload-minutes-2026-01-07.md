# Wednesday, January 7, 9:00 - 10:00 am CST

# Agenda

  69. PR Review list


  1. [OpenMP] Preserve the original address when use_device_ptr/addr lookup fails. ([#174659](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174659&sa=D&source=editors&ust=1779820786849411&usg=AOvVaw0k-BAmfNQaPN0FWcTkcfaM))


  1. \+ the stack for use_device_ptr(fb_nullify/preserve): [#169603](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/169603&sa=D&source=editors&ust=1779820786849693&usg=AOvVaw2eE2G3Oqw1u65RmjUQChXu), [#170578](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170578&sa=D&source=editors&ust=1779820786849799&usg=AOvVaw2kQNK4bv-Z4Mqk-bxUvTkn), [#173930](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/173930&sa=D&source=editors&ust=1779820786849904&usg=AOvVaw3zABi1H_VAVnE-gyd-Y0-v), [#173931](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/173931&sa=D&source=editors&ust=1779820786850007&usg=AOvVaw0QSBNrXd1K_tchv7FWhwhu) 


  70. Level zero plugin


  1. A system with Intel hardware has been added to the upstream CI


  1. Next: Add tests that exercise this code.


  71. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. Many ELF aspects are specific to OpenMP support
  2. Should move to libomptarget; might not work with CUDA/HIP anyways.
  3. Level Zero consumes SPIR-V and does not need ELF.
  4. Needs expansion of binary magic number detection.
  5. NEW: Formalizing program image format for olCreateProgram. Should it just accept Offload Binary (after its extended to support SYCL https://discourse.llvm.org/t/rfc-syclbin-a-format-for-sycl-device-code/88603/1 ) ?


  1. Working on extending olCreateProgram to accept other formats (e.g. SPIRV).


  1. [https://github.com/llvm/llvm-project/pull/166545](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/166545&sa=D&source=editors&ust=1779820786852086&usg=AOvVaw3_twTftuNtew_TaQoeUeBe) 


  2. It should really accept any offload format.  What should that format be?
  3. Will it use clang-linker-wrapper for SYCL?


  6. ELF is not an issue anymore, Alex has a workaround that takes care of it
  7. We should move all of this to libomptarget.
  8. Plan to close it
  9. Piotr has a PR for kernel launch changes:


  1. [https://github.com/llvm/llvm-project/pull/173263](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/173263&sa=D&source=editors&ust=1779820786853093&usg=AOvVaw3-5YPIAL7-vnkYxgKKTx2M)


  10. Joseph: we could implement code in the compiler that adds necessary information about the kernel arguments.
  11. Alex: we can't do that in SPIRV for OpenCL
  12. Joseph: Could we pre-compile SPIRV to ELF and have the rest of the code deal with ELF?
  13. Joseph: Could we look up a global name in SPIRV for the kernel and iterate over the arguments?
  14. Next: see if this is possible. Piotr will discuss this internally


  72. API for initializing a subset of supported platforms --continued


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


  1. SYCL has env variables to specify devices to use (identifiers provided by sycalls)
  2. In order for that to work the device identifiers should be stable between applications.
  3. Proposal: add a requirement that plugins enumerate devices in the same order every time.


  5. Joseph: thinking about how to make is ABI-stable. Make it append-only for future extensions?


  73. Add context to offloading API


  1. [https://github.com/llvm/llvm-project/issues/171129](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/171129&sa=D&source=editors&ust=1779820786857404&usg=AOvVaw2iMW3jm-vmIYkYYZjVAAM7) 
  2. Part of SYCL 2020 standard
  3. The plan is to make a prototype first to see what changes are required


  74. PR to remove standalone build for offload
  75. Dependency on old driver


  1. Some actions are different in the new driver


  1. Bundling is no longer needed, heterogeneous objects are now supported


  2. HIP is moving to the new driver
  3. A lot of cleanup can be done if the old driver is no longer needed


  1. Are there any other frontends that use the old driver? E.g. CUDA, OpenCL, SYCL
  2. SYCL is still working with the old driver, but is moving to the new one


  4. Plan: delete old driver in clang-23
  5. Joseph: working on getting the new driver in HIP, tests are green so far


  1. We'd get the new driver by default with opt-out in clang-22, and only the new driver in clang-23.



* * *
