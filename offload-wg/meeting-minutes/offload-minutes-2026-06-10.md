# Wednesday, June 10, 9:00 - 10:00 am CDT

# Agenda

  1. PR Review list
  2. Follow up proposal to OL_KERNEL_LAUNCH_PROP_TYPE_SIZE:   [https://github.com/llvm/llvm-project/pull/194333 (merged)](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/194333&sa=D&source=editors&ust=1782262385241389&usg=AOvVaw0UrKC1RsrITmfbE-Cx3R9z)


  1. Piotr working on a follow-up


  3. Windows support for SYCL


  1. PR: [https://github.com/llvm/llvm-project/pull/187006](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385241966&usg=AOvVaw06EtiI09pOi3Y6ahjQ2RIE)


  1. [Compiling liboffload on Windows](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385242177&usg=AOvVaw1CBfG8ppNTirghLrhxQZNO)
  2. [L0 implementation still needs a few tweaks](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385242401&usg=AOvVaw3BGp1ATnSzUokLe31qyoJc)
  3. [It now works with Windows.  PR to be updated this week.](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/187006&sa=D&source=editors&ust=1782262385242667&usg=AOvVaw2skSkL3gLWHzt6MDeowrlp)


  2. Joseph: the bulk of this is generic C code, so it shouldn't be hard to get it working
  3. All comments in the main PR have been addressed.
  4. There is one additional PR related to this: [https://github.com/llvm/llvm-project/pull/202540](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/202540&sa=D&source=editors&ust=1782262385243378&usg=AOvVaw2zQ6JlB-GBFh9vwWpKcI0s) 


  4. OpenACC support


  1. NVIDIA is in the process of upstreaming OpenACC support in flang.  Will also upstream runtime implementation.
  2. Has prototype that uses liboffload/libomptarget
  3. RFC will published soon (within a couple of weeks)
  4. Joseph: sounds reasonable


  1. Noted that libomptarget should depend on liboffload, not the other way around.
  2. Public buildbot would be good to have


  5. Still working on it.  Making sure that the code that was going to be published with the RFC is in a good shape.
  6. RFC: [https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793](https://www.google.com/url?q=https://discourse.llvm.org/t/openacc-runtime-in-llvm-offload-libacctarget/90793&sa=D&source=editors&ust=1782262385245167&usg=AOvVaw07YVyCBiDwAfWelmHqbffn)
  7. PR: https://github.com/llvm/llvm-project/pull/197894
  8. The dependence issue may be addressed later.  Common code may be extracted into a support library.
  9. There will need to be a buildbot to test the OpenACC code.


  1. Joseph: we should have unit tests that will have better coverage (than OpenMP tests) including corner cases.


  10. Compiler support (in flang) will be upstreamed in parallel.
  11. Ivan will start creating non-draft PRs


  5. RFC ["Proposed extension to the --offload-arch option"](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-proposed-extension-to-the-offload-arch-option/90790&sa=D&source=editors&ust=1782262385246634&usg=AOvVaw3-nb9HyYz7BWdff5tNreUD).  What are the remaining open issues, and how can we drive this to a conclusion?


  1. RFC: [https://discourse.llvm.org/t/rfc-proposed-extension-to-the-offload-arch-option/90790](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-proposed-extension-to-the-offload-arch-option/90790/23&sa=D&source=editors&ust=1782262385247214&usg=AOvVaw2iZoNT3HQFXS5iveu0b70N)
  2. Joseph: concerned about increase in complexity in the driver, these flags should instead be toolchain-specific; not opposed to the options existing
  3. Greg: specifying virtual ISAs is common enough to warrant a driver (top-level) option, rest can be toolchain-specific.
  4. Joseph: ok with that
  5. More discussion (about specific option naming/syntax) to follow
  6. Slides: [offload arch](images/liboffload-offload-arch.pptx)


* * *
