### 2022, Mar 2

### Agenda

  * Omp_target_memcpy_async


  * [https://reviews.llvm.org/D81989](https://www.google.com/url?q=https://reviews.llvm.org/D81989&sa=D&source=editors&ust=1778600246372302&usg=AOvVaw3noaKWlJEbbMvgR8_qer1h)


  * Plugin rewrite branch:


  * [https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commits/omp_cleanup_gpu_plugins&sa=D&source=editors&ust=1778600246372490&usg=AOvVaw3RF71hSZro6cwQAVFtULc3)


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246372789&usg=AOvVaw3W4usbAWSSA60Ju7GXBfKq)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246372883&usg=AOvVaw0DVy-1D6TWAet4pWEgd6Ut)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246373375&usg=AOvVaw25QueqehEZ9BAJs-Ogncpj)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246373622&usg=AOvVaw01dRGzmfPuM06bN04vrZu1) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246373913&usg=AOvVaw1-NPJvw-ctvekTqs8yyVYx)
  * Printf



  * JIT support


  * Prototype: [https://github.com/shiltian/llvm-project/tree/jit](https://www.google.com/url?q=https://github.com/shiltian/llvm-project/tree/jit&sa=D&source=editors&ust=1778600246374155&usg=AOvVaw3rk_l-sEsi8yXn6rikwnYU)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246374709&usg=AOvVaw35QJyn47fAPPAHQCQBYSmt)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246374843&usg=AOvVaw2KSw4SXAbcE39V4hHhtLrm) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246374942&usg=AOvVaw1BvPpZ9ikQTo-9K-ginVRC) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246375093&usg=AOvVaw2YyGryhGFn5QszZarkbx7G)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246375201&usg=AOvVaw0e9_u3Rv6j1Lpo4UI3rLRV)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots 


  * Currently on staging (https://lab.llvm.org/staging)


  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/155&sa=D&source=editors&ust=1778600246375524&usg=AOvVaw0jb-uD2En8aoPDJ2lmRNVx)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/154&sa=D&source=editors&ust=1778600246375628&usg=AOvVaw0MxRiuwUmxCD9eeXypvViV)


  * Typically requires ~1 week constant green before moving to production
  * [nvptx64-nvidia-cuda::bug49334 failing again](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54081&sa=D&source=editors&ust=1778600246375823&usg=AOvVaw1IdMoZNy0G3wrxPI3ZWtXD) [FLAKY]
  * [test-suite::omptargetvv-test_parallel_for_allocate-50_parallel_for-c.test](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/54082&sa=D&source=editors&ust=1778600246375971&usg=AOvVaw1peufnTahgpLlWi86FoUnI) [REVERTED]


  * OMPT target support


  * Callback support


  * Presentation slides about OMPT initialization for target devices: [https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc](https://www.google.com/url?q=https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc&sa=D&source=editors&ust=1778600246376230&usg=AOvVaw2g6a9LUzXQvH1vrASctqa1) 
  * Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246376397&usg=AOvVaw1nVmd4mVBmso342YwFTHhl)


  * Device tracing support


  * Needs review [⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246376572&usg=AOvVaw0dyYb1KoeNtPMvzTbN-Y5T)


  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows. Dhruva: D113728 and D118424 do not introduce sharing of any C++ object between libomp, libomptarget, or plugins -- so Windows build should not have this problem. However, a Windows build has not been verified.
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246377038&usg=AOvVaw2AT7I3FO9BSOfHgbIRUuWo) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246377221&usg=AOvVaw2l7P8cg2WGpwW0rNVm9oiZ) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246377362&usg=AOvVaw34we-hdu2bQkCZ_64gsLjJ) Based on D99803


  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246377499&usg=AOvVaw2ACZBY3nDZ5_kSGht07qvv)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246377652&usg=AOvVaw1WI3xyILPzOMM8O2qbSv7G) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246377987&usg=AOvVaw3UE45OD76fQ79-kQAgmuaK)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246378464&usg=AOvVaw0_usKd8lbRuaqrUq98ggQb). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246378637&usg=AOvVaw1wqeT5ZPFb-5f6M1WtIsRh)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246378951&usg=AOvVaw2gUE_OGyudxTVu3pNLrGAQ)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246379172&usg=AOvVaw2We2-DwA8N_kLNkm9NiYpF)


  * Linking shared libraries with offloading code



###
