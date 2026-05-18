### 2022, Jan 26

### Agenda

  * OMPT Presentation
  * Offloading driver update: [OpenMP Offloading Driver Update](https://www.google.com/url?q=https://docs.google.com/presentation/d/1QXKSdBWhLaUHyrI-dgd2yHMux3w_q2EF2sROyO0u52k/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246401896&usg=AOvVaw1MCglvX1-mahY-K030PqwF)


  * [https://reviews.llvm.org/D116541](https://www.google.com/url?q=https://reviews.llvm.org/D116541&sa=D&source=editors&ust=1778600246401992&usg=AOvVaw1e8AW1KmEFf_TSpUm1S78Y)
  * [https://github.com/jhuber6/llvm-project/tree/NewDriver](https://www.google.com/url?q=https://github.com/jhuber6/llvm-project/tree/NewDriver&sa=D&source=editors&ust=1778600246402116&usg=AOvVaw0oME2x3Q6Qxly_cYSBgew9)


  * Old runtime broken on amdgpu at head (buildbot demoted to staging), plan of attack?


  * ^ still broken, deletion time ahead of release?
  * 

  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246402592&usg=AOvVaw2Zc6ZCRHHcYe108gb7L59L)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246402690&usg=AOvVaw1N7PM4vpryz8fNlJzxt1FE)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246403162&usg=AOvVaw02tQsbzTZircMNORz7yjdZ)


  * 12/22 status update:


  * Dependencies for host-offloading added (libelf-dev), now running in pre-merge checks


  * Pre-merge check issues: [https://github.com/llvm/llvm-project/issues/53266](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53266&sa=D&source=editors&ust=1778600246403473&usg=AOvVaw30IM2NzarHmOICvBoGpQn4) [closed]
  * With [https://reviews.llvm.org/D116906](https://www.google.com/url?q=https://reviews.llvm.org/D116906&sa=D&source=editors&ust=1778600246403589&usg=AOvVaw1ktyW1PBvCsaIrUjqiFmP2) all OvO test pass (O3) on MI100,


  * OpenMC on MI100 builds in unity build (sometimes)
  * What else is broken on AMD?


  * QMCPACK complex reduction
  * [https://github.com/llvm/llvm-project/issues/53290](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53290&sa=D&source=editors&ust=1778600246403883&usg=AOvVaw0vGgpphV13_Z08TYYFicAE)
  * Printf
  * 


  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246404129&usg=AOvVaw3KIMQNuZUiUz7lCoBABLWQ)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * GPU working group [https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html](https://www.google.com/url?q=https://lists.llvm.org/pipermail/llvm-dev/2022-January/154618.html&sa=D&source=editors&ust=1778600246404677&usg=AOvVaw29ZzVeSVIQcL3NAt81hIj_)
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246404820&usg=AOvVaw27ytRRYaVH0-J8a-a4p-ib) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246404941&usg=AOvVaw0iLl8Wji29GxHY0uMy_BbZ) (irbuilder)


  * OMP assumes, initial patch: [https://reviews.llvm.org/D91980](https://www.google.com/url?q=https://reviews.llvm.org/D91980&sa=D&source=editors&ust=1778600246405074&usg=AOvVaw1Ne4im1KL2ppI09vlRhuZX)
  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246405176&usg=AOvVaw2V951aNF7oqsMnbEIo2uOQ)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * [openmp-offload-cuda-project](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/11&sa=D&source=editors&ust=1778600246405474&usg=AOvVaw2c6DzXzYl2sTsYq1U3jSiq)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/13&sa=D&source=editors&ust=1778600246405570&usg=AOvVaw1ngpYZ7Gf_ElmXA7WnW56u)
  * [openmp-offload-cuda-singletarget](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/2/builds/37&sa=D&source=editors&ust=1778600246405669&usg=AOvVaw0DJuPhn1H9fiqB_-yzJgCq)
  * [openmp-offload-cuda-irbuilder](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/5&sa=D&source=editors&ust=1778600246405762&usg=AOvVaw0vZAnKC_trB9qBHZIy-Y_G)


  * OMPT target support


  * AMD upstreaming JMC's implementation of the callback interface. Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246406015&usg=AOvVaw2rcXEBDBvubeEFZHFQfnyO)
  * Ravi: Sharing class ompt_device_callbacks_t between plugin and runtime breaks building on windows
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246406328&usg=AOvVaw1gyEPErcGUYMMXWvVO-V8M) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246406486&usg=AOvVaw1AKEu6j497JidIPvRlIvNu) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246406616&usg=AOvVaw0XJYZIlukxZT7wUHhWoTxX) Based on D99803


  * Device tracing (or trace records) implementation will come separately (review not yet posted)
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246406848&usg=AOvVaw0q6NDqc8rDiRwlXf9FxyCk)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246406990&usg=AOvVaw2x2SprhmckVUc3nzlt-gem) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246407339&usg=AOvVaw1TboMo1DJNmhLcms6jGIb8)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting <\- been a long time, perhaps indicative that we should wrap the cuda object
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246407885&usg=AOvVaw2lnQHnh8z3Hd5ZHr1mYKAq). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246408060&usg=AOvVaw26hzAhxJi-dDWPz79pzYJd)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246408337&usg=AOvVaw0sFyD0r7gRo69Rd3WPoBmC)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246408554&usg=AOvVaw1yNz0XGMu-qNUA_jgpb3T1)


  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



###
