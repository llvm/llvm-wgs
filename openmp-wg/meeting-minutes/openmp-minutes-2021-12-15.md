### 2021, Dec 15

### Agenda

  * Offloading driver discussion: [OpenMP Offloading Driver Implementation](https://www.google.com/url?q=https://docs.google.com/presentation/d/1HCgOUsNcRVCd7MYBBTBgw4qACjWYjgsXkP1NMZcbSHI/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246428698&usg=AOvVaw2TwzLuE91kFzl97hGFmnFk)


  * Greg has some additional charts


  * Exploring using Pre-Commit CI with OpenMP Phabricator reviews (talking with Louis Dionne)


  * LLVMdev '21: Pre-Commit CI in LLVM: A Case Study of Libc++ - Louis Dionne


  * [https://www.youtube.com/watch?v=kP8CPwaDm_U&t=1h40m15s](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkP8CPwaDm_U%26t%3D1h40m15s&sa=D&source=editors&ust=1778600246429048&usg=AOvVaw1H8POlUfmWoJyrpY_5-b4Y)
  * [https://buildkite.com/llvm-project](https://www.google.com/url?q=https://buildkite.com/llvm-project&sa=D&source=editors&ust=1778600246429162&usg=AOvVaw2bv-e8PFpsI9v95A_HOSHD)


  * 12/15 status update:


  * Louis created a buildkite OpenMP "team" and invited Johannes & Michael Kruse
  * Mikhail Goncharov ([goncharov@google.com](mailto:goncharov@google.com)), who set up the BuildKite ⇔ Phabricator integration, now working with Michael Kruse on setting up builds & agents with GPUs: [https://github.com/google/llvm-premerge-checks/issues/368](https://www.google.com/url?q=https://github.com/google/llvm-premerge-checks/issues/368&sa=D&source=editors&ust=1778600246429614&usg=AOvVaw0CmqrGM9DAHZBgB8sHOScB)


  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246429784&usg=AOvVaw2zH03zdZGJmI_EN361d4H0)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246430282&usg=AOvVaw1wo0cXlTdoAC5V5fzdOV3q) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246430391&usg=AOvVaw3F-25Hvyq8hFRDoacBDNZ7) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246430547&usg=AOvVaw3DbqoE-GOn-o4UxYjSDxOb)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * [openmp-offload-cuda-project](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/11&sa=D&source=editors&ust=1778600246430842&usg=AOvVaw0POXWCm7y7xDTLKrPNrjCc)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/13&sa=D&source=editors&ust=1778600246430940&usg=AOvVaw3tjvvAm9BEV5B6dSlO1BiY)


  * Stopped running omptarget tests since https://reviews.llvm.org/D113253


  * [openmp-offload-cuda-singletarget](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/2/builds/37&sa=D&source=editors&ust=1778600246431174&usg=AOvVaw2wpxg7Q3DPVOjWrui7coR7)
  * [openmp-offload-cuda-irbuilder](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/5&sa=D&source=editors&ust=1778600246431269&usg=AOvVaw0XrRYWjjCjLIVJfPoohJ13)


  * Don't clean source dir


  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246431402&usg=AOvVaw0mJmkPeNYLg9UzMsNH7loS)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246431476&usg=AOvVaw1P6M1ThkQs_k_nLZMsJ3us); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246431536&usg=AOvVaw12UTNllg9mpkpDueRuhJ7Z) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda-newRTL::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246431825&usg=AOvVaw3jJXaYD4WRJ5jKh0G6oXQZ) (under review)


  * Compile failure


  * FAILED: projects/openmp/libomptarget/plugins/amdgpu/CMakeFiles/omptarget.rtl.amdgpu.dir/impl/impl.cpp.o
  * Possible cause: [https://reviews.llvm.org/D115279](https://www.google.com/url?q=https://reviews.llvm.org/D115279&sa=D&source=editors&ust=1778600246432116&usg=AOvVaw3Z33Vj7kFwhJJ_MI_zpG9H) <\- fixed? Added missing functions to dynamic_hsa


  * OMPT target support


  * AMD upstreaming JMC's implementation of the callback interface. Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246432411&usg=AOvVaw3IhFhEzPT_-454JNdm3XWq)
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246432627&usg=AOvVaw0PFkkApzVH4VcJdJBtuL-0) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246432784&usg=AOvVaw3mIKUEa_dIzn-0Jj7bX6Q1) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246432918&usg=AOvVaw177dlcDgXaROa7dnmHLrMM) Based on D99803


  * Device tracing (or trace records) implementation will come separately (review not yet posted)
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246433156&usg=AOvVaw38p_Dbb5H3QX-DlNF2AfSM)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246433310&usg=AOvVaw1kA5Vh7rcFYY-LCgup2nov) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246433652&usg=AOvVaw2CnnZiZRirSxwYcOTAt78n)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246434065&usg=AOvVaw1UM1iSRxF7HPxFxEuvWejv). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246434241&usg=AOvVaw11PlKw-YCqiyicgHBfVkn_)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246434510&usg=AOvVaw1SyOsaSfuExu2fpvSQKfW1)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246434754&usg=AOvVaw04xASJUm57OPEPabbc6c4A)


  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



###
