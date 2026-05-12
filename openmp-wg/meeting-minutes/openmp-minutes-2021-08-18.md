### 2021, August 18th

### Agenda

  * 13.0.0 release schedule



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * Openmp buildbot [https://lab.llvm.org/buildbot/#/builders/84](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/84&sa=D&source=editors&ust=1778600246506091&usg=AOvVaw3WMn3ScsOinZsFGy-Dr8nw) has been dead for 3 days, can't check out source. Guesses?
  * CMake for Ubuntu Offloading


  * I.e. build it by default, may require freestanding (removing printf?)


  * Re: static libraries, --whole-archive mode
  * Static library linking ([https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246506476&usg=AOvVaw1aivhFySrKTndr4-X8k_DI), will be updated once D108291 lands)) ?


  * [clang-nvlink-wrapper] Wrapper around nvlink for archive files ([https://reviews.llvm.org/D108291](https://www.google.com/url?q=https://reviews.llvm.org/D108291&sa=D&source=editors&ust=1778600246506669&usg=AOvVaw1RrsKOcAd0WA12bf7eqaGy) up for review)
  * [clang-offload-bundler] Make Bundle Entry ID backward compatible ([https://reviews.llvm.org/D106809](https://www.google.com/url?q=https://reviews.llvm.org/D106809&sa=D&source=editors&ust=1778600246506830&usg=AOvVaw3MXgZxOepRXGPbOMJmdhkR))


  * required for downstream amdgpu compatibility
  * Should it be pulled in with changes to D105191 so that there is one patch less for the release manager to pull in for llvm-13?



  * Enable map checks in USM mode in libomptarget
  * Omt taskwait depend https://bugs.llvm.org/show_bug.cgi?id=46196
  * Offloading buildbot(s)


  * NVPTX and AMDGPU both fail on:


  * FAIL: libomptarget :: x86_64-pc-linux-gnu::bug49334.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::memory_manager.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::parallel_offloading_map.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::taskloop_offload_nowait.cpp


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246507917&usg=AOvVaw3jkd-pryKg5dFg4ClZGYbT) (don't clean source dir)


  * AMDGPU running here: [https://lab.llvm.org/staging/#/builders/182/](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/182/&sa=D&source=editors&ust=1778600246508071&usg=AOvVaw3bLwtLTKe7RHNfmu4_ipty)
  * FAIL: libomptarget :: amdgcn-amd-amdhsa::bug50022.cpp
  * FAIL: libomptarget :: amdgcn-amd-amdhsa::bug49021.cpp  
        
  * [llvm.org/PR51517](https://www.google.com/url?q=http://llvm.org/PR51517&sa=D&source=editors&ust=1778600246508297&usg=AOvVaw1BhmiiFD_Ym_3RAf8S3x2S) [NEW] (invalid CUDA kernel image)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::lambda_mapping.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49021.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49779.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::declare_mapper_nested_default_mappers_complex_structure.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::target_array_extension.c
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug47654.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::target_pointers_members_map.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::declare_mapper_target_update.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::declare_mapper_target.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::target_data_array_extension_at_exit.c
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::declare_mapper_nested_default_mappers.cpp
  * FAIL: libomptarget :: nvptx64-nvidia-cuda::parallel_offloading_map.cpp


  * [llvm.org/PR51518](https://www.google.com/url?q=http://llvm.org/PR51518&sa=D&source=editors&ust=1778600246509435&usg=AOvVaw10WXtTXZKDZQwyuHu_iqVI) [NEW] [FLAKY] (bin/opt missing in runtimes build)


  * Performing build step for 'runtimes'
  * There's a diff associated with this that added opt dependency to one of the plugins


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246509735&usg=AOvVaw3fACf486woyqkKgUHQdpca); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246509792&usg=AOvVaw1kR4kVyrst6jKVOH9gK4aU) [FLAKY]


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246510048&usg=AOvVaw1TFmpwFPjxSotXFO_gHpoi) (under review)


  * [llvm.org/PR50738](https://www.google.com/url?q=http://llvm.org/PR50738&sa=D&source=editors&ust=1778600246510146&usg=AOvVaw3oxx7XBfaJZxJ-ofCCb3ps); [llvm.org/PR51150](https://www.google.com/url?q=http://llvm.org/PR51150&sa=D&source=editors&ust=1778600246510209&usg=AOvVaw0-wU-5aJzQ73c889QaVeMe)


  * FAIL: libomptarget :: x86_64-pc-linux-gnu::memory_manager.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::parallel_offloading_map.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::taskloop_offload_nowait.cpp


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246510563&usg=AOvVaw3hiJjLPNU9Sl6MUnx5wPzR) [FLAKY]


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246510804&usg=AOvVaw2QcCZO21bkY2EvCp4ksACf), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246510878&usg=AOvVaw0hqFETsdc3Y8wWGXDnKvH-) )
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246511022&usg=AOvVaw1W0DXQ9jPp68EThZBShcXQ) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply
  * https://bugs.llvm.org/show_bug.cgi?id=51117 


  * pre-merge bot failing with libarcher failures: https://reviews.llvm.org/D105811  [https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246511504&usg=AOvVaw1xynsQBl_ddrEMEQCxWNtZ)
  * Fixed by D106855


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246511817&usg=AOvVaw2R9oT4brZx4HjGkhUYMqAO)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload archicture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246512022&usg=AOvVaw3TCkpollG2AZs92K_s57Uq)


  * Rpath, runpath, env vars and fragility of toolchains when more than one are on disk



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49787](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49787&sa=D&source=editors&ust=1778600246512314&usg=AOvVaw2Ce2wOQE7R8L_wMo9AMtN8) compiler/runtime API mismatch for async mapping
  * [https://bugs.llvm.org/show_bug.cgi?id=50336](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50336&sa=D&source=editors&ust=1778600246512467&usg=AOvVaw3FkMDrpJZw3nKbaleP5IiH) (Should be fixed in [https://reviews.llvm.org/D107668](https://www.google.com/url?q=https://reviews.llvm.org/D107668&sa=D&source=editors&ust=1778600246512556&usg=AOvVaw2BzcGuL5Ke5zzAzh1mhSUM))



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * George Rokos (Intel)
  * Ravi Narayanaswamy (Intel)
  * Jon Chesterfield (AMD)
