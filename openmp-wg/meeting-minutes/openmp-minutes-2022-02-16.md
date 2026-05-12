### 2022, Feb 16

### Agenda

  * Which libraries to include when offloading to CPU.
  * AMDGPU libm - what to do with rocm dependency
  * Offloading driver update: [OpenMP Offloading Driver Update](https://www.google.com/url?q=https://docs.google.com/presentation/d/1QXKSdBWhLaUHyrI-dgd2yHMux3w_q2EF2sROyO0u52k/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246386724&usg=AOvVaw0Ntd61b444goFoyewjQA7r)


  * Added support for CPU offloading
  * New driver variant added for all tests in the openmp test suite


  * Linking shared libraries with offloading code
  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246387227&usg=AOvVaw28tWad31nCTHeuZK9jxD_-)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246387327&usg=AOvVaw1HIPCJl3H_cShK-aKRR0r8)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246387761&usg=AOvVaw3aB-nzKlCheuqTafN_odho)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246387999&usg=AOvVaw2ZMYyd1pSc-4V-iEjxjrTA) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246388290&usg=AOvVaw0apAY_Etz3Nv02N9GLOCi8)
  * Printf



  * JIT support


  * Prototype: [https://github.com/shiltian/llvm-project/tree/jit](https://www.google.com/url?q=https://github.com/shiltian/llvm-project/tree/jit&sa=D&source=editors&ust=1778600246388529&usg=AOvVaw2OMF-JUDXDE3ZeK1WqIsjA)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246389038&usg=AOvVaw1G9n7Y0d_uYpcsgZjosWWG)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246389175&usg=AOvVaw0r1OsUiZaXXkro0dE0MWJ1) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246389281&usg=AOvVaw068zRKX1aeGE3xrnTRte1y) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246389406&usg=AOvVaw22OxUeMPVwq2G5xagM14p3)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246389496&usg=AOvVaw1yEgQmU61vlLS0_dZ0B64C)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * [openmp-offload-cuda-project](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/11&sa=D&source=editors&ust=1778600246389813&usg=AOvVaw3Au_MthDE2hh6pbLgJNHbW)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/13&sa=D&source=editors&ust=1778600246389909&usg=AOvVaw1euCUP13Ok0ktUX59ZI_Pc)
  * [openmp-offload-cuda-singletarget](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/2/builds/37&sa=D&source=editors&ust=1778600246390011&usg=AOvVaw16DgNxTdcVYx5ESrJKAj8n)
  * [openmp-offload-cuda-irbuilder](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/5&sa=D&source=editors&ust=1778600246390102&usg=AOvVaw1aEsxn-BmMFY5nb-rPuQH3)


  * [Flaky test nvptx64-nvidia-cuda::bug49334.cpp](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53730&sa=D&source=editors&ust=1778600246390214&usg=AOvVaw07hUwpsLjN3R_RTd5EkXHr) [FLAKY]


  * OMPT target support


  * Callback support


  * Presentation slides about OMPT initialization for target devices: [https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc](https://www.google.com/url?q=https://rice.box.com/s/pf3gix2hs4d4o1aatwir1set05xmjljc&sa=D&source=editors&ust=1778600246390496&usg=AOvVaw2GHO1PBE72OX7E7W7DLIau) 
  * Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246390654&usg=AOvVaw1_82CaYd4O2aZcffHcF65Y)


  * Device tracing support


  * Needs review [⚙ D118424 Implementation of OMPT target device tracing (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D118424&sa=D&source=editors&ust=1778600246390839&usg=AOvVaw0_FF06M_oXdGMhRCrBRpui)


  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows. Dhruva: D113728 and D118424 do not introduce sharing of any C++ object between libomp, libomptarget, or plugins -- so Windows build should not have this problem. However, a Windows build has not been verified.
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246391376&usg=AOvVaw25mWW2opgSUGY8T8iBLa2a) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246391527&usg=AOvVaw3-JfC4FRVBFzLF2Yx0KO3H) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246391655&usg=AOvVaw3zgZ--TMULEEa-vXKOosmW) Based on D99803


  * Device tracing (or trace records) implementation will come separately (review not yet posted)
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246391884&usg=AOvVaw1zRqU0nCBbY7zXsyzQ85eC)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246392031&usg=AOvVaw3gGijqkcPfo6itfjjAMm3J) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246392390&usg=AOvVaw1Gu0fYRXnbTLoypZbtHx8q)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246392860&usg=AOvVaw1Uwq2qfLIPaAkxf586UbJz). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246393026&usg=AOvVaw3dbM0Ig6VeYSRvtHVAQdF9)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246393306&usg=AOvVaw3-ImQyR7zVm6bRA-Qd3KCa)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246393554&usg=AOvVaw3nLVZhYb13NZIsJzbrCp5t)


  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?  Completed by D118493



###
