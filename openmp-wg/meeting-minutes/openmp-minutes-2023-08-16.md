### 2023, Aug 16

Agenda

New 

  * Indirect codegen patches


  * Design point of whether address of indirect function has the same or different type to the address of a function
  * [[Libomptarget] Support mapping indirect host calls to device functions](https://www.google.com/url?q=https://reviews.llvm.org/D157918&sa=D&source=editors&ust=1778600246062068&usg=AOvVaw1ZMsqnTXoJqziL29tOg4rC)
  * [[OpenMP] Emit offloading entries for indirect target variables](https://www.google.com/url?q=https://reviews.llvm.org/D157738&sa=D&source=editors&ust=1778600246062196&usg=AOvVaw2Zvatelhu15lXIreSDhxzN)


  * Bug49334 causing build bots to hang


  * [https://github.com/llvm/llvm-project/issues/64733](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/64733&sa=D&source=editors&ust=1778600246062364&usg=AOvVaw2omTyS_dQ1cMOzNuIJb6SL)


  * Get a policy decision if we should generate errors in compiler or runtime for unsupported OpenMP APIs
  * Unsuccessful conversion from generic to generic SPMD
  * omp_get_num_procs() on the device not supported anymore? ([https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c#inline-9277](https://www.google.com/url?q=https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c%23inline-9277&sa=D&source=editors&ust=1778600246062756&usg=AOvVaw0616fgvj52c739nMW99SBa))


  * OMP Places [https://www.openmp.org/spec-html/5.1/openmpse62.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.1/openmpse62.html&sa=D&source=editors&ust=1778600246062897&usg=AOvVaw2CLuP3m7p5f6E8c2lersIb)
  * omp_get_place_num_procs(): [https://www.openmp.org/spec-html/5.0/openmpsu134.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.0/openmpsu134.html&sa=D&source=editors&ust=1778600246063038&usg=AOvVaw3wysX-kg-IAu7msIXHPB9H)


  * Update our clang support page


  * [https://clang.llvm.org/docs/OpenMPSupport.html](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html&sa=D&source=editors&ust=1778600246063214&usg=AOvVaw3V21kyUs1IweYqbF7KuJvl)


  * OMPT: Missing callbacks in plugin generic-elf-64bit, but: how to proceed with the plugin?  
(e.g. determine number of devices? Currently hardcoded:: #define NUM_DEVICES 4)


  * [https://github.com/llvm/llvm-project/issues/64487](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/64487&sa=D&source=editors&ust=1778600246063495&usg=AOvVaw3Kw9zdTbKWSejXLIFW9iWs)  
Or: simply connect OMPT and be done with it?
