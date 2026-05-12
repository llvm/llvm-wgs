### 2023, Mar 08

Agenda

  * [Openmp] Segmentation fault on goulash on amdgpu #60602 [https://github.com/llvm/llvm-project/issues/60602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/60602&sa=D&source=editors&ust=1778600246156445&usg=AOvVaw1FlXUcTzXIDBlzBNBKTCCO)


  * This is reproducible with top of trunk. It seems to have started after   
[OpenMP] Modernize the kernel launching interface and APIs  
[https://reviews.llvm.org/rG16a385ba21a921a42009ff971199bce56eb2a86e](https://www.google.com/url?q=https://reviews.llvm.org/rG16a385ba21a921a42009ff971199bce56eb2a86e&sa=D&source=editors&ust=1778600246156703&usg=AOvVaw0LBnl9OWAQsAz5Fd-rkrph) and  
[OpenMP][FIX] Runtime args are not kernel args  
[https://reviews.llvm.org/rG3820d0eaaf4ecb557cbb260e34bf5a9eeb51e0e7](https://www.google.com/url?q=https://reviews.llvm.org/rG3820d0eaaf4ecb557cbb260e34bf5a9eeb51e0e7&sa=D&source=editors&ust=1778600246156865&usg=AOvVaw1Mtd-Rx6dA_-bGwZyzipgR) landed.
  * It fails with both the old and the nextgen plugin.


  * Enthusiasm for removing rpath setting on binaries, aka "trunk openmp doesn't work any more unless you install it under /usr or do unspecified awkward magic, possibly patch trunk yourself before compiling", at D118493.


  * Lack of defensive mechanism in libomp!!! Minimal need is major version check. Don't assume compatibility.


  * Can anyone outside of AMD run tests on AMDGPU hardware at the moment? If so, how do you do so?


  * Bonus question, is there any way to run things on an intel GPU?


  * Github intel/llvm (for SYCL) and intel/compute-runtime (L0 and IGC).


  * Unify the DeviceRTL Cmake handling [https://reviews.llvm.org/D145513](https://www.google.com/url?q=https://reviews.llvm.org/D145513&sa=D&source=editors&ust=1778600246157668&usg=AOvVaw1M0Zc4S9RrIH79Z1B7luaw)


  * Removes LIBOMPTARGET_NVPTX_COMPUTE_CAPABILITIES in favor of LIBOMPTARGET_GPU_ARCHITECTURES=<list>|all|auto


  * Firstprivate variables are passed by-ref if its alignment is greater than alignof(uintptr_t)


  * [https://godbolt.org/z/6jPvMvsxh](https://www.google.com/url?q=https://godbolt.org/z/6jPvMvsxh&sa=D&source=editors&ust=1778600246157975&usg=AOvVaw1_P-70b0J7xPgngYZLf0WR)
  * Shouldn't we be able to pass this by-value
  * [https://godbolt.org/z/sPbE3aP7n](https://www.google.com/url?q=https://godbolt.org/z/sPbE3aP7n&sa=D&source=editors&ust=1778600246158178&usg=AOvVaw0qtM7hBWJpOozK51NZZer-) <\- 64 aligned load is emitted (w/o by-value) (line 262)


  * Status of omp loop directive?


  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246158409&usg=AOvVaw30vcd7OrzjuY1zHdX7dEGR) 


  * Proposal to break non-globally installed clang openmp, [https://reviews.llvm.org/D143306](https://www.google.com/url?q=https://reviews.llvm.org/D143306&sa=D&source=editors&ust=1778600246158559&usg=AOvVaw2aHhZn4MXYYoP3_0aTfuBf)


  * Specifically, stop setting rpath because fedora don't like it, thus openmp programs won't find openmp libraries, and they'll refuse to run. Unless people set LD_LIBRARY_PATH or mess around with the linker themselves, but that'll closely approximate people trying openmp and concluding that it's just broken and giving up
  * It seems there's a configuration file alternative functionality in clang, though I can't see how that could fix things unless it also sets rpath, in which case why would fedora be ok with it? But whatever, the consensus in D143306 is going against me, so if we _don't_ want openmp to stop working from local installs on llvm-16, please speak up


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246159330&usg=AOvVaw2laPkSjPgPZWRLHvr4UB75)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246159660&usg=AOvVaw0TlZ4s3Uoq8_n9wiQ0qyVs) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246159785&usg=AOvVaw3l0xj8xUj5GnYS5-95wVOC) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246159889&usg=AOvVaw2zlHw3h934GzqEeX9xWFkG) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246160568&usg=AOvVaw3A3AU30dmX6fr-m_3ZE_sD)


  37. Allocate "all" device memory
  38. Launch -> Write the image, write all "user allocated" memory, inlc. Arguments, parameters
  39. Replay -> load image + user allocated memory, launch with argos and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246160932&usg=AOvVaw0gQHbrM-DOrORaBngmIQBg)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246161011&usg=AOvVaw37Kjl3fV13m2S_vPP89Nm0)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246161244&usg=AOvVaw1xtm9xYQH2qWsmHbfv5TAC)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246161504&usg=AOvVaw2rDORDXza9krhCJlUDzKRM) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246161668&usg=AOvVaw1aVi9nF8iMqBRx14y9jGKa)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246161902&usg=AOvVaw2WT3Vv0IjzjVxztGSm3af-) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246162002&usg=AOvVaw3BZuBxEW5vI3ul5yVbFusa)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246162146&usg=AOvVaw0CT-Pxj_uOL7peXcHVxoTL)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246162818&usg=AOvVaw3hcXhh1HVUa7SVa7ALLwb3)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246163033&usg=AOvVaw0h46bXy0lh-1F3FGxu66Uv)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246163147&usg=AOvVaw29z1cazbIprq-WZnFXrGiN) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246163305&usg=AOvVaw1lmMQZS4MefpyQ6xMVc74A) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246163829&usg=AOvVaw3om7_XgpTB-pZHvA7XU9nu) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246163988&usg=AOvVaw1oKLswjon_7kllbcFy9e9v) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246164197&usg=AOvVaw1pakQRGwrMUIp5TEGUQSG9)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246164387&usg=AOvVaw0fw4q0XBINn7T_rUhUeEFq)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246164537&usg=AOvVaw0ZF_KVEeQvfbjWYtMCEqjz): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246164752&usg=AOvVaw15DiCtkcld_HQAeXzYPTni) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
