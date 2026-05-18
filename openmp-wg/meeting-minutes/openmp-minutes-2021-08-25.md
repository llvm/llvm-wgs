### 2021, Aug 25th

### Agenda

  * 13.0.0 release schedule



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * Static library linking ([https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246500570&usg=AOvVaw0ageVWQ6fcfieB98vjlxwf), will be updated once D108291 lands)) ?


  * [clang-nvlink-wrapper] Wrapper around nvlink for archive files ([https://reviews.llvm.org/D108291](https://www.google.com/url?q=https://reviews.llvm.org/D108291&sa=D&source=editors&ust=1778600246500752&usg=AOvVaw3G3fxJ1IXQfW0Hxpzt4s5G) up for review)
  * [clang-offload-bundler] Make Bundle Entry ID backward compatible ([https://reviews.llvm.org/D106809](https://www.google.com/url?q=https://reviews.llvm.org/D106809&sa=D&source=editors&ust=1778600246500912&usg=AOvVaw3z9mUMbbcIVESpAwiynq9O))


  * required for downstream amdgpu compatibility
  * Should it be pulled in with changes to D105191 so that there is one patch less for the release manager to pull in for llvm-13?



  * Enable map checks in USM mode in libomptarget


  * [https://reviews.llvm.org/D108569](https://www.google.com/url?q=https://reviews.llvm.org/D108569&sa=D&source=editors&ust=1778600246501291&usg=AOvVaw1PYi_iSsa3iw0PI0DptGVQ)
  * LIBOMPTARGET_USM={check,disable}


  * Webpage


  * The webpage is dead, long live the webpage!
  * [https://openmp.llvm.org/](https://www.google.com/url?q=https://openmp.llvm.org/&sa=D&source=editors&ust=1778600246501507&usg=AOvVaw11KOEuRBcdechZzp6e1BLE)
  * [https://openmp.llvm.org/docs](https://www.google.com/url?q=https://openmp.llvm.org/docs&sa=D&source=editors&ust=1778600246501603&usg=AOvVaw03TIMooR5-PpNlfjf5VsLB)


  * AMDGPU buildbots


  * AMDGPU passing here: [https://lab.llvm.org/staging/#/builders/182/](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/182/&sa=D&source=editors&ust=1778600246501764&usg=AOvVaw0VA4apxxHEIr2GSNjDBr-s)


  * Release Notes 13


  * Content needed!
  * [https://openmp.llvm.org/ReleaseNotes.html](https://www.google.com/url?q=https://openmp.llvm.org/ReleaseNotes.html&sa=D&source=editors&ust=1778600246501936&usg=AOvVaw1hs6x0Tz1bNPhmKgTOS5V1)
  * [https://clang.llvm.org/docs/OpenMPSupport.html](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html&sa=D&source=editors&ust=1778600246502042&usg=AOvVaw1IyEKK5HUaXaWmcAAsfTBR)


  * NVPTX buildbots


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246502456&usg=AOvVaw14uSyDi7BQcdcnAEVJbl8E) (don't clean source dir)


  * x86_64-pc-linux-gnu failures have been marked as 'UNSUPPORTED'


  * [https://reviews.llvm.org/rGad0f6e1d984067a3dc81c17abcdd2fc3c7ff9946](https://www.google.com/url?q=https://reviews.llvm.org/rGad0f6e1d984067a3dc81c17abcdd2fc3c7ff9946&sa=D&source=editors&ust=1778600246502717&usg=AOvVaw2O9LVCHk97pa8gBMbq5HgH)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246502798&usg=AOvVaw0jdoR9QhkClO7TLd-coc-T); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246502861&usg=AOvVaw018KMTaZlPnbzlB9GJOrFX) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246503076&usg=AOvVaw0h-CdGMcVQTLBmjkMfjp1-) (under review)


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246503213&usg=AOvVaw0tqiCd_mqkcE8zMkx8Y0KS) [FLAKY] (wrong result)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246503491&usg=AOvVaw3pBQx4G33YvTwIVP8YR-vd), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246503581&usg=AOvVaw2zNLjSmuyf5u2ZHtrNr5jn))
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246503727&usg=AOvVaw0a3OW_oPuo4xtNdvsxGIrz) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply
  * Rpath, runpath, env vars and fragility of toolchains when more than one are on disk
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246504103&usg=AOvVaw3bEIG1okwxsWsJ0_14CUEs)


  * pre-merge bot failing with libarcher failures: [https://reviews.llvm.org/D105811  ](https://www.google.com/url?q=https://reviews.llvm.org/D105811&sa=D&source=editors&ust=1778600246504254&usg=AOvVaw00M9WIp7BXI6cE5lapDloT)[https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246504356&usg=AOvVaw0PJ_D8XjlcK7mdC1VBOil5)
  * Fixed by D106855


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246504665&usg=AOvVaw2hYMZWKo6qbR4xB_askZbk)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246504871&usg=AOvVaw1eZ6pDfS4DQ6nwcG0qINtc)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49787](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49787&sa=D&source=editors&ust=1778600246505054&usg=AOvVaw3-eLnCITgkCscMdMhVQzYv) compiler/runtime API mismatch for async mapping
  * [https://bugs.llvm.org/show_bug.cgi?id=50336](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50336&sa=D&source=editors&ust=1778600246505212&usg=AOvVaw1gaoWLihIHjfnzX-mXCw9R) (Should be fixed in [https://reviews.llvm.org/D107668](https://www.google.com/url?q=https://reviews.llvm.org/D107668&sa=D&source=editors&ust=1778600246505305&usg=AOvVaw2HZFE3jnWg3eaj3r_pFDGt))



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * George Rokos (Intel)
  * Ravi Narayanaswamy (Intel)
  * Jon Chesterfield (AMD)
  * Johannes Doerfert (ANL)
