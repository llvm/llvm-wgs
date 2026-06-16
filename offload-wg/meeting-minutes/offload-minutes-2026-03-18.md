# Wednesday, March 18, 9:00 - 10:00 am CDT

# Agenda

  27. PR Review list


  1. [https://github.com/llvm/llvm-project/pull/174955](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174955&sa=D&source=editors&ust=1779820786813376&usg=AOvVaw2bTxG4_ZebUlG8pjeSwaH2)
  2. [https://github.com/llvm/llvm-project/pull/184343](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/184343&sa=D&source=editors&ust=1779820786813575&usg=AOvVaw2iEXI3QZ285GwP1ZE3PpZ0) 


  28. Bump minimum supported version of CUDA


  1. CUDA version for launch API (11.8)
  2. Since Volta: independent thread scheduling API


  29. Dumping intermediate binaries for SPIRV


  1. An option for the runtime to do that, Joseph had concerns
  2. SPIRV requires more complex compilation jobs in runtime, dumping the intermediate files seems useful
  3. Joseph: ideally we'd have generic tools for this, but this may be complicated
  4. Alex: have a tool that uses runtime
  5. They went with an alternative approach


  1. Did it through offloading binary and improving the tooling.


  30. Level zero plugin


  1. Level 0 has landed, Intel working on improving test success rate


  31. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. Worked on.  Updates will be provided as needed.


  32. PR to remove standalone build for offload


  1. [https://github.com/llvm/llvm-project/pull/170693](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/170693&sa=D&source=editors&ust=1779820786815737&usg=AOvVaw0rXnq7SlTxZaIL-CLR9jwc) 


  1. Undergoing updates.  Work in progress.
  2. Will be updated today.


  33. AMDGPU Buildbots Update: Bots will be migrated to a manylinux-based docker image with gcc-13 toolchain. As part of it RHEL 8, RHEL 9, SLES 15 and at some point also Ubuntu buildbots will or may be retired.


  1. Dockerfiles to set up environment will be public.
  2. Timeline not fully clear, but test coverage always given.
  3. Most importantly: If people want coverage with a particular (old) GCC toolchain version that might not be something that we can provide.


  34. Presentation about OMPT by Michael Halkenhauser in OpenMP in LLVM meeting on Feb 25.  Seeking feedback from the community.


  1. Slides: [LLVM-OpenMP-OMPT-Upstreaming-2026-02-25 - Google Slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1s3bhaZbhhmFODF_oT0k7CMi7zQg_A1VjTbVn6qpNnw8/edit?slide%3Did.g3aab30c8bc6_0_5%23slide%3Did.g3aab30c8bc6_0_5&sa=D&source=editors&ust=1779820786817304&usg=AOvVaw3SIbVDlbLH4sdBWKWskjgN)
  2. PR underway

* * *
