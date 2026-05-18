### 2021, August 4th

### Agenda

  * Reminder 13.0.0 release schedule from May 3 email.



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * CMake for Ubuntu Offloading
  * Static library linking?


  * Fixed some issues with amdgpu. Working for nvlink issue: https://reviews.llvm.org/D105191


  * AMDGPU math headers


  * Offloading buildbot(s)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246520735&usg=AOvVaw0HDOl5pLqTT1yGQYqkLNww) (don't clean source dir)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246520843&usg=AOvVaw1WFY88zZZZ4AYXrtvGHUhp); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246520902&usg=AOvVaw0IIeKfOjLMGro-GTt2Dzu0) [FLAKY]


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246521181&usg=AOvVaw2-QuyZfSASg45cgvlkqEOM) (under review)


  * [llvm.org/PR50738](https://www.google.com/url?q=http://llvm.org/PR50738&sa=D&source=editors&ust=1778600246521288&usg=AOvVaw1iB8GydlXjP8ltKuFlCpkK); [llvm.org/PR51150](https://www.google.com/url?q=http://llvm.org/PR51150&sa=D&source=editors&ust=1778600246521344&usg=AOvVaw1m0Vbh5VVhnZyQwUl5w3XO)


  * FAIL: libomptarget :: x86_64-pc-linux-gnu::memory_manager.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::parallel_offloading_map.cpp
  * FAIL: libomptarget :: x86_64-pc-linux-gnu::taskloop_offload_nowait.cpp


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246521687&usg=AOvVaw2-0tqbJng589PKO4jagVt7) [FLAKY]


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp![](images/image1.png)


  * [llvm.org/PR51235](https://www.google.com/url?q=http://llvm.org/PR51235&sa=D&source=editors&ust=1778600246522445&usg=AOvVaw3u4XJhsHnWhQmO8An6goOu) [FLAKY]


  * https://reviews.llvm.org/D107195 [10s timeouts]
  * TIMEOUT: libomp::omp_get_wtime.c
  * TIMEOUT: libomp::omp_taskwait.c
  * TIMEOUT: libomp::omp_task_if.c
  * TIMEOUT: libomp::omp_task_final.c
  * TIMEOUT: libomp::omp_flush.c
  * TIMEOUT: libomp::omp_task.c
  * TIMEOUT: libomp::omp_taskyield.c
  * TIMEOUT: libomp::depend.cpp
  * TIMEOUT: libomp::gtid.cpp
  * [https://reviews.llvm.org/D107121](https://www.google.com/url?q=https://reviews.llvm.org/D107121&sa=D&source=editors&ust=1778600246523165&usg=AOvVaw1TW4GSlnX0EPOhVEXaOBfK) (Under review)


  * [llvm.org/PR51337](https://www.google.com/url?q=http://llvm.org/PR51337&sa=D&source=editors&ust=1778600246523267&usg=AOvVaw1ygeeFsz3Y7zoyuDa95baz) [NEW] (Could be issue with declare variant support)


  *  libomptarget :: nvptx64-nvidia-cuda :: api/omp_device_managed_memory.c
  *  libomptarget :: nvptx64-nvidia-cuda :: api/omp_get_num_devices.c
  *  libomptarget :: nvptx64-nvidia-cuda :: api/omp_get_num_devices_with_empty_target.c
  *  libomptarget :: nvptx64-nvidia-cuda :: api/omp_host_pinned_memory.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/data_absent_at_exit.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/delete_inf_refcount.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/pr38704.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_array_extension.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_data.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_data_array_extension.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_data_at_exit.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_enter_data.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_exit_data_delete.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_exit_data_release.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_update.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/target_update_array_extension.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/zero_length_array_section.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/present/zero_length_array_section_exit.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/private_mapping.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/ptr_and_obj_motion.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/target_data_array_extension_at_exit.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/target_implicit_partial_map.c
  *  libomptarget :: nvptx64-nvidia-cuda :: mapping/target_update_array_extension.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/bug49334.cpp
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/d2d_memcpy.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/dynamic_module.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/dynamic_module_load.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/host_as_target.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/info.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/lone_target_exit_data.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/mandatory_but_no_devices.c
  *  libomptarget :: nvptx64-nvidia-cuda :: offloading/offloading_success.c


  * [https://reviews.llvm.org/D106928](https://www.google.com/url?q=https://reviews.llvm.org/D106928&sa=D&source=editors&ust=1778600246526183&usg=AOvVaw3NSNzkhNiwfY9xbgCSGNbV) [AMDGPU buildbot]



  * OMPT for omptarget ([https://reviews.llvm.org/D99803](https://www.google.com/url?q=https://reviews.llvm.org/D99803&sa=D&source=editors&ust=1778600246526357&usg=AOvVaw2mvnhyx3yQ6Ux5dQtHAL0L))
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246526499&usg=AOvVaw3Aex8SDtYF_RMecsOdpf1z) issue with -Wl,-Bsymbolic-functions flag)
  * https://bugs.llvm.org/show_bug.cgi?id=51117 


  * pre-merge bot failing with libarcher failures: https://reviews.llvm.org/D105811  [https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246526798&usg=AOvVaw2KLSIf54CV-BjR0yaUl2a8)
  * Fixed by D106855


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246527103&usg=AOvVaw3YfB6yLsMcdqCMRTMEGRud)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload archicture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246527320&usg=AOvVaw0B-OxxixAZdGscDwumWEVa)


  * Rpath, runpath, env vars and fragility of toolchains when more than one are on disk



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49787](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49787&sa=D&source=editors&ust=1778600246527604&usg=AOvVaw0StldTzXdzfpHwB-OsaN5o) compiler/runtime API mismatch for async mapping
  * [https://bugs.llvm.org/show_bug.cgi?id=50336](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50336&sa=D&source=editors&ust=1778600246527759&usg=AOvVaw1WPz85Zcw7nGY3CDSeB9VD) help needed



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Saiyedul Islam (AMD)
