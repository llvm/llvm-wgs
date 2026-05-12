### 2021, Dec 1

### Agenda

  * Driver details by Greg Rodgers
  * Default to openmp-version 5.1 (Saiyedul will review experience on switch to 5.0 default)


  * AMD propose that default change in LLVM 15 (after fork) and LLVM 14 default is 5.0


  * Offloading driver discussion: [OpenMP Offloading Driver Implementation](https://www.google.com/url?q=https://docs.google.com/presentation/d/1HCgOUsNcRVCd7MYBBTBgw4qACjWYjgsXkP1NMZcbSHI/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246442184&usg=AOvVaw0ddSAk4gq68tEfhfdKumMT)


  * Greg has some additional charts


  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246442414&usg=AOvVaw17BuN5xcPOtiSZghHMaQwz)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * OvO (-O3, new RT) passes 100% C/C++ tests now on A100 (sm_80) :) 


  * Ye: still fails in A40 and RTX3060 Ti. 100% pass as well. sm_86 cards but works as sm_80.


  * LLVM change committed before the weekend (11/5) caused tests to hang when dispatching to the GPU:


  * [https://reviews.llvm.org/D105169](https://www.google.com/url?q=https://reviews.llvm.org/D105169&sa=D&source=editors&ust=1778600246443166&usg=AOvVaw0oNw9eq2bHZJfe8WaOFYQ9)



[Clang/Test]: Rename enable_noundef_analysis to disable-noundef-analysis and turn it off by default

  * hang went away if the test was compiled with: -mllvm -openmp-opt-disable-internalization=1
  * change was later (11/8) reverted here: fd9b099906c61e46574d1ea2d99b973321fe1d21
  * required also rebuilding the OpenMP runtime libraries (just rebuilding clang was not sufficient)
  * presentation on this change: [https://llvm.org/devmtg/2020-09/slides/Lee-UndefPoison.pdf](https://www.google.com/url?q=https://llvm.org/devmtg/2020-09/slides/Lee-UndefPoison.pdf&sa=D&source=editors&ust=1778600246443722&usg=AOvVaw3ivR3JVxK_-0qLeDwLRRpO)
  * likely still some optimization in llvm not correctly handing poison/freeze that was affecting OpenMP


  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old device rtl (Dan has further info


  * [https://bugs.llvm.org/show_bug.cgi?id=52169](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D52169&sa=D&source=editors&ust=1778600246444056&usg=AOvVaw2mLCfJ8CCPdNjqA95d9KIO)   
[OpenMP] Wrong answers with nested 'omp parallel for'


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246444308&usg=AOvVaw1CNY2jHneoQDvecAoK2_Xn) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246444416&usg=AOvVaw00V18HEx5wsbsb1Zhg9Qzp) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246444541&usg=AOvVaw39ltg2Y5p5pR4RPcv-97lt)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * [openmp-offload-cuda-project](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/11&sa=D&source=editors&ust=1778600246444865&usg=AOvVaw2NoJ6UCD5uwKiTZv4C5HEK)
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/13&sa=D&source=editors&ust=1778600246444964&usg=AOvVaw3dCj6s4tLzf0zej6iU-wZI)
  * [openmp-offload-cuda-singletarget](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/2/builds/37&sa=D&source=editors&ust=1778600246445057&usg=AOvVaw3MdN9votHDKjiuirIUzQUn)
  * [openmp-offload-cuda-irbuilder](https://www.google.com/url?q=http://meinersbur.de:8011/%23/builders/5&sa=D&source=editors&ust=1778600246445165&usg=AOvVaw3KsUWAIp-PFlkEQiV-slCe)


  * Don't clean source dir


  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246445331&usg=AOvVaw1npNHdzEs44ih-L69oubq1)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246445415&usg=AOvVaw0opAMiJd5EsTQz82UdSbws); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246445472&usg=AOvVaw39bZjBiYnL-hjqxBpiOx1I) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda-newRTL::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246445750&usg=AOvVaw0Zn0mJ-SaTtZWquBwrEvOC) (under review)


  * OMPT target support


  * AMD upstreaming JMC's implementation of the callback interface. Needs review [⚙ D113728 [libomptarget] [amdgpu] Foundation for OMPT target callback support (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D113728&sa=D&source=editors&ust=1778600246446019&usg=AOvVaw3OuLt2v7YAbaUUF-8ixncJ)
  * Possibly revert the 2-3 patches based on an alternative implementation


  * [⚙ D99803 [openmp] Add OMPT initialization in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246446224&usg=AOvVaw2RZgj5Msxp3aZLYEWxisTJ) reverted
  * [⚙ D106975 [openmp] Update OMPT declaration and implementation in the runtime (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246446425&usg=AOvVaw04pk6pEDxH1mfek3lPmyLA) Based on D99803
  * [⚙ D106976 [openmp] Initialize OMPT in libomptarget (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246446558&usg=AOvVaw2FIHQflU5ku-TjRVxz9N7J) Based on D99803


  * Device tracing (or trace records) implementation will come separately (review not yet posted)
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246446801&usg=AOvVaw3aeMn-HPGPho7ufb5bKJNY)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246446948&usg=AOvVaw18d3oqXM07UER_iUDXZwn9) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246447319&usg=AOvVaw2yzwvKStk_4uLNSujPZ_Jr)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246447738&usg=AOvVaw0zx61kUwhbxK4nLap75Hnh). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246447909&usg=AOvVaw0LdR0tozJfX6gR8IyH7Ffz)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246448196&usg=AOvVaw0NdxdsYFqlVLkrAKWSysTc)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246448409&usg=AOvVaw3_Y2GO2RuK4NmUvMI78N3t)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246448534&usg=AOvVaw01CQqVUJ83-BVzHgvvkRQJ)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?
