### 2022, Sept 07

Agenda

  * No more backward compatibility.


  * [https://reviews.llvm.org/D133277](https://www.google.com/url?q=https://reviews.llvm.org/D133277&sa=D&source=editors&ust=1778600246265643&usg=AOvVaw2bp10WJRspy5swKxWCdnAS) and [https://reviews.llvm.org/D133276](https://www.google.com/url?q=https://reviews.llvm.org/D133276&sa=D&source=editors&ust=1778600246265721&usg=AOvVaw0LP2u8-n8Ds4cm6Qm5NCya).
  * Ever since we build libomptarget and plugins as LLVM libraries, the "backward compatibility" is gone. Given that fact, we can change existing interfaces w/o the need of consideration of backward compatibility.
  * ^ we also never had backwards compatibility afaik, certainly never tested to see if it worked


  * Changing register requires


  * Taking a refcount for registering libomptarget is awkward because every TU has a register requires which wants to initialize libomptarget.
  * Change this to work like registering kernels / globals?


  * New Link for meeting (see top of doc for link & ICS file)
  * OpenMP GPU Reduction
  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246266542&usg=AOvVaw2Ytil1KVCv1_Lau_CFUO3L)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246266647&usg=AOvVaw09m9NwnienB-MZAJJRBR9_) 


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246266794&usg=AOvVaw1fYUofur3LhxN3cRkR8q_o) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246266979&usg=AOvVaw0tLREoZogTf5NDW2iPeEg9) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * Allocators - managed memory missing on AMD


  * Does AMD have support?
  * ^ if managed means migratable, maybe. Might be platform dependent and involve the plugin setting an environment variable read by HSA. Open question about what omp_target_is_present() is supposed to return on migratable memory.


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246267580&usg=AOvVaw0f3FfDl7Y6dBg1W6esEUvx) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246267744&usg=AOvVaw1eOjIdjowYuVrjJINDVuuO) only adds the plugin runtime support


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246268043&usg=AOvVaw245iC2urN8KKa5mllH0gR-)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246268238&usg=AOvVaw0O2CwL3GMj-rbSLryQkwiR)
  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246268432&usg=AOvVaw1MHKEUlDlgRSqYto9Tjo9t): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [OpenMP Support -- Clang 16.0.0git documentation](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246268614&usg=AOvVaw08uU_-6LN5HN-FBllKbh1O) 


  * _OPENMP (Joachim)


  * Currently 201811 (= 5.0)



###
