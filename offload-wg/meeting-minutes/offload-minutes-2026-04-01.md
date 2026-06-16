# Wednesday, April 1, 9:00 - 10:00 am CDT

# Agenda

  19. PR Review list


  1. [https://github.com/llvm/llvm-project/pull/174955](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174955&sa=D&source=editors&ust=1779820786807833&usg=AOvVaw2UR2vyE_DtO_V__blIdkVq)
  2. [https://github.com/llvm/llvm-project/pull/184343](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/184343&sa=D&source=editors&ust=1779820786808033&usg=AOvVaw3Qw4vDXo8uLiiaVI5iRUqJ) 
  3. [https://github.com/llvm/llvm-project/pull/191100](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/191100&sa=D&source=editors&ust=1779820786808240&usg=AOvVaw2lAIREfSK_5Rk82rZ_Bo2R)


  20. Emissary API demo


  1. [https://github.com/llvm/llvm-project/pull/187602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187602&sa=D&source=editors&ust=1779820786808526&usg=AOvVaw0HdFmKAwjn-fdeA_GOPa0n) 
  2. Will show what an API developer needs to do, in contrast to what's there today.
  3. Joseph: this adds a lot of complexity that may not be necessary, specifically changes in clang codegen
  4. Greg: this is much more convenient for a developer, and it's significantly faster


  21. Bump minimum supported version of CUDA


  1. CUDA version for launch API (11.8)
  2. Since Volta: independent thread scheduling API


  1. Need to use cooperative dispatch


  22. Dumping intermediate binaries for SPIRV


  1. An option for the runtime to do that, Joseph had concerns
  2. SPIRV requires more complex compilation jobs in runtime, dumping the intermediate files seems useful
  3. Joseph: ideally we'd have generic tools for this, but this may be complicated
  4. Alex: have a tool that uses runtime
  5. They went with an alternative approach


  1. Did it through offloading binary and improving the tooling.


  23. Level zero plugin


  1. Level 0 has landed, Intel working on improving test success rate


  24. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. Worked on.  Updates will be provided as needed.
  2. With olCreateProgram we're assuming ELF, but for L0 we need to support SPIRV and other types.  Alex may have other ideas about how to address it.


  25. Presentation about OMPT by Michael Halkenhauser in OpenMP in LLVM meeting on Feb 25.  Seeking feedback from the community.


  1. Slides: [LLVM-OpenMP-OMPT-Upstreaming-2026-02-25 - Google Slides](https://www.google.com/url?q=https://docs.google.com/presentation/d/1s3bhaZbhhmFODF_oT0k7CMi7zQg_A1VjTbVn6qpNnw8/edit?slide%3Did.g3aab30c8bc6_0_5%23slide%3Did.g3aab30c8bc6_0_5&sa=D&source=editors&ust=1779820786811685&usg=AOvVaw1r_e8OJzJ3AAVSvLzDhZ96)
  2. PR underway


  26. Windows support for SYCL


  1. PR: [https://github.com/llvm/llvm-project/pull/187006](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786812237&usg=AOvVaw2-208xtCaYc1gWCxoGp4Fg)


  1. [Compiling liboffload on Windows](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786812399&usg=AOvVaw2cfkOkVvUpZ5R8A9Yb1qhu)
  2. [L0 implementation still needs a few tweaks](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786812557&usg=AOvVaw1KAvOav6anZj6GJkz4i1vm) 


  2. Joseph: the bulk of this is generic C code, so it shouldn't be hard to get it working

* * *
