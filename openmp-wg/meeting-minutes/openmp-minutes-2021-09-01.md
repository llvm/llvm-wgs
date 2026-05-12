### 2021, Sept 1st

### Agenda

  * 13.0.0 release schedule



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Wish to serve ~ 5 contradictory use cases


  * Linux desktop, llvm installed from package manager, possible new user
  * HPC user, trunk installed locally / built from source, sysadmin/vendor/module systems compromising LD_LIBRARY_PATH, need to stop trunk using pieces from elsewhere
  * LLVM developer. Lots of builds on disk, need flexibility, predictability of component choice
  * Vendor toolchain, will use bits of trunk if they can and otherwise do their own thing
  * Whoever I haven't thought of


  * Currently 1, 2 don't work. 3 is ok but easy to accidentally mix up builds. 4 are getting by.
  * Propose:


  * Use a devicertl from clang tree unless command line argument otherwise. Drop LIBRARY_PATH override. Statically linked so clang flag works well to override. Better reliability across the board, devs can still splice in other bitcode (D109057, D109061)
  * Set runpath on everything. Libomptarget, plugins, user applications. LD_LIBRARY_PATH still wins out, but makes 1/ work out of the box and 3/ much less confusing 
  * Add static link options for plugins, libomptarget, libomp. Lets 3, 4 build applications that will always reliably pick up the intended components. Can't override components at all, for that use dynamic linking


  * Preferably do 1 & 2 before the 13 release. 3 can be slower as the main use cases are for bleeding edge / vendor builds and it may take a while to shake out the bugs it finds
  * May want an escape hatch for developers who have a flow that isn't considered above and systems that don't have runpath (which might be detectable by cmake)


  * Static library linking ([https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246496469&usg=AOvVaw3zG57lqYXC2ZkMNyEltn7w), going to update soon)) ?


  * [clang-nvlink-wrapper] Wrapper around nvlink for archive files ([https://reviews.llvm.org/D108291](https://www.google.com/url?q=https://reviews.llvm.org/D108291&sa=D&source=editors&ust=1778600246496681&usg=AOvVaw30GidnjlIOnRvrQhntnOJv) merged)
  * [clang-offload-bundler] Make Bundle Entry ID backward compatible ([https://reviews.llvm.org/D106809](https://www.google.com/url?q=https://reviews.llvm.org/D106809&sa=D&source=editors&ust=1778600246496858&usg=AOvVaw1dxbG6B4UHRiLdyFbMZWgl))


  * required for downstream amdgpu compatibility
  * Should it be pulled in with changes to D105191 so that there is one patch less for the release manager to pull in for llvm-13?


  * NVPTX buildbots (no update)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246497432&usg=AOvVaw37s115wiqLc-DCZ2KBj7Ws) (don't clean source dir)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246497541&usg=AOvVaw1QNEMSj2BGsvvMMeqGPb3E); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246497596&usg=AOvVaw1Ydwdfpoy5l1hF9s004ZCy) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246497817&usg=AOvVaw0JTYUB7BJoOwB1l1uZO7D9) (under review)


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246497912&usg=AOvVaw2PShAd2cc76riHcvKuryHH) [FLAKY] (wrong result)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246498190&usg=AOvVaw36DyLVxc47Um_A9fTLwNpx), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246498264&usg=AOvVaw3f__EZ6Llldo-fdkyi4ZF2))
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246498411&usg=AOvVaw3lS_wd9ro7Mpwy7110pfX2) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246498738&usg=AOvVaw2mvjUzUgoFCyOUOrRNPjFs)


  * pre-merge bot failing with libarcher failures: [https://reviews.llvm.org/D105811  ](https://www.google.com/url?q=https://reviews.llvm.org/D105811&sa=D&source=editors&ust=1778600246498887&usg=AOvVaw30kvYVZflP8op1ZUc7e8ho)[https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246498994&usg=AOvVaw0j9eT2AU65OD9gsPTiQEvI)
  * Fixed by D106855


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246499317&usg=AOvVaw31nmfpYLiisKlLJXOBcQQ6)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246499535&usg=AOvVaw14fP-oNYTgErrtA_yzcDaz)


  * Any update on CUDA issues with ELF notes?



### Open Bugs

### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Jon Chesterfield (AMD)
  * George Rokos (Intel)
  * Johannes Doerfert (ANL)
  * Saiyedul Islam (AMD)
