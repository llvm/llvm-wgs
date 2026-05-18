### 2021, Dec 8

### Agenda

  * Default to openmp-version 5.1 (Saiyedul will review experience on switch to 5.0 default)


  * AMD propose that default change in LLVM 15 (after fork) and LLVM 14 default is 5.0


  * Offloading driver discussion: [OpenMP Offloading Driver Implementation](https://www.google.com/url?q=https://docs.google.com/presentation/d/1HCgOUsNcRVCd7MYBBTBgw4qACjWYjgsXkP1NMZcbSHI/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246435548&usg=AOvVaw3fuaSPLaBkVqzSBCDkHZsL)


  * Greg has some additional charts


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne
  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246435908&usg=AOvVaw26ZEUsBGr1EPWFwruYDk5a)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246436006&usg=AOvVaw0p0ArvinSEonqBJBVk0th5)
  * [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246436153&usg=AOvVaw1fajoNvDxkwlAhiVSm4NpC)


  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246436330&usg=AOvVaw0r5Xc6cgDldN_qTl0GyqkJ)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246436820&usg=AOvVaw1-WMOIltYwSaglZ_-zHtZd) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246436918&usg=AOvVaw3KVbiDvaN3kmHHnAsPUTub) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246437066&usg=AOvVaw2CjAhdBspT1owayRS5exty)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * [openmp-offload-cuda-project](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/11&sa=D&source=editors&ust=1778600246437373&usg=AOvVaw0-PgsQQ_5qFJmycZtw7xdg)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/13&sa=D&source=editors&ust=1778600246437462&usg=AOvVaw0w2FrHN0vNDA8IwqCiBjaF)


  * Stopped running omptarget tests since https://reviews.llvm.org/D113253


  * [openmp-offload-cuda-singletarget](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/2/builds/37&sa=D&source=editors&ust=1778600246437677&usg=AOvVaw2bDixsfw-r0XdrwTCNbTMK)
  * [openmp-offload-cuda-irbuilder](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/5&sa=D&source=editors&ust=1778600246437775&usg=AOvVaw1EtSneoobVbkbkl_Kpx1TD)


  * Don't clean source dir


  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246437909&usg=AOvVaw0ll42Rr64np2STcuBtz1Lq)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246437982&usg=AOvVaw3lskb52Pv_rzGUuDXbuspm); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246438043&usg=AOvVaw0a77-r1GZvheeeeH7QzymW) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda-newRTL::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246438350&usg=AOvVaw0KCVdtf6yxg5zQbfxbBP4t) (under review)


  * Compile failure


  * FAILED: projects/openmp/libomptarget/plugins/amdgpu/CMakeFiles/omptarget.rtl.amdgpu.dir/impl/impl.cpp.o
  * Possible cause: https://reviews.llvm.org/D115279


  * OMPT target support


  * AMD upstreaming JMC's implementation of the callback interface. Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246438855&usg=AOvVaw0Sk-tpLMTN-aESHUbW1lXW)
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246439068&usg=AOvVaw02LXROoNmuAXbF4Px99VQB) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246439221&usg=AOvVaw0d8l28749F7Xi7JFbv7c5l) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246439360&usg=AOvVaw03xvMSZRHxrG6z9IDjrJta) Based on D99803


  * Device tracing (or trace records) implementation will come separately (review not yet posted)
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246439595&usg=AOvVaw0Zc86d6fLUdruLQ-2Xq5u7)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246439738&usg=AOvVaw3qf8gH5gf6wKnNfhdtyO-o) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246440074&usg=AOvVaw1vh3lbDnC4AlBN3vPoPgNU)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246440487&usg=AOvVaw3A_DbJDtpvxk2Ojj3brScf). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246440659&usg=AOvVaw2BrUp_HUbzgcd41gX2pAgw)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246440928&usg=AOvVaw0k9nUkVFw0Q-IRS9cMl6Cv)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246441152&usg=AOvVaw09r8dX0OB2W1HeLVguZ3Fw)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246441314&usg=AOvVaw3IqGciXIV687ltEvAkxsqx)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



###
