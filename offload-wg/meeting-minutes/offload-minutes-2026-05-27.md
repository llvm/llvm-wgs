# Wednesday, May 27, 9:00 - 10:00 am CDT

# Agenda

  1. Meta: meeting minutes will be stored in the llvm-wgs repo.


  1. [https://github.com/llvm/llvm-wgs](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs&sa=D&source=editors&ust=1782262385248847&usg=AOvVaw2n9gM6a_A9B4VZeqxMUqGr)
  2. [https://github.com/llvm/llvm-wgs/pull/20](https://www.google.com/url?q=https://github.com/llvm/llvm-wgs&sa=D&source=editors&ust=1782262385249047&usg=AOvVaw2hbTglrZ_RhNfQFJCFHLmW)


  2. PR Review list


  1. [https://github.com/llvm/llvm-project/pull/196275](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/196275&sa=D&source=editors&ust=1782262385249517&usg=AOvVaw0Tfpa4P3oauFYUYTUcvSIj) 


  3. Follow up proposal to OL_KERNEL_LAUNCH_PROP_TYPE_SIZE:   [https://github.com/llvm/llvm-project/pull/194333](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/194333&sa=D&source=editors&ust=1782262385249913&usg=AOvVaw35XPpDI6yZMK5gIXNhlla7)
  4. Windows support for SYCL


  1. PR: [https://github.com/llvm/llvm-project/pull/187006](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385250321&usg=AOvVaw2c_EoyP3ITdRuz5FqWOBw7)


  1. [Compiling liboffload on Windows](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385250545&usg=AOvVaw1RtfDpFncR_9iYgHV_Tft6)
  2. [L0 implementation still needs a few tweaks](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385250768&usg=AOvVaw33kecsLv2on21iETRjZBtV)
  3. [It now works with Windows.  PR to be updated this week.](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385251014&usg=AOvVaw3mbNaw-BhW83n0-yA5SIKF)


  2. Joseph: the bulk of this is generic C code, so it shouldn't be hard to get it working


  5. OpenACC support


  1. NVIDIA is in the process of upstreaming OpenACC support in flang.  Will also upstream runtime implementation.
  2. Has prototype that uses liboffload/libomptarget
  3. RFC will published soon (within a couple of weeks)
  4. Joseph: sounds reasonable


  1. Noted that libomptarget should depend on liboffload, not the other way around.
  2. Public buildbot would be good to have


  5. Still working on it.  Making sure that the code that was going to be published with the RFC is in a good shape.
  6. RFC: [https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793](https://www.google.com/url?q=https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793&sa=D&source=editors&ust=1782262385253019&usg=AOvVaw2ko__XJE8PzqrsshIPL6r4)
  7. PR: [https://github.com/llvm/llvm-project/pull/197894](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/197894&sa=D&source=editors&ust=1782262385253348&usg=AOvVaw3LiZo2mS1WJxcAtYoZqIVh)



* * *

  8. The dependence issue may be addressed later.  Common code may be extracted into a support library.
  9. There will need to be a buildbot to test the OpenACC code.


  1. Joseph: we should have unit tests that will have better coverage (than OpenMP tests) including corner cases.


  10. Compiler support (in flang) will be upstreamed in parallel.
  11. Ivan will start creating non-draft PRs


  6. What queue model is liboffload representing?


  1. Joseph: it's a FIFO, but we don't want to guarantee that it will match any specific hardware.
  2. Libomptarget creates a single queue for a pack of operations including "nowait".
  3. Joseph: the user of liboffload should handle queuing (e.g. libomptarget)
