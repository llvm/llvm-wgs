### 2023, April 05

Agenda

  * New Topics
  * OpenMP asynchronous memory copy support


  * Not sure if this fully respects the spec: "The value of num_dims must be between 1 and the implementation-defined limit, which must be at least three." and "An application can determine the number of inclusive dimensions supported by an implementation by passing NULL for both dst and src. The routine returns the number of dimensions supported by the implementation for the specified device numbers. No copy operation is performed."
  * [https://reviews.llvm.org/D136103](https://www.google.com/url?q=https://reviews.llvm.org/D136103&sa=D&source=editors&ust=1778600246130068&usg=AOvVaw0fsGgZL_62H4TQxw4nNdho) 


  * Expand  RPC support in libc
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246130242&usg=AOvVaw1WIyyOea7WO8fLy5xTGPmy)


  * Status of omp loop directive?


  * Reduction on Loop constructs.  Is it supported
  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246130449&usg=AOvVaw29uuS90UeQXVFGUlviBOEe) 
  * [https://reviews.llvm.org/D145823](https://www.google.com/url?q=https://reviews.llvm.org/D145823&sa=D&source=editors&ust=1778600246130541&usg=AOvVaw3LgGDbBTut0nYS1oxXj9Wq) 


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246130700&usg=AOvVaw3aB11bBY0HqfV_zXGlr6hH)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246131027&usg=AOvVaw2QQc7TG-K1d0CusUW6KcdD)
  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246131134&usg=AOvVaw0O_2r_CGwYZp41EqxxKLbZ)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246131227&usg=AOvVaw3xTAosgcO03_W-rx_T6iIA)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246131326&usg=AOvVaw3FDmfrnRG7IPqTK3v8Bo7d)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246131504&usg=AOvVaw3TEKvbwDT0GBdKGmiMnzFI) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246131620&usg=AOvVaw37ATnjLseiORmzUC19VGsJ) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246131726&usg=AOvVaw3Y0N-pAiniU4AD8VeV5DcB) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246132234&usg=AOvVaw0r_ly85eAsYEGfkjLvCkpW)


  25. Allocate "all" device memory
  26. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  27. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246132590&usg=AOvVaw1JjPHcFcBpzXDMAmyQK2VY)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246132669&usg=AOvVaw3Bt25g88ZlQfYVFvzpdVNf)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246132890&usg=AOvVaw1dyChstWcH7V4hgwXcPFtI)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246133155&usg=AOvVaw1nRX2kmnlYsQkD98oyWpaf) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246133316&usg=AOvVaw3wI5cbWrhmQda7Dpq5tmoW)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246133558&usg=AOvVaw1WlI8MTjZxJtIDjgjDRwyG) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246133652&usg=AOvVaw2G3rkIxeQ4vtxfWTNsRTQq)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246133786&usg=AOvVaw3VmocbxvgWzzrp1BEbB7Mr)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246134464&usg=AOvVaw3Otf2auDQZ-GtZ_Ota41TJ)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246134643&usg=AOvVaw19goD5sLqWUWhbqO2Tik4F)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246134741&usg=AOvVaw0SWzQXrskSdHPByKbrLCWV) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246134890&usg=AOvVaw0tY_-yDh5U0GIO7VG8_EA3) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246135448&usg=AOvVaw2tg0j_HH6zBRzJcQk4od2G) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246135617&usg=AOvVaw26sVJctN713kq4jov92erF) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246135844&usg=AOvVaw1x1dwHev3zYagJvIky6SLU)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246136028&usg=AOvVaw2hz7xeK0Ip6vMCKoFQ6VSI)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246136184&usg=AOvVaw3nRE9EQ7qXfUyr-2p8Ro2P): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246136374&usg=AOvVaw09O4kp75mhWDccYZe2CZG9) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
