### 2021, Oct 20

### Agenda 

  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old devicertl (Dan has further info


  * [https://bugs.llvm.org/show_bug.cgi?id=52169](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D52169&sa=D&source=editors&ust=1778600246470161&usg=AOvVaw37j0tkfWovQl1ERvKnFRLM)   
[OpenMP] Wrong answers with nested 'omp parallel for'


  * New device runtime will become default soon


  * Partially tested on amdgpu, some patches in progress to bring that online


  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246470458&usg=AOvVaw3sDJW48YaZxLi1DxgsXBps)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots (no update since last week)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246470945&usg=AOvVaw3xwni-9r4HK9SBjAoOI3ZX) (don't clean source dir)
  * Only run supported SOLLVE V&V tests: [D110047](https://www.google.com/url?q=https://reviews.llvm.org/D110047&sa=D&source=editors&ust=1778600246471075&usg=AOvVaw1Ta53cbxmgbR14cws56CRc)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246471152&usg=AOvVaw3ydIFvZJs9R1B58LF7-65u); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246471215&usg=AOvVaw2iQr-MPzmTQAlWh5ZrgHYq) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246471440&usg=AOvVaw2Pivdt3_s3_dSZhEGOAc94) (under review)



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246471595&usg=AOvVaw26JbZG1skFUmamxErp7k1I), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246471668&usg=AOvVaw0t4qkgE0KHFbSM2nmF73NF))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246471874&usg=AOvVaw0dGPl4m91UdF9MtrGvrowI)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246472016&usg=AOvVaw0rB1-2HBLKckvSTf-hewFl) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246472382&usg=AOvVaw3kAekSu0gSvIDv2cIudJWv)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246472784&usg=AOvVaw222ML6IWf85rz-bo1nxJPr). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246472956&usg=AOvVaw3DX0RRK61Su9InDHVZ4iPT)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246473255&usg=AOvVaw0QzXoe4n5AeNyhpmpodNB6)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246473461&usg=AOvVaw3xyrxnwSrclLo7q6qze5MR)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246473619&usg=AOvVaw2HPtC99Ahadr67FivmU3m_)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246474150&usg=AOvVaw1yO6HCBmzgMZB_fz-0499Z)
