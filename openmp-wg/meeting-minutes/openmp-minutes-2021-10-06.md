### 2021, Oct 6

### Agenda 

  * Promoting amdgpu staging buildbots to main lab (i.e. get emails when they break (further, some tests still disabled))


  * [https://lab.llvm.org/staging/#/builders/182](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/182&sa=D&source=editors&ust=1778600246478204&usg=AOvVaw33DHCCn64zDIzEkzDCQUKY)
  * [https://lab.llvm.org/staging/#/builders/183](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/183&sa=D&source=editors&ust=1778600246478315&usg=AOvVaw3fzEmpoGL0Al98SkWKCLs9)


  * New meeting link on the openmp-dev list
  * New device runtime becomes default now
  * NVPTX buildbots (no update since last week)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246478883&usg=AOvVaw0aJSmkGqz10Wgr9n9oGQhp) (don't clean source dir)
  * Only run supported SOLLVE V&V tests: [D110047](https://www.google.com/url?q=https://reviews.llvm.org/D110047&sa=D&source=editors&ust=1778600246479020&usg=AOvVaw0d9FczHl9DnzkFM2df1Lfz)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246479099&usg=AOvVaw3zLxh0K9FikdmjPUop6Ypy); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246479166&usg=AOvVaw1MJkmYK-PVZxzPGWgWv1ie) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246479388&usg=AOvVaw2Dpsx72aPqCRmDwxUr_4Ed) (under review)



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246479534&usg=AOvVaw2AKefqVZsf66foxOgiZRss), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246479604&usg=AOvVaw1zhol5T7hYwoKjqcslcezE))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246479835&usg=AOvVaw3-9spZuvau8BgIADh09T-p) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246480186&usg=AOvVaw0ONNvw1PnrMJwHYKp-B3ij)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Static library linking ([https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246480445&usg=AOvVaw1GaAwmbfRH1fF5BIv-1g6A), waiting for review))
  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246481232&usg=AOvVaw1eXfl1AIR8jqKAvcCW5JnT)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246481466&usg=AOvVaw3UT7JrxoIrgpV-ZQwichAo)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246481596&usg=AOvVaw3dqqZV9IOx6frfpLP42ZcV)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246481765&usg=AOvVaw2YpQaEGWwQEg_7Wj8jGFpc)



### Patches to look at
