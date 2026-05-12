### 2021, July 21st

### Agenda

  * Reminder 13.0.0 release schedule from May 3 email.



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * CMake for Ubuntu Offloading
  * Static library linking?
  * AMDGPU math headers
  * 

  * Elf cleanup in libomptarget 
  * Missing omp end declare target


  * TODO at the end of clang/test/OpenMP/declare_target_messages.cpp 


  * Deadlock :



InitLibrary,->PendingGlobalsMtx.lock 

        exit 

UnRegisterLib,-> PendingGlobalsMtx.lock()  

  * Offloading buildbot failures


  * llvm.org/PR50739 ; llvm.org/PR49940


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246533718&usg=AOvVaw2xRJPw2PKsDVQan-6-6fmh)
  * [https://reviews.llvm.org/D104555](https://www.google.com/url?q=https://reviews.llvm.org/D104555&sa=D&source=editors&ust=1778600246533825&usg=AOvVaw1wMtZFto0EIJgl6wa-MeP-)  
(potentially can also fix for host offloading; PR50738)
  * Device event mechanism: [https://reviews.llvm.org/D81989](https://www.google.com/url?q=https://reviews.llvm.org/D81989&sa=D&source=editors&ust=1778600246534030&usg=AOvVaw08aEiaOjqVdk9QkGu8jzrm) (abandoned?)


  * llvm.org/PR50738


  * FAIL: libomptarget :: x86_64-pc-linux-gnu::memory_manager.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::parallel_offloading_map.cpp
  * (probably related to the issue in bug49335.cpp)


  * llvm.org/PR51065


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49021.cpp
  * [https://reviews.llvm.org/D106341](https://www.google.com/url?q=https://reviews.llvm.org/D106341&sa=D&source=editors&ust=1778600246534514&usg=AOvVaw1GYILRV48mCesir1TSDT8j)


  * NEW: llvm.org/PR51150


  * FAIL: libomptarget :: x86_64-pc-linux-gnu::taskloop_offload_nowait.cpp


  * Rebuilding clang does not cause deviceRTL rebuilt with LLVM_ENABLE_RUNTIMES=openmp build


  * Going to clean build with ccache


  * Device specific archive library


  * Llvm-link archive support? [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246534944&usg=AOvVaw0mTEB9izAggldO8pH5-SGk) (merged)
  * Unbundling of device specific archive from fat archive [https://reviews.llvm.org/D93525](https://www.google.com/url?q=https://reviews.llvm.org/D93525&sa=D&source=editors&ust=1778600246535094&usg=AOvVaw1-H_JaC_U3-0AZpJOnxR2J) (merged)
  * [Clang][OpenMP] Add support for Static Device Libraries [https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246535253&usg=AOvVaw0Fa7MLvTEx_Nd3U2ENKGQ8) (under review)
  * Clang driver support 


  * OMPT for omptarget ([https://reviews.llvm.org/D99803](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246535415&usg=AOvVaw0fd7ElrSngNIDpT6Srfn9k))
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246535553&usg=AOvVaw1-fgKzfZJd091mrfovQnYl) issue with -Wl,-Bsymbolic-functions flag)
  * https://bugs.llvm.org/show_bug.cgi?id=51117 


  * pre-merge bot failing with libarcher failures: https://reviews.llvm.org/D105811  https://reviews.llvm.org/harbormaster/unit/113491/



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49787](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49787&sa=D&source=editors&ust=1778600246535995&usg=AOvVaw2_XBRA7Shoa_RMhvQqMiG7) compiler/runtime API mismatch for async mapping



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Jon Chesterfield (AMD)
  * George Rokos (Intel)
