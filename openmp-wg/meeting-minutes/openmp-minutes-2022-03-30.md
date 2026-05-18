### 2022, Mar 30

### Agenda

  * Omp_target_memcpy_async


  * [https://reviews.llvm.org/D81989](https://www.google.com/url?q=https://reviews.llvm.org/D81989&sa=D&source=editors&ust=1778600246339409&usg=AOvVaw1aBrbYONDuTk62oiwxSWul)


  * Copy back race:


  * [https://reviews.llvm.org/D121058](https://www.google.com/url?q=https://reviews.llvm.org/D121058&sa=D&source=editors&ust=1778600246339539&usg=AOvVaw2MXVVQui493gUlAyvPhoji)


  * New Driver binary format for bundling metadata


  * [https://reviews.llvm.org/D122069](https://www.google.com/url?q=https://reviews.llvm.org/D122069&sa=D&source=editors&ust=1778600246339720&usg=AOvVaw2CG3ID7yJUzqNItHNWFOo1)


  * Interaction between [⚙ D102107 [OpenMP] Codegen aggregate for outlined function captures (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246339910&usg=AOvVaw1CG93fMwppWtNNto37qBGA) and OpenMPOpt. Example: libomptarget/test/offloading/bug51982.c fails with this patch but passes when OpenMPOpt is disabled. In generic mode, I am seeing promotion of alloc_shared aggregate-object to stack that is then passed to parallel_51
  * Issues:


  * AMD: [https://github.com/llvm/llvm-project/issues/54309](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54309&sa=D&source=editors&ust=1778600246340307&usg=AOvVaw1cb9gITERdbTcIuz4Y8g_Y)
  * AMD: [https://github.com/llvm/llvm-project/issues/54156](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54156&sa=D&source=editors&ust=1778600246340445&usg=AOvVaw1y7H0dqu2MWuHHos7hRmpd)
  * AMD: [https://github.com/llvm/llvm-project/issues/54091](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54091&sa=D&source=editors&ust=1778600246340571&usg=AOvVaw0aYEj2dsxAVwyf8iIF21bS)
  * AMD: [https://github.com/llvm/llvm-project/issues/52706](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/52706&sa=D&source=editors&ust=1778600246340703&usg=AOvVaw3P_XVHjHPtjEWfEKkJfFr5) <\- "solved now" *but* -disable-promote-alloca-to-vector was needed before. That pass is broken when you have an array of pointers, IMHO.
  * [https://github.com/llvm/llvm-project/issues/54216](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54216&sa=D&source=editors&ust=1778600246340933&usg=AOvVaw1WYOlrk5xYVxrzU_goYgwU) <\- should be fixed soon
  * Host: [https://github.com/llvm/llvm-project/issues/54422](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54422&sa=D&source=editors&ust=1778600246341078&usg=AOvVaw0Jvvhu4fpfaumsWotqLnvk)
  * Shared pointer on device: [https://github.com/llvm/llvm-project/issues/54186](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54186&sa=D&source=editors&ust=1778600246341310&usg=AOvVaw1zvtijHjfLSSKgA9XIV9QZ)


  * [https://godbolt.org/z/hzbTxbe8x](https://www.google.com/url?q=https://godbolt.org/z/hzbTxbe8x&sa=D&source=editors&ust=1778600246341413&usg=AOvVaw2Wonuhp1-e3o8qVGrlxNPr)


  * Plugin rewrite branch:


  * [https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins&sa=D&source=editors&ust=1778600246341602&usg=AOvVaw3be1-w88770e29L_6hwXzA)


  * Non-determinism


  * [https://reviews.llvm.org/rG7211dbd01da3a0e2f3550e1987291b3c84f7ffc6](https://www.google.com/url?q=https://reviews.llvm.org/rG7211dbd01da3a0e2f3550e1987291b3c84f7ffc6&sa=D&source=editors&ust=1778600246341776&usg=AOvVaw0b8xRzlNgODnA9ruolJyYi)
  * https://reviews.llvm.org/rGe8fadafe774c7e601129be50cedce1dd20843cea


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246342165&usg=AOvVaw0DmBLVCH_IRTFtyLpjlodT)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246342276&usg=AOvVaw0p0ijdOCKslnq-sjm6jmeM)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246342744&usg=AOvVaw2XfreZ_EeMc-NVDvYLJnb4)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246342984&usg=AOvVaw2kiEdADNnycHBjWm4em6up) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246343311&usg=AOvVaw0gsAX0PPuQMNybRastkXhb)
  * Printf



  * JIT support


  * Prototype: [https://github.com/shiltian/llvm-project/tree/jit](https://www.google.com/url?q=https://github.com/shiltian/llvm-project/tree/jit&sa=D&source=editors&ust=1778600246343526&usg=AOvVaw13OYNAaVeGfz_hADuXALvq)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246344051&usg=AOvVaw2s2wG10bgmZX72nLcKfMB-)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246344202&usg=AOvVaw0JPQu4hxMwMB45Vlfky6Bo) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246344301&usg=AOvVaw372cP5ymxWoQYzsTq8JEL2) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246344441&usg=AOvVaw0qyUSHv-DyH5eeizZUL6s2)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246344533&usg=AOvVaw2K04DYZEnam8TDwp8Gkuey)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots 


  * Currently on staging (https://lab.llvm.org/staging)


  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/155&sa=D&source=editors&ust=1778600246344824&usg=AOvVaw0qmDSkdH2EK8vE9o-W4moQ)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/154&sa=D&source=editors&ust=1778600246344913&usg=AOvVaw0uSAVFZe9pA6GAZmf2iW3f)


  * Typically requires ~1 week constant green before moving to production
  * [nvptx64-nvidia-cuda::bug49334 failing again](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54081&sa=D&source=editors&ust=1778600246345101&usg=AOvVaw3T-aL95MszPVh8i1Kz3Ol1) [FLAKY]


  * OMPT target support


  * Callback support


  * Presentation slides about OMPT initialization for target devices: [https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc](https://www.google.com/url?q=https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc&sa=D&source=editors&ust=1778600246345372&usg=AOvVaw0w8bn54D_-OPQnSl51LPs1) 
  * Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246345539&usg=AOvVaw3oDvs0n0afW8cAWUq5L-cZ)


  * Device tracing support


  * Needs review [⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246345719&usg=AOvVaw2ZAtWh3wHzpFWk1P-ryKra)


  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows. Dhruva: D113728 and D118424 do not introduce sharing of any C++ object between libomp, libomptarget, or plugins -- so Windows build should not have this problem. However, a Windows build has not been verified.
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246346202&usg=AOvVaw2l_yOaMb7mIKfYkQfaHLia) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246346357&usg=AOvVaw19kcZy5GJ9QDWQVq5_sIN8) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246346488&usg=AOvVaw2R2czJUwM-uXPV49PCcEcc) Based on D99803


  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246346622&usg=AOvVaw2UUZ5q-dqe7_CVWukX4Eoy)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246346764&usg=AOvVaw0ULjvJYoMtJQI_wB_mv5h2) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246347127&usg=AOvVaw2lWfK2-jHrePZdWTs8Hd0A)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246347607&usg=AOvVaw1z4kFj-d2Z8aJaaEdpd5Jn). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246347773&usg=AOvVaw2Hi7JGpNVQ8UasRQnGz_PK)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246348041&usg=AOvVaw2L_kAZzURgP3G_Uyfb6W7O)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246348262&usg=AOvVaw2NSUo3pVJqQrmZHCyESlxF)


  * Linking shared libraries with offloading code



###
