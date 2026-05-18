### 2021, July 7th

### Agenda

  * Elf cleanup in libomptarget 
  * Offloading buildbot https://lab.llvm.org/staging/#/workers/118


  * https://llvm.org/PR50739 (Race condition in bug49334.cpp)


  * [https://reviews.llvm.org/D104382](https://www.google.com/url?q=https://reviews.llvm.org/D104382&sa=D&source=editors&ust=1778600246539175&usg=AOvVaw2ZWU9Le-d1rVQHKsZh6-hV) (committed)
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246539341&usg=AOvVaw2kIsHDW6MvBD16MOTU6HVC)
  * [https://reviews.llvm.org/D104555](https://www.google.com/url?q=https://reviews.llvm.org/D104555&sa=D&source=editors&ust=1778600246539429&usg=AOvVaw0bjdGFOVg13Bot2a5YERsP) (potentially can also fix for host offloading)
  * https://bugs.llvm.org/show_bug.cgi?id=50737 (probably fixed by https://reviews.llvm.org/D105308)


  * Device event mechanism: https://reviews.llvm.org/D81989


  * Device specific archive library


  * Llvm-link archive support? [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246539822&usg=AOvVaw2IZgvXgWJhWHoJKF3aUQGq) (merged)
  * Unbundling of device specific archive from fat archive [https://reviews.llvm.org/D93525](https://www.google.com/url?q=https://reviews.llvm.org/D93525&sa=D&source=editors&ust=1778600246539977&usg=AOvVaw0k-Kxb0ofrH1AOWUQP0dFC) (merged)
  * [Clang][OpenMP] Add support for Static Device Libraries [https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246540130&usg=AOvVaw3A5QsyOFEoMKKlIwJcTYA5) (under review)
  * Clang driver support 


  * Device runtime specialization
  * Removing TSan annotations from libomp ([https://reviews.llvm.org/D103767](https://www.google.com/url?q=https://reviews.llvm.org/D103767&sa=D&source=editors&ust=1778600246540351&usg=AOvVaw36ALt-5djC-77gXP5k5oIK))
  * New plugins


  * Remote with UCX
  * VGPU



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=50640](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50640&sa=D&source=editors&ust=1778600246540592&usg=AOvVaw1pxie39iP-YN12YYrzyKks)
  * [https://bugs.llvm.org/show_bug.cgi?id=50619](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50619&sa=D&source=editors&ust=1778600246540700&usg=AOvVaw1DZKO8ja1Rlq3HZH5H-Il1)



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Jon Chesterfield (AMD)
  * George Rokos (Intel)
  * Saiyedul Islam (AMD)
  * Raghu Maddhipatla (AMD)
