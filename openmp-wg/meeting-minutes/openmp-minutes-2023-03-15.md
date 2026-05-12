### 2023, Mar 15

Agenda

  * Initial RPC support in libc


  * [https://reviews.llvm.org/D145913](https://www.google.com/url?q=https://reviews.llvm.org/D145913&sa=D&source=editors&ust=1778600246150434&usg=AOvVaw240I8hKsfxHVu1A4GRsVqJ)


  * Status of omp loop directive?


  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246150570&usg=AOvVaw3XBQs8ph_KG4wXuQMwSUBA) 
  * [https://reviews.llvm.org/D145823](https://www.google.com/url?q=https://reviews.llvm.org/D145823&sa=D&source=editors&ust=1778600246150672&usg=AOvVaw07Cu1TrFtiHrJ2B_GW5RkZ) 


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246150830&usg=AOvVaw1bBbG75GXLv-4tUGXVAS0j)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246151165&usg=AOvVaw1-AvjZjYqGjWc7bBpd4W7u) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246151290&usg=AOvVaw0U6bClZUR0178a-M01saeL) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246151402&usg=AOvVaw23UqvtOr6v9epIHDLDQ-iD) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246151951&usg=AOvVaw20571ONJD34jODHC1oAs-k)


  34. Allocate "all" device memory
  35. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  36. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246152318&usg=AOvVaw0GuPWimZJcBjWEZHZhT0Oe)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246152406&usg=AOvVaw3LAVKQEAlwjY2qqLi4E4Z_)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246152625&usg=AOvVaw1kZyt884WIhdM_XeZviSfS)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246152883&usg=AOvVaw3qWs9_Tzp6Q3k6d7nJpN-R) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246153039&usg=AOvVaw22vZVQiz4zGKLDO1EUo-Vs)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246153290&usg=AOvVaw3zB_bhqfAA984tvD0NuTWl) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246153383&usg=AOvVaw2J3N_Nt8YtZSRFZOCvnC8I)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246153514&usg=AOvVaw2J_F7bnhtJDZg9ZKm2vcF2)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246154195&usg=AOvVaw1pNdPNYgGX8ZiPOFpTdAsb)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246154363&usg=AOvVaw3IoOeQj-dG4bTcKlvOduoE)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246154472&usg=AOvVaw0Gg5N5l14CXA7AAMoijsiq) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246154627&usg=AOvVaw0IHOBLh3_ukHH_RTDQphTM) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246155152&usg=AOvVaw3lHPmhZknoazFTqQT3UOck) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246155323&usg=AOvVaw0T-hAQVAVyBu9hYeyS6Rkc) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246155519&usg=AOvVaw3aBlwJJuMrFGzHhPk_QLs3)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246155707&usg=AOvVaw32HJp7kPkQwq2ONx90dWdR)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246155864&usg=AOvVaw2CiKd3ws6UECt-AfSHv5u_): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246156044&usg=AOvVaw1IAb_2riuTo2IGaE__IysR) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
