### 2022, Feb 23

### Agenda

  * AMDGPU libm - what to do with rocm dependency
  * Plugin rewrite branch:


  * [https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins&sa=D&source=editors&ust=1778600246379620&usg=AOvVaw2H1s9n5Ho7gnhcnsjVzbGJ)


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246379934&usg=AOvVaw1CdsegMYftPrTL0u37ra84)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246380037&usg=AOvVaw3dLwzjSD2yXfKIKTsOcmyN)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246380491&usg=AOvVaw0Crc5wG4XudjQ_9m-TWq00)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246380737&usg=AOvVaw2gwmCWayQu2_Gln37e0zG2) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246381033&usg=AOvVaw2bL1rM3caiNZnzyHTuf5l4)
  * Printf



  * JIT support


  * Prototype: [https://github.com/shiltian/llvm-project/tree/jit](https://www.google.com/url?q=https://github.com/shiltian/llvm-project/tree/jit&sa=D&source=editors&ust=1778600246381265&usg=AOvVaw1sB7xR0mrQH9Rb5hCBGTSn)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246381782&usg=AOvVaw2apYzbvMBK7CZbdQAVC8-l)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246381909&usg=AOvVaw0hVv2r9MOacPZAObQDrHFV) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246382017&usg=AOvVaw3w1D28JS6-_ssK_u6OMzjV) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246382147&usg=AOvVaw3Nl0RP0fzebNOg0gH92Mto)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246382245&usg=AOvVaw3uqeKoDPuPU2_PYyekideO)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots 


  * Currently on staging (https://lab.llvm.org/staging)


  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/155&sa=D&source=editors&ust=1778600246382541&usg=AOvVaw1XPK8xkoW7BZcy_6DNbIg7)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/154&sa=D&source=editors&ust=1778600246382628&usg=AOvVaw0z5YwMVVQ6DW5aj10ksXYU)


  * Typical wait time ~1 week before moving to production


  * OMPT target support


  * Callback support


  * Presentation slides about OMPT initialization for target devices: [https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc](https://www.google.com/url?q=https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc&sa=D&source=editors&ust=1778600246382986&usg=AOvVaw0PFva2p-4JzkXwh4hJkBxy) 
  * Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246383155&usg=AOvVaw0_IlFolNrxLxHkbgee0375)


  * Device tracing support


  * Needs review [⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246383335&usg=AOvVaw22C8GOfXpkuCh0LNrzomR0)


  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows. Dhruva: D113728 and D118424 do not introduce sharing of any C++ object between libomp, libomptarget, or plugins -- so Windows build should not have this problem. However, a Windows build has not been verified.
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246383802&usg=AOvVaw2-A-z5_C1r_q6JMIoBR4k2) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246383946&usg=AOvVaw03OFTyK7xJmdse044YWrMz) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246384072&usg=AOvVaw2dU8tfvbalG981jDpD_2Ae) Based on D99803


  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246384229&usg=AOvVaw0gNoRx6PGm-nzfDBBEwOMq)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246384392&usg=AOvVaw3kpGegQbHiXrZQpVvV5P8Z) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246384746&usg=AOvVaw2vCZoixZ4UdUwIYeR7gANT)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246385226&usg=AOvVaw21bHjFfCOHj_MUwxCF9_r_). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246385399&usg=AOvVaw0lS4pfEMByWAqxYpZB-kKA)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246385670&usg=AOvVaw1QpiFKKCmLb483gM6Zs0vw)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246385895&usg=AOvVaw1O5i2wn7y7J118WTxID-y_)


  * Linking shared libraries with offloading code
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?  Completed by D118493



###
