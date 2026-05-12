### 2021, Sept 8th

### Agenda

  * 13.0.0 release schedule



July 27: release/13.x branch created

July 30: 13.0.0-rc1

Aug  24: 13.0.0-rc2

Sep   7: 13.0.0-rc3

Sep  21: 13.0.0-final

  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Landed D109057 (can find device libs without LIBRARY_PATH), D109071 (libomptarget can find plugins without LD_LIBRARY_PATH, tests no longer use LD_LIBRARY_PATH)
  * Debate at D109061 about whether LIBRARY_PATH should take priority over looking next to clang for deviceRTL, continue to win out, or whether it should be totally ignored (which requires users who have put a devicertl somewhere else to specify it with ibomptarget-nvptx-bc-path)


  * Note that 'some other devicertl' is not especially likely to work with clang, so I'd like it to be inconvenient (i.e. must pass the flag), to reduce the odds of doing it by accident)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag


  * Static library linking ([https://reviews.llvm.org/D105191](https://www.google.com/url?q=https://reviews.llvm.org/D105191&sa=D&source=editors&ust=1778600246489849&usg=AOvVaw0RDdGpgO0ppn9D1EO_vRbM), going to update in next few hours))


  * [clang-nvlink-wrapper] Wrapper around nvlink for archive files ([https://reviews.llvm.org/D108291](https://www.google.com/url?q=https://reviews.llvm.org/D108291&sa=D&source=editors&ust=1778600246490043&usg=AOvVaw2BpIGM5jSAtwy69tH6_xDT) merged)
  * [clang-offload-bundler] Make Bundle Entry ID backward compatible ([https://reviews.llvm.org/D106809](https://www.google.com/url?q=https://reviews.llvm.org/D106809&sa=D&source=editors&ust=1778600246490213&usg=AOvVaw1kTg1quFUHJl146dsiHS6w)): merged
  * [clang-nvlink-wrapper] Add documentation in clang docs ([https://reviews.llvm.org/D109225](https://www.google.com/url?q=https://reviews.llvm.org/D109225&sa=D&source=editors&ust=1778600246490416&usg=AOvVaw25wkr9czqJAPAzWh_41yVj)): merged


  * NVPTX buildbots (no update since last week)


  * Currently running here: http://meinersbur.de:8011


  * openmp-offload-cuda-project: http://meinersbur.de:8011/#/builders/1
  * openmp-offload-cuda-runtime: http://meinersbur.de:8011/#/builders/117
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246490877&usg=AOvVaw3O82eWsr9Z2F1iUnzD1nEv) (don't clean source dir)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246490995&usg=AOvVaw0Uut06CROa7VDEujckV1du); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246491052&usg=AOvVaw2PbWFlBO2eRRBUuhH1aj23) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246491277&usg=AOvVaw0bZ4SQlcbB_OncRkbZ04Fl) (under review)


  * [llvm.org/PR51233](https://www.google.com/url?q=http://llvm.org/PR51233&sa=D&source=editors&ust=1778600246491380&usg=AOvVaw3dtHGkT_V-Pu2E2AVLWDjh) [FLAKY] (wrong result)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug50022.cpp



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246491648&usg=AOvVaw0_4mCh1Bic3G7RIdXWFE1z), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246491753&usg=AOvVaw2TpENWfFT_lPCSJKkHfmI8))
  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246491911&usg=AOvVaw12f-evg9LXxZp4Ik5gUlqh) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246492236&usg=AOvVaw2g9qaxYh-pT4D7TLy6ziUR)


  * pre-merge bot failing with libarcher failures: [https://reviews.llvm.org/D105811  ](https://www.google.com/url?q=https://reviews.llvm.org/D105811&sa=D&source=editors&ust=1778600246492384&usg=AOvVaw2wEhpwIe-ml6BhxSr6irqW)[https://reviews.llvm.org/harbormaster/unit/113491/](https://www.google.com/url?q=https://reviews.llvm.org/harbormaster/unit/113491/&sa=D&source=editors&ust=1778600246492468&usg=AOvVaw3iua-7BRQUZLR4DAA4PJv7)
  * Fixed by D106855


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246492771&usg=AOvVaw1cooUPurLmKZtdWGlLIcmX)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246492977&usg=AOvVaw302072lPnj99N6Njll4RJF)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51647](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51647&sa=D&source=editors&ust=1778600246493261&usg=AOvVaw0l_E9F1InI6cVgtgqQfQjM)  
[OpenMPOpt] produces: error: Invalid record (Producer: 'LLVM14.0.0git' Reader: 'LLVM 14.0.0git')


  * failing with invalid record due to a mismatch in the type of the argument and worker.work_fn.addr parameter passed for __kmpc_kernel_parallel due to a difference in address space
  * have tested a fix that:


  *   1) performs the worker.work_fn.addr AllocaInst in the AddressSpace::Local (5) rather than letting a later pass realize it is in the local address space, and
  *   2) adds an AddrSpaceCastInst to generic before the call to __kmpc_kernel_parallel


  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246493899&usg=AOvVaw1VK4h3T_c4Sk9VLZkr1D9D)



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)Johannes Doerfert (ANL)
  * Jon Chesterfield (AMD)
  * George Rokos (Intel)
  * Roger Ferrer Ibañez (BSC)
  * Saiyedul Islam (AMD)
