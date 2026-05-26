# Wednesday, May 13, 9:00 - 10:00 am CDT

# Agenda

  1. Meta: meeting minutes will be stored in the llvm-wgs repo.


  1. [https://github.com/llvm/llvm-wgs](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs&sa=D&source=editors&ust=1779820786790091&usg=AOvVaw0Fs5VmwXwGEeVEt-S75EeU)


  2. PR Review list


  1. [https://github.com/llvm/llvm-project/pull/184343](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/184343&sa=D&source=editors&ust=1779820786790460&usg=AOvVaw3ls2z-niNSUtXaB5azNk1J) 


  1. Adds option for cooperative kernel launch
  2. Lukasz removed sizes from the first PR.
  3. Merged


  2. [https://github.com/llvm/llvm-project/pull/196275](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/196275&sa=D&source=editors&ust=1779820786790918&usg=AOvVaw3AkhiDaf6WemxmkaaZW8Is) 


  3. Follow up proposal to OL_KERNEL_LAUNCH_PROP_TYPE_SIZE:   [https://github.com/llvm/llvm-project/pull/194333](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/194333&sa=D&source=editors&ust=1779820786791312&usg=AOvVaw3UryWzIfom14vAGhjsVl-b)
  4. Windows support for SYCL


  1. PR: [https://github.com/llvm/llvm-project/pull/187006](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786791699&usg=AOvVaw1ffVLPFOrk80QEU98NpoYf)


  1. [Compiling liboffload on Windows](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786791889&usg=AOvVaw05IkLK0gnKei3fOVPrgNo2)
  2. [L0 implementation still needs a few tweaks](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786792077&usg=AOvVaw3a2xSLqS1WAEnxsYwYbgOl)
  3. [It now works with Windows.  PR to be updated this week.](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1779820786792269&usg=AOvVaw2Ky0eZH57sk3V2UglBt9xN)


  2. Joseph: the bulk of this is generic C code, so it shouldn't be hard to get it working


  5. OpenACC support


  1. NVIDIA is in the process of upstreaming OpenACC support in flang.  Will also upstream runtime implementation.
  2. Has prototype that uses liboffload/libomptarget
  3. RFC will published soon (within a couple of weeks)
  4. Joseph: sounds reasonable


  1. Noted that libomptarget should depend on liboffload, not the other way around.
  2. Public buildbot would be good to have


  5. Still working on it.  Making sure that the code that was going to be published with the RFC is in a good shape.
  6. RFC: [https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793](https://www.google.com/url?q=https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793&sa=D&source=editors&ust=1779820786793964&usg=AOvVaw0sSkDNXFAo4wmEeG8xzq83)

* * *
