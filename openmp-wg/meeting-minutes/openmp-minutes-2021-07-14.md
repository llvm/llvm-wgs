### Ravi Narayanaswamy (Intel)2021, July 14th

### Agenda

  * Elf cleanup in libomptarget 
  * Offloading buildbot https://lab.llvm.org/staging/#/workers/118


  * https://llvm.org/PR50739 (Race condition in bug49334.cpp)


  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246536659&usg=AOvVaw2f2UrV1qEVmB0Mg0uMpE-O)
  * [https://reviews.llvm.org/D104555](https://www.google.com/url?q=https://reviews.llvm.org/D104555&sa=D&source=editors&ust=1778600246536752&usg=AOvVaw0oqOIh8ODM4kQyHdgODEJa) (potentially can also fix for host offloading)


  * Device event mechanism: https://reviews.llvm.org/D81989 (abandoned?)
  * Regression: libomptarget :: nvptx64-nvidia-cuda::bug49021.cpp


  * https://lab.llvm.org/staging/#/builders/155/builds/1673
  * https://lab.llvm.org/staging/#/builders/154/builds/1317
  * Caused by D101976 or D101977
  * Related bug report [https://bugs.llvm.org/show_bug.cgi?id=51065](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51065&sa=D&source=editors&ust=1778600246537273&usg=AOvVaw3_Th9U29bzvnLbuvEoNv90)


  * ? https://lab.llvm.org/staging/#/builders/154/builds/1421


  * Device specific archive library


  * Llvm-link archive support? [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246537516&usg=AOvVaw0LkPAe4umvf2iVmhMBTbSf) (merged)
  * Unbundling of device specific archive from fat archive [https://reviews.llvm.org/D93525](https://www.google.com/url?q=https://reviews.llvm.org/D93525&sa=D&source=editors&ust=1778600246537660&usg=AOvVaw2spAvh0N-LMWyv4NgzGFx7) (merged)
  * [Clang][OpenMP] Add support for Static Device Libraries [https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246537816&usg=AOvVaw0ZCItSEo45z6xN3lAUmDcP) (under review)
  * Clang driver support 


  * New plugins


  * Remote with UCX
  * VGPU


  * Mapping issues for new code examples in the OpenMP Examples Document


  * [https://bugs.llvm.org/show_bug.cgi?id=51088](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51088&sa=D&source=editors&ust=1778600246538159&usg=AOvVaw19xOYdGz1BYYj5vRdii7ow) 
  * [https://bugs.llvm.org/show_bug.cgi?id=51089](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51089&sa=D&source=editors&ust=1778600246538277&usg=AOvVaw1M6zp9c5zL1wb0ZifaoKFD)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49787](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49787&sa=D&source=editors&ust=1778600246538427&usg=AOvVaw2dx4r-3CpX23WEZRthLFr-) compiler/runtime API mismatch for async mapping



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Jon Chesterfield (AMD)
  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert, Ye Luo (ANL)
  * George Rokos (Intel)
  * Saiyedul Islam (AMD)
