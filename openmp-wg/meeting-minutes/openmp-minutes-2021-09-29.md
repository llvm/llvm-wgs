### 2021, Sept 29th

### Agenda

  * 13.0.0 release schedule



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * Presentation about task graphs (Georgia Tech)


  * Built on top of [https://github.com/habanero-rice/hclib](https://www.google.com/url?q=https://github.com/habanero-rice/hclib&sa=D&source=editors&ust=1778600246482408&usg=AOvVaw3WKCNgj1lLVsJVOtHqQ6TX) 


  * New meeting link on the openmp-dev list
  * NVPTX buildbots (no update since last week)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246482844&usg=AOvVaw36GHCxOJ5ADyAL6uGgI-1Y) (don't clean source dir)


  * Changes to the top-level 'runtimes' directory (introduced in [D93408](https://www.google.com/url?q=https://reviews.llvm.org/D93408&sa=D&source=editors&ust=1778600246482984&usg=AOvVaw3TgZuvcy9iWi2QT-3mIlMo)) not triggering a build
  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246483087&usg=AOvVaw1O6d3X4uBYxX1vxjxr7YSB); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246483156&usg=AOvVaw0l20pP8N8QagWaC5tthqem) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246483377&usg=AOvVaw3M2BvJNDBw9avxkd-VbSAZ) (under review)


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246483478&usg=AOvVaw2GTR-qJcw2ejwoeZ_OlxuO) [FLAKY] (wrong result)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp


  * Ignore failing SOLLVE V&V tests: [D110047](https://www.google.com/url?q=https://reviews.llvm.org/D110047&sa=D&source=editors&ust=1778600246483717&usg=AOvVaw0DsSzif0O3fG2EvUAIK2dG)



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246483857&usg=AOvVaw1lDFRTAAw5tmeD7ychnsov), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246483938&usg=AOvVaw2nL8CMvbt1pmKXpHx-ikHU))
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246484083&usg=AOvVaw18odzdp33kv6VLQl3ZhYMi) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246484435&usg=AOvVaw25pV0E80TtIBgXzjdb6DIf)


  * pre-merge bot failing with libarcher failures: [https://reviews.llvm.org/D105811  ](https://www.google.com/url?q=https://reviews.llvm.org/D105811&sa=D&source=editors&ust=1778600246484582&usg=AOvVaw2kBEHrGFUiKXnz36B2z72X)[https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246484666&usg=AOvVaw3aatD-VI9EacO0H_BNaTa-)
  * Fixed by D106855


  * Static library linking ([https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246484815&usg=AOvVaw1IJtBkhNSOJPWLBk5hR4Xc), waiting for review))
  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246485233&usg=AOvVaw0p9oeouPYlpSZRQrmpQquw)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246485451&usg=AOvVaw2U4bz9B332W3G2mNSuK3ft)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246485579&usg=AOvVaw0PdXSTcQwSiaJKzOVjz7mo)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246485728&usg=AOvVaw1TS9xEze9Es4z66SYs0xV5)



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * George Rokos (Intel)
  * Jon Chesterfield (AMD)
  * Andrey Churbanov (Intel)
  * Johannes Doerfert (ANL)
  * Saiyedul Islam (AMD)
  * Vivek Sarkar (Georgia Tech)
  * Seonmyeong Bak (NVIDIA, Georgia Tech)



HClib-related information

  * HClib repository: [https://github.com/habanero-rice/hclib](https://www.google.com/url?q=https://github.com/habanero-rice/hclib&sa=D&source=editors&ust=1778600246486416&usg=AOvVaw3qARlHiRGBGCAyBzev-ort) 


  * Basic tutorial on use of HClib APIs (not internal design) can be found [here](https://www.google.com/url?q=https://github.com/habanero-rice/hclib/tree/master/tutorial/hipc18/presentation&sa=D&source=editors&ust=1778600246486564&usg=AOvVaw26Ib6jdqJHMdSR3-tubC9P)
  * As mentioned in the meeting, the main motivation for HClib is to enable efficient event-driven tasking with events that can be used to support task dependences, completion of inter-node/host-device communication requests, etc.


  * Repository for work presented today that uses HClib to enable gang scheduling of OpenMP tasks that perform extra-OpenMP synchronization and communication calls, as in the SLATE library: [https://github.com/sbak5/OMP_SLATE_eval](https://www.google.com/url?q=https://github.com/sbak5/OMP_SLATE_eval&sa=D&source=editors&ust=1778600246487095&usg=AOvVaw3j-ro5eoDp7wSZcG5Gwui-) 
  * Some relevant papers


  * [Task-Graph Scheduling Extensions for Efficient Synchronization and Communication](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3447818.3461616&sa=D&source=editors&ust=1778600246487313&usg=AOvVaw1alqrbn5tqVWu6WmA24ulS). Seonmyeong Bak, Oscar Hernandez, Mark Gates, Piotr Luszczek, Vivek Sarkar. Proceedings of the 35th ACM International Conference on Supercomputing (ICS), June 2021.
  * [A Pluggable Framework for Composable HPC Scheduling Libraries](https://www.google.com/url?q=https://wiki.rice.edu/confluence/download/attachments/4425835/AsHES-03.pdf?version%3D1%26modificationDate%3D1489773371949%26api%3Dv2&sa=D&source=editors&ust=1778600246487602&usg=AOvVaw1OtU1zrBAes-qpvrtYuu3K). Max Grossman, Vivek Kumar, Nick Vrvilo, Zoran Budimlic, Vivek Sarkar. The Seventh International Workshop on Accelerators and Hybrid Exascale Systems (AsHES). May 2017. [[slides](https://www.google.com/url?q=https://wiki.rice.edu/confluence/download/attachments/4425835/ashes17-slides.pdf?version%3D1%26modificationDate%3D1496614131040%26api%3Dv2&sa=D&source=editors&ust=1778600246487835&usg=AOvVaw2K3FBMvrmdxTSq5xpX_Erf)]
  * [Integrating Asynchronous Task Parallelism with OpenSHMEM](https://www.google.com/url?q=https://wiki.rice.edu/confluence/download/attachments/4425835/asyncshmem1.pdf?version%3D2%26modificationDate%3D1473733904618%26api%3Dv2&sa=D&source=editors&ust=1778600246487988&usg=AOvVaw0S0FFltX-ssepL9XCSpOXt). Max Grossman, Vivek Kumar, Zoran Budimlic, Vivek Sarkar. OpenSHMEM Workshop, August 2016.
  * [HabaneroUPC++: a Compiler-free PGAS Library](https://www.google.com/url?q=https://wiki.rice.edu/confluence/download/attachments/4425835/habaneroupc-pgas14.pdf?version%3D1%26modificationDate%3D1413408225016%26api%3Dv2&sa=D&source=editors&ust=1778600246488207&usg=AOvVaw2ZnqIxM_bROwS5G60xa-OJ). Vivek Kumar, Yili Zheng, Vincent Cave,  Zoran Budimlic, Vivek Sarkar. 8th International Conference on Partitioned Global Address Space Programming Models (PGAS14), October 2014. [[slides](https://www.google.com/url?q=https://wiki.rice.edu/confluence/download/attachments/4425835/habaneroupc-pgas14-slides.pdf?version%3D1%26modificationDate%3D1413408371601%26api%3Dv2&sa=D&source=editors&ust=1778600246488447&usg=AOvVaw2s-U1kwPevKamNGQAsICtp)]



* * *

#
