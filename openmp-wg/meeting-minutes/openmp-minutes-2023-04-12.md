### 2023, April 12

Agenda

New intel

  * Recommended method to restore -rpath usage for OpenMP


  *  [https://reviews.llvm.org/D147943](https://www.google.com/url?q=https://reviews.llvm.org/D147943&sa=D&source=editors&ust=1778600246122026&usg=AOvVaw1KmaiCzkMGCotH9x_EE23w)


  * How to handle multiple images with conflicting architectures


  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246122213&usg=AOvVaw3MG2spQXqphUZ7FwmuY71e)


  * Open Source contributions from HPE (Michael Kruse, Zachary Tschirhart)
  * Variables automatically allocated kmpc_alloc_shared



Previous

  * OpenMP asynchronous memory copy support


  * Not sure if this fully respects the spec: "The value of num_dims must be between 1 and the implementation-defined limit, which must be at least three." and "An application can determine the number of inclusive dimensions supported by an implementation by passing NULL for both dst and src. The routine returns the number of dimensions supported by the implementation for the specified device numbers. No copy operation is performed."
  * [https://reviews.llvm.org/D136103](https://www.google.com/url?q=https://reviews.llvm.org/D136103&sa=D&source=editors&ust=1778600246122920&usg=AOvVaw2WUPf0ncyKpx4qYzl2-GSf) 


  * Expand  RPC support in libc
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246123106&usg=AOvVaw2ez4NCuf-Kg2wITGjjIXtt)


  * Status of omp loop directive?


  * Reduction on Loop constructs.  Is it supported
  * [https://reviews.llvm.org/D144634](https://www.google.com/url?q=https://reviews.llvm.org/D144634&sa=D&source=editors&ust=1778600246123320&usg=AOvVaw2MBr8GuRzRb47ulvdt4xD3) 
  * [https://reviews.llvm.org/D145823](https://www.google.com/url?q=https://reviews.llvm.org/D145823&sa=D&source=editors&ust=1778600246123412&usg=AOvVaw1YH3z2CuRVWMIM9asQ6TId) 


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246123588&usg=AOvVaw1CDoAgNv510whMpT_Bh9ou)


  * Need help to identify the right intinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124070](https://www.google.com/url?q=https://reviews.llvm.org/D124070&sa=D&source=editors&ust=1778600246123904&usg=AOvVaw06tuH7J41m0ZN09u_17DsI)
  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246124030&usg=AOvVaw2g1wgwuRIFrn7rU3zU9mRp)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246124140&usg=AOvVaw2-ucHBdbQ_x4IfjyCWWZZ8)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246124233&usg=AOvVaw0WVBi9MpizVsWE2ZO6vxUR)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246124430&usg=AOvVaw2puiVPoiZzuN8xB47SsRr6) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246124552&usg=AOvVaw1MRVhpTJzbb80hvJhUy2ZG) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246124655&usg=AOvVaw1A-8gXF7NOI8CNhR24DnQU) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246125169&usg=AOvVaw3BZ7RWxyIIvuqAI1xtmNA5)


  22. Allocate "all" device memory
  23. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  24. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246125532&usg=AOvVaw0JCN4cDu190Wy4WYx--mx0)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246125616&usg=AOvVaw0YK6qk_zmGRHcwUGK2BOG-)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246125832&usg=AOvVaw21jaoFUxF4qhNQXvv-S1Pw)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246126085&usg=AOvVaw2vva3irPTgej-G0wcmdO8f) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246126268&usg=AOvVaw0nWVYKHx-OOZcl6EFkkFZ2)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246126502&usg=AOvVaw28MKGJOYOhVCf5LVauXGDN) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246126601&usg=AOvVaw15Ipa_iz6xTRXBuLxZykDu)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246126737&usg=AOvVaw3fyB9Nsn5YLWDiN2fZc0EO)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246127409&usg=AOvVaw1VNKYzBC4GifQTmP36ofsx)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246127577&usg=AOvVaw2elmirhaUfXHz0qepdKCF5)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246127703&usg=AOvVaw3pdHj7EL5TDP9OvxVkzkDe) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246127859&usg=AOvVaw0j1-AG9tVxa4cpfjg_Uym1) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246128418&usg=AOvVaw3_UHkkuqa4-EXOL509xro_) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246128594&usg=AOvVaw2LVueLrnhfNsUFQ3p-t2Sn) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246128807&usg=AOvVaw2mKM7r_sVY_FM4rXWQz7eS)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246128998&usg=AOvVaw0rCPd73GDAOYDDUTk-oyZH)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246129160&usg=AOvVaw0StO8O8jiXrv5S2923xunf): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246129352&usg=AOvVaw1fdby13xRKRSWaZVCUFypX) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
