### 2021, June 16th

### Agenda

  * Offloading buildbot https://lab.llvm.org/staging/#/workers/118 (Michael)


  * https://llvm.org/PR50738 (Assertion failure with result verification)
  * https://llvm.org/PR50739 (Race condition in bug49334.cpp)


  * to make it failing steadily, reduce the size of the matrix (BS = 16; /  N = 256;)
  * https://lab.llvm.org/staging/#/builders/155/builds/444
  * https://lab.llvm.org/staging/#/builders/154/builds/175 (bug49334.cpp)
  * Caused by race condition with asynchronous data movement. Will fix it by attaching an event to each data movement (host->device).


  * https://lab.llvm.org/staging/#/builders/155/builds/263 (api/omp_get_wtime)
  * https://llvm.org/PR50737 (Flaky segfault at test exit)


  * depend.cpp and gtid.cpp should be similar. Both with exit code -11 after result is correctly printed. Will investigate it soon.


  * Device specific archive library


  * Llvm-link archive support? [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246546070&usg=AOvVaw0bpaGZ2eByjiUWvEBzntss) (merged)
  * Unbundling of device specific archive from fat archive [https://reviews.llvm.org/D93525](https://www.google.com/url?q=https://reviews.llvm.org/D93525&sa=D&source=editors&ust=1778600246546220&usg=AOvVaw30_pSVuFtcnd6FitlgHGu9) (under review)


  * Implementation of serialized parallel regions in OpenMP vs. OMPT
  * Globalization update



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=50640](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50640&sa=D&source=editors&ust=1778600246546490&usg=AOvVaw2T_czGMnucyLytDGSBJvNh)
  * [https://bugs.llvm.org/show_bug.cgi?id=50619](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50619&sa=D&source=editors&ust=1778600246546600&usg=AOvVaw3r92Q67Xbg551XlXqoLnIK)



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * John Mellor-Crummey (Rice)
  * Vladimir Indjic (University of Novi Sad)
  * Andrey Churbanov (Intel)
  * Shilei Tian (SBU)
  * Joseph Huber (ORNL)
  * George Rokos (Intel)
  * Saiyedul Islam (AMD)



###
