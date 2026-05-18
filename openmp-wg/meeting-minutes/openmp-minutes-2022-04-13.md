### 2022, April 13

### Agenda

  * New Driver binary format for bundling metadata


  * [https://reviews.llvm.org/D122069](https://www.google.com/url?q=https://reviews.llvm.org/D122069&sa=D&source=editors&ust=1778600246321545&usg=AOvVaw18rICRZfznBPh_798wWB2Z)


  * [https://discourse.llvm.org/t/openmp-runtime-code-owner/61594](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-runtime-code-owner/61594&sa=D&source=editors&ust=1778600246321685&usg=AOvVaw2suEQPHz-ciQBK0Jd3Ggbh) 
  * New OpenMP driver has been made default
  * Compiling CUDA with the new driver is up for review [https://reviews.llvm.org/D123812](https://www.google.com/url?q=https://reviews.llvm.org/D123812&sa=D&source=editors&ust=1778600246321881&usg=AOvVaw0vLhm6X4xjdc0qEnlQZdDm). Allows OpenMP Offloading to be compiled with and call CUDA.
  * Omp_target_memcpy_async


  * [https://reviews.llvm.org/D81989](https://www.google.com/url?q=https://reviews.llvm.org/D81989&sa=D&source=editors&ust=1778600246322071&usg=AOvVaw0wFlhuVL0GEtsOSTRZTGsY)


  * Issues:


  * AMD: [https://github.com/llvm/llvm-project/issues/54156](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54156&sa=D&source=editors&ust=1778600246322255&usg=AOvVaw03Y5J5K9ez--bAPrmbCj1H)
  * AMD: [https://github.com/llvm/llvm-project/issues/52706](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/52706&sa=D&source=editors&ust=1778600246322386&usg=AOvVaw1wuvaW5sWywvOJM0BaSAzf) <\- "solved now" *but* -disable-promote-alloca-to-vector was needed before. That pass is broken when you have an array of pointers, IMHO.
  * Host: [https://github.com/llvm/llvm-project/issues/54422](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54422&sa=D&source=editors&ust=1778600246322644&usg=AOvVaw09UMPFEcgy0xXFFK0gjaaM)
  * Shared pointer on device: [https://github.com/llvm/llvm-project/issues/54186](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54186&sa=D&source=editors&ust=1778600246322780&usg=AOvVaw3NXmHkt-DZ8FVsVZMjBmq9)


  * [https://godbolt.org/z/hzbTxbe8x](https://www.google.com/url?q=https://godbolt.org/z/hzbTxbe8x&sa=D&source=editors&ust=1778600246322869&usg=AOvVaw1xGCALYJ1N5jtrve11r872)


  * [https://github.com/llvm/llvm-project/issues/54654](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54654&sa=D&source=editors&ust=1778600246322990&usg=AOvVaw0sdTW2u3gDRD9M3Wyr8pf8) Solved.


  * Plugin rewrite branch:


  * [https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins&sa=D&source=editors&ust=1778600246323207&usg=AOvVaw2u8WJ5i3A35iHi5WYoDGhM)


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246323526&usg=AOvVaw3a0gyo2XrGoe0upJACyMGs)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246323627&usg=AOvVaw0-AMw8Ncf90qB2D3jZgJY8)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246324091&usg=AOvVaw0eD4GS1oKpIuuIytEM_sFV)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246324340&usg=AOvVaw3KfknYSlPvmXtisSb20zUA) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246324662&usg=AOvVaw0V5KvReeeZnWKAvDnOT-7o)
  * Printf



  * JIT support


  * Prototype: [https://github.com/shiltian/llvm-project/tree/jit](https://www.google.com/url?q=https://github.com/shiltian/llvm-project/tree/jit&sa=D&source=editors&ust=1778600246324897&usg=AOvVaw3_mfef2LKrMkafgdQ3LI51)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246325440&usg=AOvVaw1u2dbEws8udDzmhefQcYvq)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246325591&usg=AOvVaw1_4wm6TIbPjHJ07aD76bO9) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246325696&usg=AOvVaw25VT--KuzO0gd8aIxuKo3m) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246325836&usg=AOvVaw2OUbYxKRvLTJYvyJUEVmPd)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246325938&usg=AOvVaw1z7gSq6aNWBY2wvdUGifqF)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots 


  * Currently on staging (https://lab.llvm.org/staging)


  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/155&sa=D&source=editors&ust=1778600246326263&usg=AOvVaw2vNeiD6yvQBtNpHxCusO5q)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/154&sa=D&source=editors&ust=1778600246326365&usg=AOvVaw3rOUw7dihXXd-DRM3kQqxj)


  * Typically requires ~1 week constant green before moving to production
  * [intermittent failures in map_back_race.cpp for x64 offloading target](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54618&sa=D&source=editors&ust=1778600246326582&usg=AOvVaw2dXbrQJDmnVgK34uL0kC4Q) [FLAKY]
  * [nvptx64-nvidia-cuda::bug49334 failing again](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54081&sa=D&source=editors&ust=1778600246326714&usg=AOvVaw06UA_JKhkvxQ4BQ5Eucjjr) [FLAKY]


  * OMPT target support


  * Callback support


  * [D113728](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246326881&usg=AOvVaw23vGuLJ7PFgGbJGShNj1kU) will be split up into a stack of smaller patches. Current top of stack: [D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246326991&usg=AOvVaw2Cmt8zN74EU4UIjy4Kdkra)
  * Presentation slides about OMPT initialization for target devices: [https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc](https://www.google.com/url?q=https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc&sa=D&source=editors&ust=1778600246327173&usg=AOvVaw0FJYPiM0L_xjmnJPAtR3Ve) 
  * Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246327342&usg=AOvVaw2TABU4D5mkQ5pgcJhWsClT)


  * Device tracing support


  * Needs review [⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246327518&usg=AOvVaw1vTEl7YiNV5V4f17JOrB_x)


  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows. Dhruva: D113728 and D118424 do not introduce sharing of any C++ object between libomp, libomptarget, or plugins -- so Windows build should not have this problem. However, a Windows build has not been verified.
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246328013&usg=AOvVaw29kBWZOKWA6uPnAGurLn-q) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246328176&usg=AOvVaw1GKQ2_ZsAI3u0U5Cebe0t1) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246328308&usg=AOvVaw1hBwzHkAXTxpD5SQwphSq5) Based on D99803


  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246328465&usg=AOvVaw2_Z6OXP4-iakdyw7sCA5Tt)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246328614&usg=AOvVaw0uGk7ZOH2ZODFn9tzWhl9A) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246328969&usg=AOvVaw17si2K4r1AqcVdpNS8vfjB)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246329447&usg=AOvVaw2JvzCk5qP3OLtohd0sM1bc). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246329622&usg=AOvVaw2XfhQd2oQ-zF5at-WfMuXv)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246329914&usg=AOvVaw0L8KzciWabuSBqWKgvQaeq)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246330150&usg=AOvVaw354rtaXUJrJ9qrsSzUcH8S)


  * Linking shared libraries with offloading code



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246330451&usg=AOvVaw1mSHatdXDdCdbu-OJ4v7oQ)



### Patches to look at

[⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246330708&usg=AOvVaw1dCgZ9kNk4hVGLqzdBdlFM)

[⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246330837&usg=AOvVaw04U9syZNSiRs493NmnbGsz)
