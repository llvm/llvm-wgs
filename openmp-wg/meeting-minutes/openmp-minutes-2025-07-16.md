### 2025, July 16

Agenda 

New 

  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245943333&usg=AOvVaw1QYFNkRgsaX_8UpKeZkeZQ) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245943511&usg=AOvVaw2AGM734kDefOrnb6lXPKDo)


  * Discuss 5.2 and 6.0 features


  * omp_target_is_accessible - may need to be modified in the spec, we can implement 5.2 behavior for now


  * 5.2: the pointer passed is a valid host pointer
  * 6.0: the pointer passed is a pointer


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245943938&usg=AOvVaw1G8p3y0O9gBCSiSpQ8Z7Zg)        
  * OpenMP version 5.2 as default


  * Worthwhile to update to 5.2 as default, but needs more thorough review


  * Make sure all the new features are guarded by a warning
  * Updating the version itself implies changing lots of tests
  * Catherine with help, Deepak: will do the assessment


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245944480&usg=AOvVaw3iifWbq5a9yw3_wrghY27D) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * WIP: 2 level reductions: [https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red&sa=D&source=editors&ust=1778600245944748&usg=AOvVaw2lRtVZJTegmYzEc94liOIH) 
  * Discuss [https://github.com/llvm/llvm-project/pull/137307](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/137307&sa=D&source=editors&ust=1778600245944874&usg=AOvVaw1wZgm9OaUiMkDv2jVvGTxC) ?


  * [https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392#diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392%23diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df&sa=D&source=editors&ust=1778600245945123&usg=AOvVaw2z1OHT3eQ6bM7QWzcUrxYl) 


  * Bug(s) that needs looking into, see [https://github.com/llvm/llvm-project/pull/140786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/140786&sa=D&source=editors&ust=1778600245945285&usg=AOvVaw3EqOLl-zlKmKwsAhsOOm1n) 
  * Clang use of new GPU loop interface


  * [https://github.com/jdoerfert/llvm-project/tree/gpu_loop](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/gpu_loop&sa=D&source=editors&ust=1778600245945525&usg=AOvVaw2g_avuGS7Riwy1lG5mA_Ut) 


  * Sanitizer wish list:


  * out-of-bounds
  * Use-after-free
  * Use-after-scope
  * Alignment (which alignment?)
  * Address space
  * Double free()?


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events).


  * Upstream PR opened  
[https://github.com/llvm/llvm-project/pull/147381](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/147381&sa=D&source=editors&ust=1778600245946104&usg=AOvVaw0bQiFcDucUEl28sO90CMiC)


  * Please review
  * Michael Klemm will contact Intel people for review


  * Downstream implementation  
[https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245946407&usg=AOvVaw16DaNesQYwh4ayIj-NyR-C)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245946586&usg=AOvVaw16GPnz0eVaL4sPAkpZgaZQ) 


  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * [[OFFLOAD][OPENMP] 6.0 compatible interop interface by adurang * Pull Request #143491 * llvm/llvm-project](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/143491&sa=D&source=editors&ust=1778600245946884&usg=AOvVaw0LQAEUHSU7Jh473KuHbZk-)


  * Call for review


  * [https://github.com/llvm/llvm-project/pull/149036](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149036&sa=D&source=editors&ust=1778600245947041&usg=AOvVaw28ZffNZxgZHPB0hebBizJi)


  * ATTACH implementation in the runtime


  * ARB will vote to produce JSON files (for us to use)


  * Update : ARB has approved for LLVM to use.  OpenMP Lang committee needs to approve each release
  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Compound constructs in Flang (and Clang)


  * New [3/26]: Updated PR for compound root directive: [https://github.com/llvm/llvm-project/pull/118878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/118878&sa=D&source=editors&ust=1778600245947669&usg=AOvVaw2O_xCkvwNzvmiT4YYxoYCM)
  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600245947905&usg=AOvVaw3RJ7NivPvbc8R91aw1pK11) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break



Previous

  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600245948579&usg=AOvVaw0DZiOvPceA3DsI2BI2smBc) (-DLLVM_ENABLE_PROJECTS=openmp): 


  * Link issue since https://github.com/llvm/llvm-project/pull/74520
  * Tries to use lld with gcc-compiled lto objects
  * RUNTIMES=openmp disables -flto because CMake test looks for LLVMgold.so


  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600245948940&usg=AOvVaw21MscWpXTEBvQf96vqYzKA) (-DLLVM_ENABLE_RUNTIMES=openmp): 21 failed testsomp_get_num_procs() on the device not supported anymore? ([https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c#inline-9277](https://www.google.com/url?q=https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c%23inline-9277&sa=D&source=editors&ust=1778600245949186&usg=AOvVaw0OqWoPkRK6ieURW7H-kH6f))


  * OMP Places [https://www.openmp.org/spec-html/5.1/openmpse62.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.1/openmpse62.html&sa=D&source=editors&ust=1778600245949328&usg=AOvVaw1NFcHcj6sDp9AtbL0u0C9W)


  * omp_get_place_num_procs(): [https://www.openmp.org/spec-html/5.0/openmpsu134.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.0/openmpsu134.html&sa=D&source=editors&ust=1778600245949487&usg=AOvVaw1g_J2gN7q3L1LEDFR9BRjn)
  * New offloading command line reference
  * [https://openmp.llvm.org/CommandLineArgumentReference.html](https://www.google.com/url?q=https://openmp.llvm.org/CommandLineArgumentReference.html&sa=D&source=editors&ust=1778600245949674&usg=AOvVaw0XowtmSeNzzA4s2A_IHOX2)Target annotations for tuning (min/max workgroup size, etc.)



#pragma omp target teams distribute parallel for ompx_attribute(amdgpu_waves_per_eu(6), amdgpu_flat_work_group_size(64, 256), __launch_bounds__(256, 6))  num_teams(NumTeams) thead_limit(ThreadLimit)

                                         for (...)

  * Next time: Testing libm-gpu.a,  WIP, Anton will talk about it soon: 


  * [timing_histograms (1).pdf](https://www.google.com/url?q=https://drive.google.com/file/d/1ZK9J-iJAFjb7cQb7ghP6xSqMbUukeRXW/view?usp%3Dshare_link&sa=D&source=editors&ust=1778600245950271&usg=AOvVaw3YuLnGnoR_OlLFEDwy_l8p)


  * [error_plots (1).pdf](https://www.google.com/url?q=https://drive.google.com/file/d/1372FZKRRPTuERCAuJrAls7Q5zI4LsRfj/view?usp%3Dshare_link&sa=D&source=editors&ust=1778600245950383&usg=AOvVaw3pWIfCoJi3Mo9-Rp4-u55X) 
  * Landed support for the libc RPC in OpenMP and the wrapper headers


  * [[libc] Add support for creating wrapper headers for offloading in clang](https://www.google.com/url?q=https://reviews.llvm.org/D154036&sa=D&source=editors&ust=1778600245950584&usg=AOvVaw08TE7u9Yo1ZpkcT_7y08Kd)
  * [[Libomptarget] Begin implementing support for RPC services](https://www.google.com/url?q=https://reviews.llvm.org/D154312&sa=D&source=editors&ust=1778600245950696&usg=AOvVaw1HjVFV7KVMF2vd_YQkRuiG)


  * Minimal support for reverse offloading via GPU libc


  * [[libc] Add basic support for calling host functions from the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D155003&sa=D&source=editors&ust=1778600245950885&usg=AOvVaw1JAguE4K7diNuH5HU0i90z)


  * What should get in before the LLVM 17 forkRPC implementation in libomptarget [https://reviews.llvm.org/D154312](https://www.google.com/url?q=https://reviews.llvm.org/D154312&sa=D&source=editors&ust=1778600245951041&usg=AOvVaw3IVdNJC2F5TWzapqM9_JZ7)
  * [[libc] Add support for creating wrapper headers for offloading in clang](https://www.google.com/url?q=https://reviews.llvm.org/D154036&sa=D&source=editors&ust=1778600245951168&usg=AOvVaw0-bZ_otj-DGX6ATBzRe49C)
  * Header proposal


  * [D153897: [libc][hdr-gen] Add special offloading handling for the GPU targe](https://www.google.com/url?q=https://reviews.llvm.org/D153897&sa=D&source=editors&ust=1778600245951327&usg=AOvVaw3C7DzKYXDFvjk3g5KkmA_Q)t
  * Alternative in progress


  * OpenMP does not apply values to canonical definitions


  * [[OpenMP] Always apply target declarations to canonical definitions](https://www.google.com/url?q=https://reviews.llvm.org/D153369&sa=D&source=editors&ust=1778600245951593&usg=AOvVaw0k5aGPLbEQvKsta3CTkATS)
  * Important for providing headers for libc


  * Implement as a single header generated by `libc` that both the host and the device include


  * One downside, `omp declare target to() make offloading entries


  * Libm work


  * [D153395: Populating 'libmgpu.a' for math on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D153395&sa=D&source=editors&ust=1778600245951976&usg=AOvVaw2IW4XekkYvAUFmQiIzCjDz).
  * [D152603: [libc] Add math functions to AMD/NVPTX libm](https://www.google.com/url?q=https://reviews.llvm.org/D152603&sa=D&source=editors&ust=1778600245952122&usg=AOvVaw0YMfOi8qdDR00KOyobu0Ea)


  * Work on exporting RPC to OpenMP
  * [[libc] Rename and install the RPC server interface](https://www.google.com/url?q=https://reviews.llvm.org/D153040&sa=D&source=editors&ust=1778600245952290&usg=AOvVaw09OQs0S-PQL2lkCbh4NXG3)Initial proposed patch for implementing a libm upstream


  * [[libc] Begin implementing a 'libmgpu.a' for math on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D152486&sa=D&source=editors&ust=1778600245952464&usg=AOvVaw0kgoLu2ozhC9OAgWMpkj7I)
  * The libc maintainers want an implementation in the LLVM libc. Unimplemented functions will temporarily be mapped to vendor functions


  * GPU/Offloading workshop prior to LLVM Dev: [https://discourse.llvm.org/t/pre-llvm-dev23-gpu-offloading-workshop/71338](https://www.google.com/url?q=https://discourse.llvm.org/t/pre-llvm-dev23-gpu-offloading-workshop/71338&sa=D&source=editors&ust=1778600245952780&usg=AOvVaw0Cx8h589Kx0LIWAnrfSz0u)
  * Mapper still not working


  * [https://github.com/llvm/llvm-project/issues/61636](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/61636&sa=D&source=editors&ust=1778600245952935&usg=AOvVaw3LWoiXdZ5wVRBoGxt6yEA5)
  * Tests: [dbd6759](https://www.google.com/url?q=https://github.com/llvm/llvm-project/commit/dbd6759dac52fa91d3321aaf0d9d78fbe3772dd4&sa=D&source=editors&ust=1778600245953035&usg=AOvVaw3SG4f90Vlr064VL6a7YIUm)


  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600245953167&usg=AOvVaw0hfYzf6ipz3T_a3lg3Z0ok) Libm for the GPU


  * Easiest solution is to use the `libc` infrastructure and remap calls to the existing device libs
  * E.g. -Xclang -mlink-builtin-bitcode -Xclang libdevice.10.bc
  * Can we redistribute NVIDIA's libdevice?


  * Artem from Google is asking for this and an MLIR project, license seems to suggest so


  * The answer is "yes"


  * Exporting the RPC interface from libc


  * [[libc] Begin implementing a library for the RPC server](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600245953711&usg=AOvVaw0uUKitH1og-EFp14fiwEwj)
  * [[libc] Export GPU extensions to `libc` for external use](https://www.google.com/url?q=https://reviews.llvm.org/D152283&sa=D&source=editors&ust=1778600245953821&usg=AOvVaw0GyIHfR8nekJXiOkW-sFie)


  * Moving the AMDGPU libc build bot to staging


  * [https://lab.llvm.org/staging/#/builders/247](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/247&sa=D&source=editors&ust=1778600245954013&usg=AOvVaw1SOIOLuDKGeUWjFFN_Uk7n)


  * Leftover runtime "state" down to 1 element (for simple kernels)
  * Lightweight Attributor under review -> Attributor compile time reduction under development
  * Flang OpenMP offload is making nice progress (thanks to AMD)
  * Implementing the device runtime in a separate project


  * Some complains about the project / runtimes handling


  * Remove keep alive functionality in OpenMP [https://reviews.llvm.org/D151324](https://www.google.com/url?q=https://reviews.llvm.org/D151324&sa=D&source=editors&ust=1778600245954530&usg=AOvVaw1t2EqiKKxyom1-saEVvziC)


  * Used to be required to keep RTL functions alive
  * We unconditionally link the library late now which should prevent this from happening


  * Libm for the GPU


  * Easiest solution is to use the `libc` infrastructure and remap calls to the existing device libs
  * E.g. -Xclang -mlink-builtin-bitcode -Xclang libdevice.10.bc
  * Can we redistribute NVIDIA's libdevice?


  * Artem from Google is asking for this and an MLIR project, license seems to suggest so


  * Integrating the libc RPC implementation into OpenMP


  * How to do this?
  * Header oly library, but exposes libc internals
  * Goals for LLVM 1n7 release?


  * OpenMP version change
  * Bump up GCC requirement for libomp?
  * Summary of OpenMP F2F (Deepak) 
  * LibC Status


  * [[libc] Enable multiple threads to use RPC on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D148943&sa=D&source=editors&ust=1778600245955557&usg=AOvVaw2E_0imoAKxnE2Sl5jsmmxA)
  * [[libc] Support concurrent RPC port access on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D149598&sa=D&source=editors&ust=1778600245955680&usg=AOvVaw0g1EAioZuvAeU9AnFQ8F3z)
  * [[libc] Enable running libc unit tests on AMDGPU](https://www.google.com/url?q=https://reviews.llvm.org/D149517&sa=D&source=editors&ust=1778600245955787&usg=AOvVaw2Arzh8TkkzaKX8JccnzgQW)
  * [[libc] Enable running libc unit tests on NVPTX](https://www.google.com/url?q=https://reviews.llvm.org/D149532&sa=D&source=editors&ust=1778600245955889&usg=AOvVaw3U-qPjk_vhyFGLRVy-LPt2)
  * Nvidia buildbot: [https://lab.llvm.org/buildbot/#/builders/46](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/46&sa=D&source=editors&ust=1778600245956010&usg=AOvVaw1ZuF6neAp8YlsMRdF4AaM8)
  * AMDGPU buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600245956154&usg=AOvVaw3TxfxU_tNkBG3Q2HDWxvzc)
  * Presentation [LibC for GPUs](https://www.google.com/url?q=https://docs.google.com/presentation/d/1jQ5uoWtTv-esba-aUJSRxsCKoeha_VOtYO1u2XkeCqc/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600245956283&usg=AOvVaw1Icd3vWvF6s66yRTJ1d2vC)


  * Reverse offloading proof of concept demo
  * [https://github.com/jhuber6/OpenMP-reverse-offloading](https://www.google.com/url?q=https://github.com/jhuber6/OpenMP-reverse-offloading&sa=D&source=editors&ust=1778600245956455&usg=AOvVaw3kY1y_c6fgmwMlsmRDQL1l)Switch current "experimental" AMDGPU OpenMP Runtime buildbot to production and move the current "production" buildbot into staging


  * Experimental buildbot does make check-openmp, check-clang, check-llvm, check-lld, check-libc
  * Production buildbot: [https://lab.llvm.org/buildbot/#/builders/193](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193&sa=D&source=editors&ust=1778600245956784&usg=AOvVaw0QMZl7ZQpv-5grwtunlulm)
  * Experimental buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600245956909&usg=AOvVaw3ujotuSnvMlCmb_Z-ZtUIA) 


  *   * One SPEC HPC C/C++ test is still not working on Frontier, five are running now.
  * AMD signal active waiting[ https://reviews.llvm.org/D148808](https://www.google.com/url?q=https://reviews.llvm.org/D148808&sa=D&source=editors&ust=1778600245957149&usg=AOvVaw3PxpGopJWRH2zQcVWN7tOK)How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600245957287&usg=AOvVaw27MY-kUWmheSUkKCrJ2slj)
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600245957413&usg=AOvVaw3qVbuvMUTsnKW83oX89R5s)


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600245957577&usg=AOvVaw24-ObhEHdhUtCOxdnA0FGC)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600245957881&usg=AOvVaw0ZUV1fCqMMotWRErsa3whE) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600245958007&usg=AOvVaw0_IRSY1aiVIbQsnEMDt8dZ) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600245958285&usg=AOvVaw2QmU5WaPOpL5xDWyb5L7lu) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600245958789&usg=AOvVaw3Gms0C926UnzbWQ2ftKIjG)


  1. Allocate "all" device memory
  2. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  3. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600245959153&usg=AOvVaw2hswzV5Gbv0Za0nTPpSLju)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600245959240&usg=AOvVaw2nnM1I9oPh7PVLRo64MPg_)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600245959490&usg=AOvVaw3-aRFG0R4qkmcboth4w6zr)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600245959755&usg=AOvVaw0vLc7DR4P4Eu1-jadvmiTW) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600245959914&usg=AOvVaw3DYw4h9htUcvfekRE7ewH-)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600245960180&usg=AOvVaw2xFkEptqfcQUHrDyBZlXQj) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600245960283&usg=AOvVaw02KUfMw77FAUl359Ar9hj3)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600245960421&usg=AOvVaw1y1l7tANe-HZ7Xq4lZJvMw)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600245961082&usg=AOvVaw0f0ZoroJNoYio4WyDd_IhW)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600245961266&usg=AOvVaw0396gCjjBjWYg8EHjmjcof)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600245961368&usg=AOvVaw0EKKNSk1I-bbm57sUitHk9) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600245961533&usg=AOvVaw3m7kTdR6R1K-aOFGOq6Kfb) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600245962048&usg=AOvVaw3RzOjk5UG2wD4IXCXHPmpF) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600245962220&usg=AOvVaw1LcEoB0Zxok214phqZTXyE) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600245962435&usg=AOvVaw3p8q9cei0p737modfgEDUR)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600245962616&usg=AOvVaw3fPH_PRMnHxzSYiRkUEYzb)
  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600245962901&usg=AOvVaw3kI8Qwxts83zChBdZwDhCS) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600245963019&usg=AOvVaw3AmBhIiC6brs-7yGCU5CDF)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600245963145&usg=AOvVaw2rCx9So00sfeGCOsHqEdhx)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600245963266&usg=AOvVaw0bGayPeaNdvTNUB8_Vr55w)
