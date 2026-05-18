### 2023, May 24

Agenda

New 

  * OpenMP version change
  * Bump up GCC requirement for libomp?
  * Summary of OpenMP F2F (Deepak)



Previous

  *    LibC Status


  * [[libc] Enable multiple threads to use RPC on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D148943&sa=D&source=editors&ust=1778600246090910&usg=AOvVaw0z6bQTrjSfrFeL8HxL0I-_)
  * [[libc] Support concurrent RPC port access on the GPU](https://www.google.com/url?q=https://reviews.llvm.org/D149598&sa=D&source=editors&ust=1778600246091029&usg=AOvVaw0uHmavjpm_nuwEFCXoMNAg)
  * [[libc] Enable running libc unit tests on AMDGPU](https://www.google.com/url?q=https://reviews.llvm.org/D149517&sa=D&source=editors&ust=1778600246091140&usg=AOvVaw0Tv_INi_kg1GOxhcz3SgUO)
  * [[libc] Enable running libc unit tests on NVPTX](https://www.google.com/url?q=https://reviews.llvm.org/D149532&sa=D&source=editors&ust=1778600246091253&usg=AOvVaw2dvOOo4DqmdmtUh38HG8ZI)
  * Nvidia buildbot: [https://lab.llvm.org/buildbot/#/builders/46](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/46&sa=D&source=editors&ust=1778600246091376&usg=AOvVaw0if_zXR34caHsuv79QS91V)
  * AMDGPU buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246091497&usg=AOvVaw1MM-zXaY9NbGJFyGldNH8T)
  * Presentation [LibC for GPUs](https://www.google.com/url?q=https://docs.google.com/presentation/d/1jQ5uoWtTv-esba-aUJSRxsCKoeha_VOtYO1u2XkeCqc/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246091610&usg=AOvVaw0IWR1u04ARc7D1d9PeL9vM)


  * Reverse offloading proof of concept demo
  * [https://github.com/jhuber6/OpenMP-reverse-offloading](https://www.google.com/url?q=https://github.com/jhuber6/OpenMP-reverse-offloading&sa=D&source=editors&ust=1778600246091777&usg=AOvVaw1eOOYeLGG7o062GjpRs1Hi)Switch current "experimental" AMDGPU OpenMP Runtime buildbot to production and move the current "production" buildbot into staging


  * Experimental buildbot does make check-openmp, check-clang, check-llvm, check-lld, check-libc
  * Production buildbot: [https://lab.llvm.org/buildbot/#/builders/193](https://www.google.com/url?q=https://lab.llvm.org/buildbot/%23/builders/193&sa=D&source=editors&ust=1778600246092105&usg=AOvVaw39I6uCdrfVjticJjY2S4yg)
  * Experimental buildbot: [https://lab.llvm.org/staging/#/builders/200](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/200&sa=D&source=editors&ust=1778600246092242&usg=AOvVaw1W8Dk--r3_kpXcpRs-TBJl) 


  *   * One SPEC HPC C/C++ test is still not working on Frontier, five are running now.
  * AMD signal active waiting[ https://reviews.llvm.org/D148808](https://www.google.com/url?q=https://reviews.llvm.org/D148808&sa=D&source=editors&ust=1778600246092477&usg=AOvVaw3URv5sLUsknIL7YtWPe_b-)How to handle multiple images with conflicting architectures
  * [https://reviews.llvm.org/D147756](https://www.google.com/url?q=https://reviews.llvm.org/D147756&sa=D&source=editors&ust=1778600246092650&usg=AOvVaw2VzTfqqdWtw5rdxVQOchdm)
  * RPC Server library


  * [https://reviews.llvm.org/D147054](https://www.google.com/url?q=https://reviews.llvm.org/D147054&sa=D&source=editors&ust=1778600246092794&usg=AOvVaw2WLLOFaEaig6Cvgo56byt7)


  * SPIRV/Intel offloading 


  * WIP for device runtime: [https://reviews.llvm.org/D144893](https://www.google.com/url?q=https://reviews.llvm.org/D144893&sa=D&source=editors&ust=1778600246092957&usg=AOvVaw16OQSYs49bqsO8MtpJxCFo)


  * Need help to identify the right intrinsics/builtins (@Intel)


  * Driver missing
  * Plugin missing


  * OMPT for nextgen plugins - refactored 'legacy' patches


  * [https://reviews.llvm.org/D124652](https://www.google.com/url?q=https://reviews.llvm.org/D124652&sa=D&source=editors&ust=1778600246093272&usg=AOvVaw37GVTA3VAhiBwxUsMPdNL7)
  * [https://reviews.llvm.org/D127365](https://www.google.com/url?q=https://reviews.llvm.org/D127365&sa=D&source=editors&ust=1778600246093367&usg=AOvVaw0cmZYiTqsgfq_n35jEATBS)
  * [https://reviews.llvm.org/D127367](https://www.google.com/url?q=https://reviews.llvm.org/D127367&sa=D&source=editors&ust=1778600246093465&usg=AOvVaw2q6VONvbLby8UeJmFT4XS4)


  * Remove old plugins: ~ mid March
  * LLVM/OpenMP 16 -- What's new: [OpenMP Offloading in LLVM 16](https://www.google.com/url?q=https://docs.google.com/presentation/d/1ugiN6J1hfk7hIRvuOONzbYsYpVXK0_ukl6EBVxV3cKU/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246093637&usg=AOvVaw3N6C9yH8vr6Zp7CMF4uPub) 
  * Clang OpenMP support: [https://reviews.llvm.org/D141541](https://www.google.com/url?q=https://reviews.llvm.org/D141541&sa=D&source=editors&ust=1778600246093757&usg=AOvVaw2ciEq-Xn83tDzMhTYIfCki) 
  * [https://reviews.llvm.org/D116908](https://www.google.com/url?q=https://reviews.llvm.org/D116908&sa=D&source=editors&ust=1778600246093866&usg=AOvVaw1e2B_nMndj72tyJZdx8dSN) 
  * Libc for GPU


  * Part of LLVM/libc


  * String and type functions for now
  * libm_gpu.a should be our next target
  * Allocators (Shilei)


  * Multiple needed (pool, bump, …)


  * Testing is an issue


  * Direct GPU compilation is a possibility to create standalone tests


  * GPU libc WIP [https://libc.llvm.org/gpu_mode.html](https://www.google.com/url?q=https://libc.llvm.org/gpu_mode.html&sa=D&source=editors&ust=1778600246094413&usg=AOvVaw0Hl85YQmeu7NhD2xlFr1bn)


  10. Allocate "all" device memory
  11. Launch -> Write the image, write all "user allocated" memory, inlc. arguments, parameters
  12. Replay -> load image + user allocated memory, launch with args and parameters


  * [Optimized reduction implementation by Greg](https://www.google.com/url?q=https://drive.google.com/drive/folders/1d2xrH1UYVqKl7ZrRvzR4Q8SA7Ov-BL_s&sa=D&source=editors&ust=1778600246094776&usg=AOvVaw2HRB6pE09K2kb96dZoD8Ww)


  * [Review D126641](https://www.google.com/url?q=https://reviews.llvm.org/D136641&sa=D&source=editors&ust=1778600246094861&usg=AOvVaw2tvCA_otAkVg6xg2xTsdrH)


  * Reduction alternative:


  * [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp#L201](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/red.cpp%23L201&sa=D&source=editors&ust=1778600246095085&usg=AOvVaw0nQE9SGd9vKSr5HH4X9iY2)
  * Reduction impl entry point: [https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp#L2059](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/blob/c4e637d2c94959ca493363b921aa226286188eb3/openmp/libomptarget/DeviceRTL/src/Reduction.cpp%23L2059&sa=D&source=editors&ust=1778600246095384&usg=AOvVaw0Qz6WB_Pu83vxCv2jA6w21) 



  * OpenMP Cluster and MPI plugin [[https://reviews.llvm.org/D136278](https://www.google.com/url?q=https://reviews.llvm.org/D136278&sa=D&source=editors&ust=1778600246095546&usg=AOvVaw11VlaLstVd8U-oIM8w8DwY)] 
  * Segmentation fault when a constant variable is used in a map clause


  * Caused by a copy-back from the device
  * Review: [https://reviews.llvm.org/D137649](https://www.google.com/url?q=https://reviews.llvm.org/D137649&sa=D&source=editors&ust=1778600246095784&usg=AOvVaw3zxJ28fhtnQY_yXNERmvj_) 


  * [https://reviews.llvm.org/D135162](https://www.google.com/url?q=https://reviews.llvm.org/D135162&sa=D&source=editors&ust=1778600246095873&usg=AOvVaw2n3ecDn4VxfybnMZlCNXe5)
  * Changing register requires


  * [https://reviews.llvm.org/D133539](https://www.google.com/url?q=https://reviews.llvm.org/D133539&sa=D&source=editors&ust=1778600246096004&usg=AOvVaw3jRx9zk4TUlMUyLiBzMOfo)


  * Replaces the `omp_register_requires` call with a global array registered the same way we handle globals / kernels
  * Requires breaking backwards compatibility


  * Could be made mostly backwards compatible, only losing support for unified shared memory in old executables.


  * Device destructors


  * By the time the host calls the destructor the plugin has been destructed.


  * Lifetime extending patch was reverted for AMD so this no longer works


  * Make the plugins handle it directly


  * New libomptarget plugin infrastructure 


  * [https://reviews.llvm.org/D134396](https://www.google.com/url?q=https://reviews.llvm.org/D134396&sa=D&source=editors&ust=1778600246096680&usg=AOvVaw1kmBSvO4STBXbCjlvQyf7D)


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246096854&usg=AOvVaw1emY93UkrrcSuPBXdCw7Es)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246096958&usg=AOvVaw1gfw7BpULxzffyY5fKcADX) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246097126&usg=AOvVaw1KLMjAFjDryCcvBXJtYurc) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  *  if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246097648&usg=AOvVaw3N9G81T6j_A0F3JOhSEyFL) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246097811&usg=AOvVaw2yOVMNZ3Q1jzDCS9J7SuEd) only adds the plugin runtime support


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246098007&usg=AOvVaw2pL2I-vKPcQ9utfdLyByUR)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246098201&usg=AOvVaw1HJ93XIIm2ho3IRARbjQl6)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246098358&usg=AOvVaw1UY81slR90TY_kOnVDeSpA): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246098545&usg=AOvVaw3TxEuHjGAQmUo64MFBmJ63) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)
