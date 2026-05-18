### 2023, April 26

Agenda

New 

  * Switch current "experimental" AMDGPU OpenMP Runtime buildbot to production and move the current "production" buildbot into staging


  * Experimental buildbot does make check-openmp, check-clang, check-llvm, check-lld, check-libc
  * Production buildbot: [https://lab.llvm.org/buildbot/#/builders/193](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193&sa=D&source=editors&ust=1778600246107136&usg=AOvVaw0xwwbcCul4Jd0zHFMTHSg8)
  * Experimental buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246107274&usg=AOvVaw2TJy6YWLefgOKwZE8EqICj) 


  * Multi-threaded RPC support


  * [https://reviews.llvm.org/D148943](https://www.google.com/url?q=https://reviews.llvm.org/D148943&sa=D&source=editors&ust=1778600246107410&usg=AOvVaw2hmoMr2SKa-YdTR1qbg4oT)
  * Nvidia buildbot: [https://lab.llvm.org/buildbot/#/builders/46](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/46&sa=D&source=editors&ust=1778600246107557&usg=AOvVaw2yMd2OJUfKCR4tFJldhQx2)
  * AMDGPU buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246107684&usg=AOvVaw3datB7vjFKNmIUGn5YhZ2z)


  * One SPEC HPC C/C++ test is still not working on Frontier, five are running now.
  * AMD signal active waiting[ https://reviews.llvm.org/D148808](https://www.google.com/url?q=https://reviews.llvm.org/D148808&sa=D&source=editors&ust=1778600246107886&usg=AOvVaw3u4vVtruf7Of7kEek21Ucb)



Previous

  * How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246108104&usg=AOvVaw1lB_QbaOuU8qGuTruq55WY)
  * Expand  RPC support in libc
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246108295&usg=AOvVaw2ec2HtI2ZcoZxwBglRyf5s)


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246108457&usg=AOvVaw1NEtXHDeo3t-o8vqa36-Ni)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246108765&usg=AOvVaw2-Kr7zdzqRXIjB5kqcHed4)
  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246108864&usg=AOvVaw2ZUkuVHzPwaVUjjd3usw3s)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246108987&usg=AOvVaw16JiKSS5JYKMvghbZICciR)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246109090&usg=AOvVaw3HLoUFY2eZHRiSjUyJZFxk)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246109281&usg=AOvVaw39SplJ_DGED4yTioXgh2vT) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246109412&usg=AOvVaw1Lb23E6tPEs83CNHqmy0bl) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246109517&usg=AOvVaw3o9dcWbpdf2WOGwonspQQz) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246110008&usg=AOvVaw3T3AhecffP92DJPzRe11my)


  16. Allocate "all" device memory
  17. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  18. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246110369&usg=AOvVaw3CBftjfL40xXu6nbjTJakT)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246110459&usg=AOvVaw2k01h0n-OWyxbvvlNqHM_f)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246110677&usg=AOvVaw1EpDA6xHRtMo-dkrHkOtd4)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246110941&usg=AOvVaw23Zfq0t_tmH38GysOeR4TS) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246111097&usg=AOvVaw0xHR1hQ1pevtnO5S_GVm-G)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246111334&usg=AOvVaw0sApmhedis0MkUA2A-RcPt) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246111435&usg=AOvVaw366AN-FZC5pDApNslcvTYU)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246111568&usg=AOvVaw3zfcySfASLPRkz3eZ8H74_)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246112266&usg=AOvVaw1dL486hXX1MqtLwmAgFQVM)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246112447&usg=AOvVaw2XkDcGqkRmfm1joeQbaTkG)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246112546&usg=AOvVaw3xC9GDzgK67lO5aINRoqdq) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246112696&usg=AOvVaw3ddHmTttvEY_rzM8kfhfF0) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246113224&usg=AOvVaw2sBFsNzcb7-6xcuBz7bDqW) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246113402&usg=AOvVaw2jYvMa9r3paovc0gwX1S4E) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246113621&usg=AOvVaw2YV9wbTQd8yx82z_AewfUl)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246113818&usg=AOvVaw08L5SUELQBlXF-qZnhzyvN)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246113980&usg=AOvVaw1UiFVIbQVyj18sLOBQTPNN): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246114166&usg=AOvVaw1cBkChuir-NTBvAP9JuwFC) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



