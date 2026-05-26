# Wednesday, March 4, 9:00 - 10:00 am CST

# Agenda

  35. PR Review list


  1. https://github.com/llvm/llvm-project/pull/174955  
  2. [https://github.com/llvm/llvm-project/pull/174955](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174955&sa=D&source=editors&ust=1779820786818134&usg=AOvVaw395KNjUrlovstWr2JivoSP)  
https://github.com/llvm/llvm-project/pull/184343



  36. Bump minimum supported version of CUDA
  37. Dumping intermediate binaries for SPIRV


  1. An option for the runtime to do that, Joseph had concerns
  2. SPIRV requires more complex compilation jobs in runtime, dumping the intermediate files seems useful
  3. Joseph: ideally we'd have generic tools for this, but this may be complicated
  4. Alex: have a tool that uses runtime


  38. Level zero plugin


  1. A system with Intel hardware has been added to the upstream CI


  1. Next: Add tests that exercise this code.
  2. Only 10-15% tests passing, the rest was XFAILED.
  3. Next: work on getting the tests pass


  1. SPIRV device RTL was merged, but is not used yet


  1. Johannes has some fixes (https://github.com/jdoerfert/llvm-project/tree/spirv-offload), seems like lots of errors are caused by a small number of issues


  2. Adding unit tests for L0
  3. Testing of device RTL was enabled, but added more failures, work in progress to address these


  39. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. [...old discussion in prior meeting notes…]
  2. Joseph: Could we look up a global name in SPIRV for the kernel and iterate over the arguments?
  3. Next: see if this is possible. Piotr will discuss this internally
  4. There is an experimental API in L0 to get the argument sizes directly.  The existing launch kernel API can be implemented this way.
  5. The OpenCL is still an issue.


  1. Generic kernel launch API: [https://github.com/llvm/llvm-project/pull/176742](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/176742&sa=D&source=editors&ust=1779820786821832&usg=AOvVaw1MAtPte8y-T1Q91XS8yIq4)
  2. Working on generalizing the interface
  3. Lukasz is currently working on adding cooperative kernel launch support to the API, almost done


  40. API for initializing a subset of supported platforms --continued


  1. [...old discussion in prior meeting notes…]
  2. Joseph: thinking about how to make is ABI-stable. Make it append-only for future extensions?
  3. Low priority.
  4. Done.  Using size as the version.


  1. Using size seems to be easier than keeping a separate version, since all preexisting members need to be kept.
  2. Using version allows removing fields.
  3. Alex: version is more flexible


  41. Add context to offloading API


  1. [https://github.com/llvm/llvm-project/issues/171129](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/171129&sa=D&source=editors&ust=1779820786823567&usg=AOvVaw1LIZZn3gHZUoPcAaMYkRJv) 
  2. Part of SYCL 2020 standard
  3. The plan is to make a prototype first to see what changes are required
  4. Low priority, remove from agenda until this comes back


  42. PR to remove standalone build for offload


  1. [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1779820786824252&usg=AOvVaw3_2dKNmqtCkFlMMjgRV_hy) 


  1. Undergoing updates.  Work in progress.


  43. AMDGPU Buildbots Update: Bots will be migrated to a manylinux-based docker image with gcc-13 toolchain. As part of it RHEL 8, RHEL 9, SLES 15 and at some point also Ubuntu buildbots will or may be retired.


  1. Dockerfiles to set up environment will be public.
  2. Timeline not fully clear, but test coverage always given.
  3. Most importantly: If people want coverage with a particular (old) GCC toolchain version that might not be something that we can provide.


  44. Presentation about OMPT by Michael Halkenhauser in OpenMP in LLVM meeting on Feb 25.  Seeking feedback from the community.

* * *
