### 2022, April 06

### Agenda

  * Dispatch and interop support 
  * Omp_target_memcpy_async


  * [https://reviews.llvm.org/D81989](https://www.google.com/url?q=https://reviews.llvm.org/D81989&sa=D&source=editors&ust=1778600246331124&usg=AOvVaw1fUtupXhB3c8eCW95RYXyd)


  * New Driver binary format for bundling metadata


  * [https://reviews.llvm.org/D122069](https://www.google.com/url?q=https://reviews.llvm.org/D122069&sa=D&source=editors&ust=1778600246331292&usg=AOvVaw0CE5DZlngHV5oqprmkEvAN)
  * [Improving the OpenMP Offloading Driver: LTO, libraries, and toolchains](https://www.google.com/url?q=https://docs.google.com/presentation/d/1A5-fkV-_pJEFtUenZaAaOOcb9-6n1u9s5JpuPQkfMqY/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246331393&usg=AOvVaw38OhYH2AJHyjp5qwpxzpeQ) (Overview talk)


  * Issues:


  * AMD: [https://github.com/llvm/llvm-project/issues/54156](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54156&sa=D&source=editors&ust=1778600246331582&usg=AOvVaw2vCEvjiL2FJPf2WdOKPmwp)
  * AMD: [https://github.com/llvm/llvm-project/issues/52706](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/52706&sa=D&source=editors&ust=1778600246331707&usg=AOvVaw1lMV45KF305KUIwXtInZFd) <\- "solved now" *but* -disable-promote-alloca-to-vector was needed before. That pass is broken when you have an array of pointers, IMHO.
  * Host: [https://github.com/llvm/llvm-project/issues/54422](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54422&sa=D&source=editors&ust=1778600246331964&usg=AOvVaw1zDpy1xTxWKnqkhINehE2d)
  * Shared pointer on device: [https://github.com/llvm/llvm-project/issues/54186](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54186&sa=D&source=editors&ust=1778600246332101&usg=AOvVaw3RdDeIQ3ABPcB1V_Scm7yq)


  * [https://godbolt.org/z/hzbTxbe8x](https://www.google.com/url?q=https://godbolt.org/z/hzbTxbe8x&sa=D&source=editors&ust=1778600246332204&usg=AOvVaw1z9IZuCQYljIKej86Gi5HZ)


  * [https://github.com/llvm/llvm-project/issues/54654](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54654&sa=D&source=editors&ust=1778600246332317&usg=AOvVaw07OtX6nU8I0IBJsEdsq7z3) 


  * Plugin rewrite branch:


  * [https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins&sa=D&source=editors&ust=1778600246332502&usg=AOvVaw2Xtq1TVyNhE1apCstwJ7v9)


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246332798&usg=AOvVaw0e4FOiE5i0tBYW4IkdxeW9)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246332901&usg=AOvVaw1a_7mnaFyTcRH0v3xRvzwu)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246333351&usg=AOvVaw3M3J_o_dB9yniUGOolAF_8)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246333592&usg=AOvVaw0Dt3c5x9pdHGmyrE0mL5UE) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246333878&usg=AOvVaw2S9tM2PX5gvrYP__A5iSWv)
  * Printf



  * JIT support


  * Prototype: [https://github.com/shiltian/llvm-project/tree/jit](https://www.google.com/url?q=https://github.com/shiltian/llvm-project/tree/jit&sa=D&source=editors&ust=1778600246334092&usg=AOvVaw2FzssKBv8qWRNgeTsfCeJr)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246334610&usg=AOvVaw2wwp87ASRMXMmJ0Kh7R3DD)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246334749&usg=AOvVaw2kTRnZrQdTTb9lJbcFSZQb) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246334857&usg=AOvVaw0yYHf4u510a1OeNUunstKL) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246335015&usg=AOvVaw2xAkjFCIQYCxn63d4GG-2k)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246335154&usg=AOvVaw2HI54PYECZ1p-HY9XjpCaS)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots 


  * Currently on staging (https://lab.llvm.org/staging)


  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/155&sa=D&source=editors&ust=1778600246335464&usg=AOvVaw2kddfG0s_FGi7edHGwVpiA)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/154&sa=D&source=editors&ust=1778600246335555&usg=AOvVaw1Ps8X3KB0fEeAJ0QfrpjlL)


  * Typically requires ~1 week constant green before moving to production
  * [intermittent failures in map_back_race.cpp for x64 offloading target](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54618&sa=D&source=editors&ust=1778600246335765&usg=AOvVaw2zh0G6rMF8_f82U9-kVX6_) [FLAKY]
  * [nvptx64-nvidia-cuda::bug49334 failing again](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54081&sa=D&source=editors&ust=1778600246335883&usg=AOvVaw2X5Fs2sVuWUt1kbMP-_We0) [FLAKY]


  * OMPT target support


  * Callback support


  * Presentation slides about OMPT initialization for target devices: [https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc](https://www.google.com/url?q=https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc&sa=D&source=editors&ust=1778600246336159&usg=AOvVaw2vUHhBKMGSISab2da13QKU) 
  * Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246336324&usg=AOvVaw22VB6O_N-OEc1bWMGR-oJL)


  * Device tracing support


  * Needs review [⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246336511&usg=AOvVaw020Tcyq_GxEhNUxZPm6uRg)


  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows. Dhruva: D113728 and D118424 do not introduce sharing of any C++ object between libomp, libomptarget, or plugins -- so Windows build should not have this problem. However, a Windows build has not been verified.
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246337008&usg=AOvVaw0m8NbKDfD3yJnANWgDKEQ2) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246337166&usg=AOvVaw255AVx3lR-37_78MwhaObS) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246337301&usg=AOvVaw3P1dNbKs_XAMmjDQRnNVPu) Based on D99803


  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246337444&usg=AOvVaw3EPSBvTlWFLnWqIxi3dHMo)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246337589&usg=AOvVaw1cYD8BPQBHYXF73QK4kge4) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246337950&usg=AOvVaw3NURlxZuC0zI431bRQlhII)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246338427&usg=AOvVaw1cYvrPkaWrL6Gkf7O-Vp89). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246338591&usg=AOvVaw0grkZDZIlGzrebPGNGHn-B)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246338853&usg=AOvVaw0Qmfg4C7tlVxAf8j_whsEE)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246339079&usg=AOvVaw1R6zaLYeM-TTzacqa4buy1)


  * Linking shared libraries with offloading code



###
