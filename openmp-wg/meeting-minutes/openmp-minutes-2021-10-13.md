### 2021, Oct 13

### Agenda 

  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old devicertl (Dan has further info)
  * Promoting amdgpu staging buildbots to main lab (i.e. get emails when they break (further, some tests still disabled))


  * [https://lab.llvm.org/staging/#/builders/182](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/182&sa=D&source=editors&ust=1778600246474636&usg=AOvVaw0DodZgfIj4CMiR11UUcoPD)
  * [https://lab.llvm.org/staging/#/builders/183](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/183&sa=D&source=editors&ust=1778600246474741&usg=AOvVaw1XPJBYJDBOK7dAUdZhF3Fd)


  * New device runtime will become default soon
  * NVPTX buildbots (no update since last week)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246475178&usg=AOvVaw0cQWyOXQBxBAolWDhZ6T5Q) (don't clean source dir)
  * Only run supported SOLLVE V&V tests: [D110047](https://www.google.com/url?q=https://reviews.llvm.org/D110047&sa=D&source=editors&ust=1778600246475307&usg=AOvVaw3mFaEZ-ziQEoI2zmm-Ru43)


  * Fixed search for nvlink executable: https://reviews.llvm.org/D111488 [landed]
  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246475471&usg=AOvVaw3Rw52oWagJPz9Vvol729mX); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246475529&usg=AOvVaw325DuVJjjB_Wfb0CgDWizZ) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246475738&usg=AOvVaw02dsJTZJTTh8KK9oE6P-N1) (under review)



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246475919&usg=AOvVaw3d-37OK9KCx80a34kYFcLu), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246475999&usg=AOvVaw0FdFVXtF5qq4Tm6KIeosEi))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246476220&usg=AOvVaw3-rzE9wSuRONEHkT4ZRBQL)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246476372&usg=AOvVaw0TgCKirxn-o0FrN_rWj32E) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246476718&usg=AOvVaw150M280acntGwT_bi2uPc-)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246477260&usg=AOvVaw2f9IwcdNZ_Z87Q3PdIiEqL)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246477478&usg=AOvVaw2NLIq8tDAoJHd8JgBkcu9r)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246477605&usg=AOvVaw03-mDwG3R4SRUT9OhxXP2q)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246477753&usg=AOvVaw1vyJlwlPXdLl8nAY9kESbe)



### Patches to look at

###
