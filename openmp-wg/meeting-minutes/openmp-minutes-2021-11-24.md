### 2021, Nov 24

### Agenda 

  * Default to openmp-version 5.1
  * Offloading driver discussion: [OpenMP Offloading Driver Implementation](https://www.google.com/url?q=https://docs.google.com/presentation/d/1HCgOUsNcRVCd7MYBBTBgw4qACjWYjgsXkP1NMZcbSHI/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246449206&usg=AOvVaw3BLxljxhw8xPKC0N3ANnZO)
  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246449396&usg=AOvVaw1QrnOBs8j6D77OprmQLOoG)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * OvO (-O3, new RT) passes 100% C/C++ tests now on A100 (sm_80) :) 


  * Ye: still fails in A40 and RTX3060 Ti. 100% pass as well. sm_86 cards but works as sm_80.


  * LLVM change committed before the weekend (11/5) caused tests to hang when dispatching to the GPU:


  * [https://reviews.llvm.org/D105169](https://www.google.com/url?q=https://reviews.llvm.org/D105169&sa=D&source=editors&ust=1778600246450097&usg=AOvVaw2_Au9HBfWx2rIRdpBue3p5)



[Clang/Test]: Rename enable_noundef_analysis to disable-noundef-analysis and turn it off by default

  * hang went away if the test was compiled with: -mllvm -openmp-opt-disable-internalization=1
  * change was later (11/8) reverted here: fd9b099906c61e46574d1ea2d99b973321fe1d21
  * required also rebuilding the OpenMP runtime libraries (just rebuilding clang was not sufficient)
  * presentation on this change: [https://llvm.org/devmtg/2020-09/slides/Lee-UndefPoison.pdf](https://www.google.com/url?q=https://llvm.org/devmtg/2020-09/slides/Lee-UndefPoison.pdf&sa=D&source=editors&ust=1778600246450639&usg=AOvVaw0ZgQcctGLmSYQ8-1gbkcMX)
  * likely still some optimization in llvm not correctly handing poison/freeze that was affecting OpenMP


  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old device rtl (Dan has further info


  * [https://bugs.llvm.org/show_bug.cgi?id=52169](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D52169&sa=D&source=editors&ust=1778600246450981&usg=AOvVaw0rXvWhXAkzEgZvJYBdnQ6l)   
[OpenMP] Wrong answers with nested 'omp parallel for'


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246451222&usg=AOvVaw0ZHP2GTmQgpDfPEz9luKkX) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246451323&usg=AOvVaw1TtsGc66M1xO2FXGH8vepI) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246451446&usg=AOvVaw386sLSJjhb7ZGMhG-J_2Tb)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * [openmp-offload-cuda-project](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/11&sa=D&source=editors&ust=1778600246451776&usg=AOvVaw27MyH5G8GjddsDg5B0Qnef)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/13&sa=D&source=editors&ust=1778600246451867&usg=AOvVaw1i81D-3dj5Ua5zGdMmU55o)
  * [openmp-offload-cuda-singletarget](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/2/builds/37&sa=D&source=editors&ust=1778600246451969&usg=AOvVaw1cpqEnTschPiiF2pCgFlol)
  * [openmp-offload-cuda-irbuilder](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/5&sa=D&source=editors&ust=1778600246452059&usg=AOvVaw1HkTVXEQfqX43bYNLP-DzW)


  * Don't clean source dir


  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246452220&usg=AOvVaw0URYtorld3j1UI7axTa-rc)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246452300&usg=AOvVaw1_6kECC9iJBeQTvHLQhKJ_); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246452355&usg=AOvVaw3OB-FnGHvTy4USoQx0anWn) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda-newRTL::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246452642&usg=AOvVaw1I5tPD29PFI9HfOgBLapsj) (under review)


  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246452798&usg=AOvVaw38e32phQGShzG5i-YRqWwx), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246452876&usg=AOvVaw2-GKxRAIVNy0Qc6Wn1omHe))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation of the callback interface


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246453127&usg=AOvVaw31F-8BOy9Nv03yzrBNERWF) reverted
  * [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246453284&usg=AOvVaw1Nzt50v2hqSaCMGrkslW-8) needs review


  * Device tracing (or trace records) implementation will come separately
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246453524&usg=AOvVaw2ufDyV49KfqeGiilxIXfnA)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246453678&usg=AOvVaw1XbhjgmO_rA_fox9ZRdZZO) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246454029&usg=AOvVaw3K11-jTlRJnt5rjEvUpZQ1)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246454460&usg=AOvVaw3IprFQNHz0vZP_Z2x8Wa0Q). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246454629&usg=AOvVaw23bd4wOvcBb1S1ARGP8Vmz)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246454924&usg=AOvVaw2d7T9Er4Zu_iJrV8HoW43M)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246455137&usg=AOvVaw3K1MNi5QctxHywM4tSlAp_)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246455272&usg=AOvVaw0JJvMAXG0DL75uMWe-PirX)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?
