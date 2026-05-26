# Wednesday, April 29, 9:00 - 10:00 am CDT

# Agenda

  6. PR Review list


  1. [https://github.com/llvm/llvm-project/pull/184343](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/184343&sa=D&source=editors&ust=1779820786794789&usg=AOvVaw1T9N3jKEZ_8Zx7tj_o0kVZ) 


  1. Adds option for cooperative kernel launch
  2. Follow up proposal to OL_KERNEL_LAUNCH_PROP_TYPE_SIZE:   [https://github.com/llvm/llvm-project/pull/194333](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/194333&sa=D&source=editors&ust=1779820786795451&usg=AOvVaw142LEZJv9K70LESOCfUwaJ)
  3. Lukasz removed sizes from the first PR.


  7. Bump minimum supported version of CUDA


  1. CUDA version for launch API (11.8)
  2. PR merged: [https://github.com/llvm/llvm-project/pull/191100](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/191100&sa=D&source=editors&ust=1779820786796151&usg=AOvVaw0J9mp4A1I14M6h96DMRr5I)
  3. [Done](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/191100&sa=D&source=editors&ust=1779820786796276&usg=AOvVaw23fZEFbmkuK4iuxvKbAZ1q)


  8. Dumping intermediate binaries for SPIRV


  1. An option for the runtime to do that, Joseph had concerns
  2. SPIRV requires more complex compilation jobs in runtime, dumping the intermediate files seems useful
  3. Joseph: ideally we'd have generic tools for this, but this may be complicated
  4. Alex: have a tool that uses runtime
  5. They went with an alternative approach


  1. Did it through offloading binary and improving the tooling.


  6. Slowly progressing


  9. ELF Program Image in Plugin Interface. Biggest problem with running SYCL with L0 plugin right now. Should we add an argument to olCreateProgram to choose program image type?


  1. Worked on.  Updates will be provided as needed.
  2. With olCreateProgram we're assuming ELF, but for L0 we need to support SPIRV and other types.  Alex may have other ideas about how to address it.
  3. The initial image doesn't need to be ELF anymore.
  4. Complete


  10. Windows support for SYCL


  1. PR: [https://github.com/llvm/llvm-project/pull/187006](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786798489&usg=AOvVaw1q11D-cfu6Gg-8_LghfT31)


  1. [Compiling liboffload on Windows](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786798670&usg=AOvVaw1or0mNzf9GTLFFX62pI0ao)
  2. [L0 implementation still needs a few tweaks](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786798841&usg=AOvVaw2BlTaLa-qK19k0A11I5FaD)
  3. [It now works with Windows.  PR to be updated this week.](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786799065&usg=AOvVaw3Grt3uyxaVv7ogPRIb3S31)


  2. Joseph: the bulk of this is generic C code, so it shouldn't be hard to get it working


  11. OpenACC support


  1. NVIDIA is in the process of upstreaming OpenACC support in flang.  Will also upstream runtime implementation.
  2. Has prototype that uses liboffload/libomptarget
  3. RFC will published soon (within a couple of weeks)
  4. Joseph: sounds reasonable


  1. Noted that libomptarget should depend on liboffload, not the other way around.


  5. Public buildbot would be good to have

* * *