### 

### 023, April 19

Agenda

New 

  * RPC implementation WIP


  * [https://reviews.llvm.org/D148288](https://www.google.com/url?q=https://reviews.llvm.org/D148288&sa=D&source=editors&ust=1778600246114576&usg=AOvVaw0oNRStFzSzp2dguJY-hHfb)


  * Status or expected behavior of the schedule clause on GPUs


  * 'ordered schedule(dynamic)'


  * GPU tests for AMDGPU + O3: [https://reviews.llvm.org/D148576](https://www.google.com/url?q=https://reviews.llvm.org/D148576&sa=D&source=editors&ust=1778600246114809&usg=AOvVaw3eldx7f3SdFwWKskTlTNqs)
  * Nested LOOP constructs



Previous

  * Recommended method to restore -rpath usage for OpenMP


  *  [https://reviews.llvm.org/D147943](https://www.google.com/url?q=https://reviews.llvm.org/D147943&sa=D&source=editors&ust=1778600246115062&usg=AOvVaw3YkUpidDKO1KemEi7hzMEO)


  * How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246115239&usg=AOvVaw0Rsl-WMMkNL0FGLNFA8Yuw)
  * Expand  RPC support in libc
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246115420&usg=AOvVaw0TAg_ZNEzeoOGl9hlFCpY1)


  * Status of omp loop directive?


  * Reduction on Loop constructs.  Is it supported
  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246115642&usg=AOvVaw0Eebkgm1Shs9BiXf_V4yeP) 
  * [https://reviews.llvm.org/D145823](https://www.google.com/url?q=https://reviews.llvm.org/D145823&sa=D&source=editors&ust=1778600246115743&usg=AOvVaw3khXS2uLTz9xDFG-gzy6ib) 


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246115900&usg=AOvVaw2bTEgwX1xS_OrnfGzG_mj2)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246116210&usg=AOvVaw1I_l-9QprMkO1LoYa7JH56)
  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246116304&usg=AOvVaw0LkcpiV9XuIF8m1QQkWACD)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246116403&usg=AOvVaw1mf1Rs5MjKv_kSR3i0X5S-)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246116494&usg=AOvVaw0XwM0WKWq0G_GCsMHjXF_9)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246116673&usg=AOvVaw1eQasIdVYip9oiuBs7ICCa) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246116800&usg=AOvVaw3l1iVF0jfMCMyjktdKjyHc) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246116900&usg=AOvVaw2grFYSYTI6Igysrh2w0jVy) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246117407&usg=AOvVaw2TfvskkJfzikkTRtw3yKex)


  19. Allocate "all" device memory
  20. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  21. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246117768&usg=AOvVaw00HOAHOUdzmuSIJ6ejcx4g)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246117846&usg=AOvVaw10XNPYfw94sAXKnLLExU09)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246118061&usg=AOvVaw1fziulQf0hmNCwJUGHAyor)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246118337&usg=AOvVaw1xjegQk28hFMBzMbrdJsvW) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246118499&usg=AOvVaw2I_jrT2V-i0Oy-R6xNdaX6)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246118739&usg=AOvVaw3vzyxUrQZkHeZ4m-UHaWk5) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246118829&usg=AOvVaw3FoVCiE_EMVdPcstShltX1)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246118959&usg=AOvVaw28l4xsvh_bJmkoRiZPklfI)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246119632&usg=AOvVaw2-Pj8pqN8HQlF3_jxcrQ6v)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246119802&usg=AOvVaw2msued6tmtxPUoDeLB52dM)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246119898&usg=AOvVaw1DoW62-l9WI95egqxC2emE) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246120084&usg=AOvVaw0Wwd447zVrQbbVLxEHSZun) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246120642&usg=AOvVaw1tSHU78c4omPOvKP5kIXWU) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246120806&usg=AOvVaw09ne-aF_KM0LqRyUc0Blyf) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246121028&usg=AOvVaw0m7JYaVNu7iHoHUvXo54r2)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246121238&usg=AOvVaw357kM7f8lrEcP4pt5fTFQa)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246121399&usg=AOvVaw2umFA1g5go0BZrJzOcIrAU): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246121598&usg=AOvVaw2m-cIjFwAU4FEaF5ZvwEm7) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
