### 2023, Mar 22

Agenda

  * Initial RPC support in libc


  * [https://reviews.llvm.org/D145913](https://www.google.com/url?q=https://reviews.llvm.org/D145913&sa=D&source=editors&ust=1778600246144016&usg=AOvVaw3TOfyL7CmW0vVtVtHwxqhh)


  * Status of omp loop directive?


  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246144167&usg=AOvVaw2hLkOIe1u3WvDCeQwO-2ou) 
  * [https://reviews.llvm.org/D145823](https://www.google.com/url?q=https://reviews.llvm.org/D145823&sa=D&source=editors&ust=1778600246144270&usg=AOvVaw3b6au2T5v2WVbx0TGZUWqb) 


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246144426&usg=AOvVaw1QQq4_NnY-Y8xz5qJGKy_1)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246144725&usg=AOvVaw0P3Mk6CVQn2CNwG29cf0cu)
  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246144827&usg=AOvVaw3qAsd0dR1sFmPcJae7Nrnr)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246144921&usg=AOvVaw1eyEJEweUZs69PIpFS8UOe)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246145010&usg=AOvVaw0TjFS2Yg-4Ocu0hlYQoYSW)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246145222&usg=AOvVaw2WTWoqefUSuxVkfAPMqWLt) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246145356&usg=AOvVaw0sRnDXFSmHRSW0i_kq6tpP) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246145462&usg=AOvVaw04mpVni2MvMd1JcF6TpC1X) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246145955&usg=AOvVaw30zocedRbAuqI7NqLQuDOG)


  31. Allocate "all" device memory
  32. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  33. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246146318&usg=AOvVaw1RwDvJbnXqp_-HhEQNQQjJ)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246146399&usg=AOvVaw0o1htJE4gPfhHYc75sQK60)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246146617&usg=AOvVaw0tPMmu4nGbY1EN-0zDNrhH)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246146877&usg=AOvVaw3BAk6ykt01ww6SL4QKfqds) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246147031&usg=AOvVaw1xG7VGWzs4YiELmO1cWBrR)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246147275&usg=AOvVaw04S3_RhmY2z9n2SH0A3-YB) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246147367&usg=AOvVaw1RcPaw11DZ6pOXNI0c8VcU)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246147500&usg=AOvVaw10FEHP8N5hv_tVeVl-XGY7)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246148198&usg=AOvVaw3PmAxibOfq1xh47AWG2N95)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246148376&usg=AOvVaw3WQ_zE0h_WFeqlVlYI8OmD)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246148480&usg=AOvVaw0KYAGmMR6LWBTqAjc85dCb) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246148632&usg=AOvVaw1DLEQ9sFMTSyD3cM78Ty4b) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246149174&usg=AOvVaw2a3BSVdQrsUfg-c87ZxzcD) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246149342&usg=AOvVaw0Y86HVf-D39GKdbHsL7CcX) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246149587&usg=AOvVaw2RbMLlJ72PmAj-hQcHS1Ad)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246149781&usg=AOvVaw02gUVMTnLFmnSe5ZuAtAwK)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246149937&usg=AOvVaw1mtICLMsgfnG-HDAkcYZiQ): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246150121&usg=AOvVaw3UvjSeYE_6jmmcPvtHF-rk) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
