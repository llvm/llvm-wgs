# Wednesday, April 15, 9:00 - 10:00 am CDT

# Agenda

  12. PR Review list


  1. [https://github.com/llvm/llvm-project/pull/174955 - defered, needs update](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/174955&sa=D&source=editors&ust=1779820786801335&usg=AOvVaw0ukDMIDXCM2H3wzVZFZqsB)
  2. [https://github.com/llvm/llvm-project/pull/184343](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/184343&sa=D&source=editors&ust=1779820786801680&usg=AOvVaw3Dk3Ntr6ayWmQpVE5ETm52) 
  3. [https://github.com/llvm/llvm-project/pull/191100](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/191100&sa=D&source=editors&ust=1779820786802104&usg=AOvVaw3oHWu_1m8z1wab1Fg8lqor)


  13. Bump minimum supported version of CUDA


  1. CUDA version for launch API (11.8)
  2. Since Volta: independent thread scheduling API


  1. Need to use cooperative dispatch


  3. Ivan: A patch was merged that inadvertently uses a function from 12.4.  This will be addressed separately.


  14. Dumping intermediate binaries for SPIRV


  1. An option for the runtime to do that, Joseph had concerns
  2. SPIRV requires more complex compilation jobs in runtime, dumping the intermediate files seems useful
  3. Joseph: ideally we'd have generic tools for this, but this may be complicated
  4. Alex: have a tool that uses runtime
  5. They went with an alternative approach


  1. Did it through offloading binary and improving the tooling.


  6. Slowly progressing


  15. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. Worked on.  Updates will be provided as needed.
  2. With olCreateProgram we're assuming ELF, but for L0 we need to support SPIRV and other types.  Alex may have other ideas about how to address it.
  3. The initial image doesn't need to be ELF anymore.


  16. Windows support for SYCL


  1. PR: [https://github.com/llvm/llvm-project/pull/187006](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786804975&usg=AOvVaw3vVx9uM82b5B7rW7xpKivQ)


  1. [Compiling liboffload on Windows](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786805193&usg=AOvVaw3-33HN-EyvVg5vHs2Vt6qm)
  2. [L0 implementation still needs a few tweaks](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786805368&usg=AOvVaw3Sxx3SZqG8bPLtMALm6wok)
  3. [It now works with Windows.  PR to be updated this week.](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786805553&usg=AOvVaw3EVuj0YsnvV_ROi6qc1Be5)


  2. Joseph: the bulk of this is generic C code, so it shouldn't be hard to get it working


  17. OpenACC support


  1. NVIDIA is in the process of upstreaming OpenACC support in flang.  Will also upstream runtime implementation.
  2. Has prototype that uses liboffload/libomptarget
  3. RFC will published soon (within a couple of weeks)
  4. Joseph: sounds reasonable


  1. Noted that libomptarget should depend on liboffload, not the other way around.


  5. Public buildbot would be good to have


  18. Emissary API demo (done on April 1)


  1. https://github.com/llvm/llvm-project/pull/187602 
  2. Will show what an API developer needs to do, in contrast to what's there today.
  3. Joseph: this adds a lot of complexity that may not be necessary, specifically changes in clang codegen



Greg: this is much more convenient for a developer, and it's significantly faster

* * *
