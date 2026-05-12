### 2022, Jan 05

### Agenda

  * Offloading driver update: [OpenMP Offloading Driver Update](https://www.google.com/url?q=https://docs.google.com/presentation/d/1QXKSdBWhLaUHyrI-dgd2yHMux3w_q2EF2sROyO0u52k/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246422191&usg=AOvVaw1nB7s3vG9Y3n3VHauNA3Xc)


  * [https://reviews.llvm.org/D116541](https://www.google.com/url?q=https://reviews.llvm.org/D116541&sa=D&source=editors&ust=1778600246422291&usg=AOvVaw3_hsdZWxPptAq4qWvurcVn)


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246422584&usg=AOvVaw1zJgW88YvDYITHoXapjcPT)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246422678&usg=AOvVaw0iF5tfSR1CSXRp7qGVpGR-)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246423125&usg=AOvVaw1vJQeOyyLv3fjCQCVA1Nq6)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246423501&usg=AOvVaw2oZP1fZ1j97lpJGISw_uJy)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246424020&usg=AOvVaw1AtLs2poLAEBLzy3lTZg-Y) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246424137&usg=AOvVaw3pY5pB4K8cwPwGyIb_Pls4) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246424274&usg=AOvVaw1bNcrn6jDdEodhkwJWTkKo)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently offline
  * Don't clean source dir


  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246424587&usg=AOvVaw1XdSIeCtm4P-Z1qPEMpnYC)
  * Partially fixed: [https://reviews.llvm.org/rZORG5ba5d2e80969](https://www.google.com/url?q=https://reviews.llvm.org/rZORG5ba5d2e80969&sa=D&source=editors&ust=1778600246424723&usg=AOvVaw09l7RLt0cfkZKzqGkWGu4y)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246424798&usg=AOvVaw39sv5BvTwK7ASNY1KjQ1d8); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246424852&usg=AOvVaw0Vx2YrJ4RHhzFuf4Ok1EJ1) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda-newRTL::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246425140&usg=AOvVaw0eWDH7eB_xT0IwzLcpYfvP) (accepted, but not committed)


  * OMPT target support


  * AMD upstreaming JMC's implementation of the callback interface. Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246425435&usg=AOvVaw1rPN6SGJx-zTAVEEM3QVfm)
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246425637&usg=AOvVaw2VsWJOHOPAp6wymY3dvxCG) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246425788&usg=AOvVaw2Lt46j46nkhU9JKE-5Ykit) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246425923&usg=AOvVaw0aykWlZtWhswu4IMVZSf2t) Based on D99803


  * Device tracing (or trace records) implementation will come separately (review not yet posted)
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246426183&usg=AOvVaw3ctgwvDEgU8OzLq0PNFh-4)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246426335&usg=AOvVaw2JKKbhfulXQH3v_UdfTeBT) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246426701&usg=AOvVaw134_IB2dzJVyTakXDxWQq1)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246427122&usg=AOvVaw1f8SvofTcYacEuKnW5Fuu1). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246427295&usg=AOvVaw2Q6Qm8PuKytTiFL4b00LPT)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246427565&usg=AOvVaw0bQIpVpSIpN9o-WnfFxd02)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246427768&usg=AOvVaw1LRsLOX_wwDdohSaTEgTvS)


  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246428241&usg=AOvVaw2eG9K0CiaUEaJCGT5K9MSt)



### Patches to look at

[⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246428444&usg=AOvVaw0gO6oM0UC4EnUHDdO3OlQx)

###
